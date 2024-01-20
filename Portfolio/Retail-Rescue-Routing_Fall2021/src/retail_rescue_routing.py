from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import pandas as pd #pip install pandas
import numpy as np
import datetime


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    matrix = pd.read_excel(r'src\miniTimeMatrix.xlsx')
    matrix.drop('Location ID', axis=1, inplace=True)
    data['num_nodes'] = int(matrix[matrix.columns[0]].count()) #indicates the number of locations visited
    data['time_matrix'] = matrix.values
    #test

    windows = pd.read_excel(r'src\miniTimeWindows.xlsx')
    windows.drop('Location ID', axis=1, inplace=True)
    #converts excel sheet to a list and casts the list to tuples
    timeWindows = windows.to_numpy().tolist()
    tupleWindows = [tuple(elt) for elt in timeWindows]
    
    #Converts the time windows from time variables (hour:minute:seconds) to minutes since the start of the shift
    minuteWindows = []
    date = datetime.date(1, 1, 1)
    shiftStartTime = datetime.time(7, 0, 0)
    shiftStart = datetime.datetime.combine(date, shiftStartTime)
    for index, timeTuple in enumerate(tupleWindows):
        startTime = timeTuple[0]
        endTime = timeTuple[1]

        date = datetime.date(1, 1, 1)
        start = datetime.datetime.combine(date, startTime) #the value need to be converted from a datetime.time type to a datetime.datetime type before they can be subtracted 
        end = datetime.datetime.combine(date, endTime)
        start_in_minutes = (start - shiftStart).total_seconds() / 60 #finds time difference between the time window and the shift start time (7:00 AM), converts it to seconds, and then into mintues
        end_in_minutes = (end - shiftStart).total_seconds() / 60

        minuteWindows.append((int(start_in_minutes), int(end_in_minutes)))

    minuteTuples = tuple(minuteWindows)

    data['time_windows'] = minuteTuples

    data['num_vehicles'] = 3
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            plan_output += '{0} Time({1},{2}) -> '.format(
                manager.IndexToNode(index), solution.Min(time_var),
                solution.Max(time_var))
            index = solution.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        plan_output += '{0} Time({1},{2})\n'.format(manager.IndexToNode(index),
                                                    solution.Min(time_var),
                                                    solution.Max(time_var))
        plan_output += 'Time of the route: {}min\n'.format(
            solution.Min(time_var))
        print(plan_output)
        total_time += solution.Min(time_var)
    print('Total time of all routes: {}min'.format(total_time))


def main():
    """Solve the VRP with time windows."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['time_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    #Add minimum vehicle usage constraint (ensures a roughly equal number of stops per vehicle)
    count_dimension_name = 'count'
    routing.AddConstantDimension(
        1, # increment by one every time
        data['num_nodes'] // data['num_vehicles'] + 1,  # max value forces equivalent # of jobs
        True,  # set count to zero
        count_dimension_name)
    count_dimension = routing.GetDimensionOrDie(count_dimension_name)

    # Add Time Windows constraint.
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        30,  # allow waiting time
        3000,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == data['depot']:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    # Add time window constraints for each vehicle start node.
    depot_idx = data['depot']
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(
            data['time_windows'][depot_idx][0],
            data['time_windows'][depot_idx][1])

    # Instantiate route start and end times to produce feasible times.
    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)


if __name__ == '__main__':
    main()
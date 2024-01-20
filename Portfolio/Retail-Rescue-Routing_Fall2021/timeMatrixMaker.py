import pandas as p
from pandas import ExcelWriter
import os

# MUST HAVE THE FOLLOWING FILES IN THE SAME DIRECTORY:
# By Day and By Week.xlsx
# timeMatrix.xlsx
# Outputs a spreadsheet with 5 separate sheets: one for each day
def generate_time_matrices():
    output_path = path = os.path.realpath(__file__)+'\\..\\dailyTimeMatrices.xlsx'
    df = p.read_excel(os.path.realpath(__file__)+'\\..\\By Day and By Week.xlsx')
    times = p.read_excel(os.path.realpath(__file__)+'\\..\\timeMatrix.xlsx')
    with ExcelWriter(output_path) as writer:
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            mon = df[df[day] == 1]['Location ID']
            mon.values.tolist()

            monday = times[times['Location ID'].isin(mon)]
            monday = monday.transpose()

            result = monday.loc[mon]
            result.columns = mon

            result.to_excel(writer, sheet_name=day)
        writer.save()

generate_time_matrices()
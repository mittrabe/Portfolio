import sqlalchemy as db

#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
#https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql

#featuers:
#sign in
#keep track of win/loss

#engine = db.create_engine('sqlite:///exampleDatabase.db')
engine = db.create_engine('sqlite:///C:\\Users\\1magi\\Desktop\\roguelikeToPlayChess\\chessDatabase.db')
connection = engine.connect()
metadata = db.MetaData()
cpuBoard = db.Table('cpuBoard',metadata,autoload=True,autoload_with=engine)

#print the column names
print(cpuBoard.columns.keys())

#Print full table metadata
#print(repr(metadata.tables['census']))

#Equivalent to 'SELECT * FROM census'
query = db.select([cpuBoard])

results = connection.execute(query)

resultSet = results.fetchall() 
print(resultSet)

#ResultSet = ResultProxy.fetchall()



#Inserting record one by one
playerBoard = ['Pawn','Queen','Empty','Empty','Empty','Rook']
playerBoardStr = ''

for piece in playerBoard:
    playerBoardStr += piece + ','
print(playerBoardStr)

query = db.insert(cpuBoard).values(turn=1,pieces=playerBoardStr[:-1])
resultProxy = connection.execute(query)

results = connection.execute(db.select([cpuBoard])).fetchall()
print(results)


import sqlite3

db = sqlite3.connect('movie.sqlite')
cursor = db.cursor()
start = int(input('Enter the start year: '))
end = int(input('Enter the end year: '))

command = '''SELECT O.year, M.name, M.runtime
             FROM Movie M, Oscar O
             WHERE M.id = O.movie_id
               AND O.type = 'BEST-PICTURE'
               AND O.year BETWEEN ? and ?
             ORDER BY O.year;'''

cursor.execute(command, [start, end])

count = 0
for row in cursor:
    print(row[0], row[1], '(' + str(row[2]) + ' minutes)')
    count += 1

if count == 0:
    print('There are no Best Picture winners between', start, 'and', str(end) + '.')

db.commit()
db.close()

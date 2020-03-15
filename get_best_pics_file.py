import sqlite3

db = sqlite3.connect('movie.sqlite')
cursor = db.cursor()
start = int(input('Enter the start year: '))
end = int(input('Enter the end year: '))

results_file = input('Enter the name of the results file: ')
outfile = open(results_file, 'w')


command = '''SELECT O.year, M.name, M.runtime
             FROM Movie M, Oscar O
             WHERE M.id = O.movie_id
               AND O.type = 'BEST-PICTURE'
               AND O.year BETWEEN ? and ?
             ORDER BY O.year;'''

cursor.execute(command, [start, end])

count = 0
for row in cursor:
    print(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]), file=outfile)
    count += 1

if count == 0:
    print('There are no Best Picture winners between', start, 'and', str(end) + '.')
else:
    print('Wrote', count, 'lines of results to the file.')

db.commit()
db.close()
outfile.close()

# get_director_movies.py
#
# A simple front end for our movie database in SQLite.
# It retrieves information about all movies by a given director
# in a given range of years.
#
# It uses a parameterized query to protect against SQL injections.
#
# This program only works if you put the database file in the same
# folder as the program.
#
# Computer Science 105

import sqlite3

# Connect to the database and create a cursor for it.
filename = input('name of database file: ')
db = sqlite3.connect(filename)
cursor = db.cursor()

dir_name = input("director's name: ")
start = input('start of year range: ')
end = input('end of year range: ')

# A command string with three placeholders.
command = '''SELECT M.name, M.year
             FROM Movie M, Person P, Director D
             WHERE M.id = D.movie_id
               AND P.id = D.director_id
               AND P.name = ?
               AND M.year BETWEEN ? AND ?;'''

# Execute the command, replacing the placeholders with the values of 
# the variables in the list [dirName, start, end].
cursor.execute(command, [dir_name, start, end])

count = 0
for row in cursor:
    print(row[0], '(' + str(row[1]) + ')')
    count = count + 1

if count == 0:
    print('There are no movies for that director in those years.')

db.commit()
db.close()

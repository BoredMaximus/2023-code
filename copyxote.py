import sqlite3
#so uhhh this is definitely my first assignment when it comes to programming in general.
#first thing i need to do is get the data from my database.
database = "limbusdatabase.db"
#now that i can get the data now, this string shows you the data is a simple way.
'''functions'''
def gametable(connection, tabletoread):
    cursor = connection.cursor()
    sqlgame = f"select * from {tabletoread}"
    cursor.execute(sqlgame)
    results = cursor.fetchall()
    if tabletoread.casefold() == "games".casefold():
    columns = [description[0] for description in cursor.description]:
    print(results)

        
with sqlite3.connect(database) as connection:
    tables = input("Which table would you like to select from?")
    gametable(connection, tables)
#so the basics are done. now is the time to make it better!
#review text data is stupidly big, idk how to make it neat sorry!
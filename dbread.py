import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('sample.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'"""
        sqlite_select_query = """SELECT * FROM blockchain"""

        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("row0: ", row[0])
            #print("row1: ", row[1])
            #print("row2: ", row[2])
            #print("row3: ", row[3])
            #print("row4: ", row[4])
            #print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
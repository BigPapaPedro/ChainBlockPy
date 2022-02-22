import json
import sqlite3


class DBDriver:

    def __init__(self, dbName):

        self.dbName = dbName

        self.sql_create_blockchain_table = """ CREATE TABLE IF NOT EXISTS blockchain (
                                                id integer PRIMARY KEY,
                                                forger_pub_key text NOT NULL,
                                                prev_block_hash text NOT NULL,
                                                signature text NOT NULL,
                                                time_stamp text NOT NULL
                                            ); """

        self.sql_insert_block = ''' INSERT INTO blockchain (
                                        id, forger_pub_key, prev_block_hash, signature, time_stamp)
                                        VALUES (?,?,?,?,?)
                                     '''

        self.sql_insert_record = ''' INSERT INTO blockchain (
                                                id, forger_pub_key, prev_block_hash, signature, time_stamp)
                                                VALUES (1, "forger_pub_key", "prev_block_hash", "signature", "time_stamp")
                                             '''
    #
    def createDB(self):

        print("DBDriver.createDB")

        connection = None

        try:
            connection = sqlite3.connect(self.dbName)
            cursor = connection.cursor()

            cursor.execute(self.sql_create_blockchain_table)

            connection.commit()
            connection.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if connection:
                connection.close()
                print("sqlite connection is closed")

    #
    def insertBlock(self, block):

        try:

            print('!!! insertBlock !!!')

            print("dbName")
            print(self.dbName)

            data_tuple = (block.blockCount, block.forger, block.prevHash, block.signature, block.timeStamp)

            print(data_tuple)


            connection = sqlite3.connect(self.dbName)
            cursor = connection.cursor()

            cursor.execute(self.sql_insert_block, data_tuple)

            connection.commit()
            connection.close()

        except sqlite3.Error as error:
            print("Error while inserting record", error)

        finally:
            if connection:
                connection.close()
                print("sqlite connection is closed")

    #
    def getBlocks(self):

        connection = sqlite3.connect(self.dbName)
        cursor = connection.cursor()

        cursor.execute("select * from blockchain")

        records = cursor.fetchall()

        print("row count:", records.count())

        for row in records:
            print("id: ", row[0])
            print("Signature: ", row[2])

        cursor.close()
        connection.close()

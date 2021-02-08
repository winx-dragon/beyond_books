import MySQLdb

def connection():
    # Edited out actual values
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="anki@123janvi",
                           db = "pythonregister")
    c = conn.cursor()

    return c, conn
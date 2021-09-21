import sqlite3

db = sqlite3.connect('database.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS Monday (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Tuesday (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Wednesday (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Thursday (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Friday (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS para_time (
    para1 TEXT,
    para2 TEXT,
    para3 TEXT,
    para4 TEXT,
    para5 TEXT,
    para6 TEXT
)""")
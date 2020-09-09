import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()

def create():
    curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')
def add(name,inventory,damage):
    curs.execute('INSERT INTO zoo VALUES("%s", %d, %f)'
                 % (str(name),int(inventory),float(damage)))
    conn.commit()
def select():
    curs.execute('SELECT * FROM zoo')
    return curs.fetchall()

data = select()

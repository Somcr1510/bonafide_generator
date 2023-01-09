import sqlite3
from datetime import datetime



conn=sqlite3.connect('REG.db')
conn.execute('''CREATE TABLE IF NOT EXISTS register(ID INTEGER PRIMARY KEY AUTOINCREMENT,
	URN INT NOT NULL,
	NAME TEXT NOT NULL,
	DEPT TEXT NOT NULL,
	YEAR TEXT NOT NULL,
	REASON TEXT NOT NULL,
	DATE TEXT NOT NULL
	);''')
conn.close()



def genarate(name,dept,year,date,reason):
	data=f'''                      Bonafide Certificate
	                   Presented to
	                  {name}
	               who is a bonafide student and pursueing the {dept} Engineering in {year} year. To the best of my knowledge,she/hebears a good moral character. 
	The medium of instruction during the entire programme is English. This certificate is issued on {date} her/his request for enabling her/his to obtain {reason} reason.
	          The Institute was formerly xxxxxxx college'''


	with open("certificate.doc","w") as fs:
		fs.write(data)


def entry(urn,name,dept,year,reason):
	conn=sqlite3.connect('REG.db')
	
	date_t=datetime.now()
	genarate(name,dept,year,date_t.date(),reason)
	
	date_t=str(date_t)
	conn.execute("INSERT INTO register(URN, NAME, DEPT, YEAR, REASON,DATE) VALUES(?, ?, ?, ?, ?, ?)",(urn,name,dept,year,reason,date_t))
	conn.commit()
	conn.close()
	


#entry("20131103", "SOM REVANKAR", "CSE","1st", "Other")

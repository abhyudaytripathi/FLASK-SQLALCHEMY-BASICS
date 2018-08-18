from flask import Flask 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine=create_engine("")## Database URI
db =scoped_session(sessionmaker(bind=engine))

def main():
	
	flights=db.execute('SELECT origin,destination, duration FROM test').fetchall()
    
	
	for flight in flights:
		print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes...")
	print("DONE !!!")
##app=Flask(__name__)

##@app.route('/')
##def 



if __name__=='__main__':
	main()
##	app.run(debug=True)

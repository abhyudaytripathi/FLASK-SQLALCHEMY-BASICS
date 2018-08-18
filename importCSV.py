from flask import Flask 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import csv
engine=create_engine("")## DATABASE URI
db =scoped_session(sessionmaker(bind=engine))

def main():
	with open("flights.csv") as f:
		reader=csv.reader(f)
		for origin,destination,duration in reader:
			db.execute("INSERT INTO  test (origin,destination,duration) VALUES (:origin,:destination,:duration)",
			{"origin":origin,"destination":destination,"duration":duration})
			print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
			db.commit()

##app=Flask(__name__)
##@app.route('/')
##def 
if __name__=='__main__':
	main()
##	app.run(debug=True)

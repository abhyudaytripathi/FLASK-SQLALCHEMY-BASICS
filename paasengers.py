from flask import Flask 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine=create_engine("") ##DataBase URI
db =scoped_session(sessionmaker(bind=engine))

def main():
	
	flights=db.execute('SELECT id,origin,destination, duration FROM test').fetchall()
    
	for flight in flights:
		print(f"Flight {flight.id} from {flight.origin} to {flight.destination} in {flight.duration} minutes...")
	flight_id=int(input("\nFlight ID :"))
	flight=db.execute("SELECT origin,destination,duration FROM test WHERE id=:id",{"id":flight_id}).fetchone()
	if flight is None:
		print("NO such flight :(")
		return
	passengers=db.execute("SELECT name from passengers WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
	print("\nPassengers : ")

	for passenger in passengers:
		print(passenger.name)
		if(len(passengers)==0):
			print("No Passengers !!!")
##app=Flask(__name__)

##@app.route('/')
##def 



if __name__=='__main__':
	main()
##	app.run(debug=True)

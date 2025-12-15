from flask import Flask, render_template, request
import sqlite3
from db import create_table, get_db_connection, insert_record
from services.calculate import calculate_final_premium


app = Flask(__name__)

create_table()

# routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        age = int(request.form["age"])
        vehicle_type = request.form["vehicle_type"]
        engine_type = request.form["engine_type"]
        vehicle_value = int(request.form["vehicle_value"])
        location = request.form["location"]
        accidents = int(request.form["accidents"])

    
        # calculate premium value
        final_premium, risk, risk_level = calculate_final_premium( age,
        vehicle_type,
        engine_type,
        location,
        accidents,
        vehicle_value)

        insert_record(age, vehicle_type, engine_type, vehicle_value, location, accidents, final_premium, risk, risk_level )
        
        return render_template(
            "result.html",
            premium = final_premium,
            risk = risk,
            risk_level = risk_level
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
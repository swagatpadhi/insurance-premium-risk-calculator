# Insurance Premium & Risk Calculator

A simple, rule-based web-application that estimates insurance premium and risk
for two-wheelers and four-wheelers based on user inputs. It uses risk multiplier model.
This project demonstrates backend development using Python, Flask, SQLite with a simple
frontend created with HTML and CSS. Resposiveness is taken care as well.

---

## Features
- Calculation of insurance premium using risk multipliers.
- Analysis of risk based on user profile.
- Clean and professional form-based UI.
- Flask backend with routing and templating.
- SQLite database for storing user data and calculations.
- Data safely stored, SQL injection is prevented.
- Whole project is modularized, components communicate via imports

---

## Tech Stack
- Frontend: HTML, CSS
- Backend: Python, Flask
- Database: SQLite

---

## Working of the project

users enter details such as age, vehicle type, vehicle price, engine type of the vehicle, 
their driving history, location. Each factor is mapped to a predifined risk multiplier.
For e.g.,
A 24 year old man's risk multiplier is 1.3, whereas for a 38 year old man's risk multiplier is 
1.0.
High risk indicates high premium amount.

Total risk factor is calculated by multiplying all the risk factors.
Then final insurance premium is calculated using the formula:  
    Final premium = Base premium * Total risk factor

After calculation, the result is displayed on a separate results page and stored in database.

---

## How to run the project

On terminal, type:

pip instal flask
python app.py

Then open:
http://localserver:5000/

---

## Future improvements and features

- Insurance history of user using the data stored in database.
- Learn more page on home page featuring working of the project.

---
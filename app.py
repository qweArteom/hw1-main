from flask import Flask, render_template
from models import session, Departure, Tour

app = Flask(__name__)

@app.route('/')
def index():
    departures = session.query(Departure).all()
    tours = session.query(Tour).all()
    return render_template('index.html', departures=departures, tours=tours)

if __name__ == '__main__':
    app.run(debug=True)
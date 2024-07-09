from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, BajajAuto, EicherMotors, HeroMotocorp, Infosys, Tcs, TvsMotors
import pandas as pd

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_dates', methods=['POST'])
def update_dates():
    update_all_dates()
    return redirect(url_for('index'))

@app.route('/calculate_ma', methods=['POST'])
def calculate_ma():
    calculate_moving_averages()
    return redirect(url_for('index'))

@app.route('/display_data')
def display_data():
    data = get_data()
    return render_template('results.html', data=data)

def update_all_dates():
    tables = [BajajAuto, EicherMotors, HeroMotocorp, Infosys, Tcs, TvsMotors]
    for table in tables:
        rows = table.query.all()
        for row in rows:
            row.Date = pd.to_datetime(row.Date, format='%d-%m-%Y')
            db.session.commit()

def calculate_moving_averages():
    tables = [BajajAuto, EicherMotors, HeroMotocorp, Infosys, Tcs, TvsMotors]
    for table in tables:
        rows = table.query.all()
        data = pd.DataFrame([(row.Date, row.ClosePrice) for row in rows], columns=['Date', 'ClosePrice'])
        data['20 Day MA'] = data['ClosePrice'].rolling(window=20).mean()
        data['50 Day MA'] = data['ClosePrice'].rolling(window=50).mean()
        for i, row in data.iterrows():
            db_row = table.query.filter_by(Date=row['Date']).first()
            db_row.MA20 = row['20 Day MA']
            db_row.MA50 = row['50 Day MA']
            db.session.commit()

def get_data():
    data = {
        'bajaj': BajajAuto.query.all(),
        'eicher': EicherMotors.query.all(),
        'hero': HeroMotocorp.query.all(),
        'infosys': Infosys.query.all(),
        'tcs': Tcs.query.all(),
        'tvs': TvsMotors.query.all()
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)

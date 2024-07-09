from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BajajAuto(db.Model):
    __tablename__ = 'bajaj_auto'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

class EicherMotors(db.Model):
    __tablename__ = 'eicher_motors'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

class HeroMotocorp(db.Model):
    __tablename__ = 'hero_motocorp'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

class Infosys(db.Model):
    __tablename__ = 'infosys'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

class Tcs(db.Model):
    __tablename__ = 'tcs'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

class TvsMotors(db.Model):
    __tablename__ = 'tvs_motors'
    Date = db.Column(db.Date, primary_key=True)
    ClosePrice = db.Column(db.Float)
    MA20 = db.Column(db.Float)
    MA50 = db.Column(db.Float)

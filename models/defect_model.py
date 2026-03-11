from extensions import db

class Defect(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    aircraft = db.Column(db.String(100))
    component = db.Column(db.String(100))
    defect = db.Column(db.String(200))
    severity = db.Column(db.String(50))
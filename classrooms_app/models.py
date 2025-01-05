from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cabinet(db.Model):
    __tablename__ = 'classrooms'
    index = db.Column(db.Integer, primary_key=True)
    cab_number = db.Column(db.Integer)
    sit_places = db.Column(db.Integer)
    cab_with_projector = db.Column(db.Boolean, default=False)
    cab_is_gym = db.Column(db.Boolean, default=False)
    cab_is_small = db.Column(db.Boolean, default=False)
    cab_is_computer = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Cabinet {self.cab_number}'


class Reservations(db.Model):
    cab_number = db.Column(db.Integer, primary_key=True)
    pair_number = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Cabinet {self.cab_number}'


if __name__ == '__main__':
    from classrooms_app import cabs_app
    with cabs_app.app_context():
        db.create_all()

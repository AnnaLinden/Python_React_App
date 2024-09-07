from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), uniquie = False, nullable = false)
    last_name = db.Column(db.String(80), uniquie = False, nullable = false)
    email = db.Column(db.String(120), uniquie = True, nullable = false)

    def to_json():
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,

        }
    
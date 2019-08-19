from feedback.extensions import db


class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer_name, dealer, rating, comments):
        self.customer = customer_name
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

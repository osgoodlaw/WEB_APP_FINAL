from app import db
from flask_login import UserMixin

# User model (assuming this exists in your app)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    # Relationship with Movie model (One-to-Many)
    movies = db.relationship('Movie', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    # Password hashing and verification methods
    @staticmethod
    def hash_password(password):
        from werkzeug.security import generate_password_hash
        return generate_password_hash(password)

    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


# Movie model with rating system
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(100))  # URL of the movie poster
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<Movie {self.title}>'
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationship with Movie and User models
    movie = db.relationship('Movie', backref='reviews', lazy=True)
    user = db.relationship('User', backref='reviews', lazy=True)

    def __repr__(self):
        return f'<Review by {self.user.username} for {self.movie.title}>'

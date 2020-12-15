from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    genres = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    

    def __repr__(self):
      return f'Venue id ={self.id},{self.name},{self.genres},{self.city},{self.state},{self.phone},{self.image_link},{self.shows},{self.facebook_link},{self.seeking_talent},{self.seeking_description},{self.shows}'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    genres = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    

    def __repr__(self):
      return f'Artist id={self.id}, name={self.name},genres={self.genres},city={self.city},state={self.state},phone={self.phone},image_link={self.image_link},facekbook_link={self.facebook_link},seeking_venue={self.seeking_venue},seeking_description={self.seeking_description},shows={self.shows}>'

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    venue = db.relationship('Venue', backref=db.backref('shows', lazy=True))
    artist = db.relationship('Artist', backref=db.backref('shows', lazy=True))

    def __repr__(self):
        return f'<Show id={self.id}, artist_id={self.artist_id},venue_id={self.venue_id}>'
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from models import Venue, Artist, Show
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from sqlalchemy import func

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)





# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#






    # TODO: implement any missing fields, as a database migration using Flask-Migrate



    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():

  locals = [{
    "city": "New Haven",
    "state": "CT",
    "venues": [{
      "id": 1,
      "name": "Toad\'s Place",
      "num_upcoming_shows": 1,
    }]
    }, {
      "id": 3,
      "name": "College Street Music Hall",
      "num_upcoming_shows": 2,
    
  }, {
    "city": "Philadelphia",
    "state": "PA",
    "venues": [{
      "id": 2,
      "name": "The Fillmore",
      "num_upcoming_shows": 0,
    }]
  }]
    
  
  venues = db.session.query(Venue).all()
  places = Venue.query.distinct(Venue.city, Venue.state).all()
  
  for place in places:
   locals.append({
     'city': place.city,  
     'state': place.state,
     'venues': []
     })
  for l in locals:
     for venue in venues:
          if l["state"] == venue.state and l["city"] == venue.city:
            l["venues"].append({
              "id": venue.id, 
              "name": venue.name,
              "num_upcoming_shows": db.session.query(Show).filter(Show.venue_id==venue.id).count()})
          
          return render_template('pages/venues.html', areas = locals)

      # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.


 
#Start of search implementation 12-10-20



@app.route('/venues/search', methods=['POST'])
def search_venues():
  search_term = request.form.get('search_term', '')
  search_results = db.session.query(Venue).filter(func.lower(Venue.name.ilike(f'%{search_term}%'))).all()
  count = len(search_results)

  response = {
      "count": count,
      "data": search_results
    }
  for venue in search_results:
    response[data].append(
        {"id": venue.id,
        "name": venue.name,
        "num_upcoming_shows": db.session().query(Show).filter(Show.venue_id == venue.id).count()}
      )

  return render_template('pages/search_venues.html', results=response, search_term=search_term)
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  
@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  venue = Venue.query.get(venue_id)
  
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id

  data1={
    "id": 1,
    "name": "Toad's Place",
    "genres": ["Alternative", "Hip-hop", "Modern Rock", "Pop-punk", "Classic Rock"],
    "address": "300 York Street",
    "city": "New Haven",
    "state": "CT",
    "phone": "203-634-8623",
    "website": "https://www.toadsplace.com",
    "facebook_link": "https://www.facebook.com/toadsplaceofficial",
    "seeking_talent": True,
    "seeking_description": "Where the Legends Play!",
    "image_link": "https://s.hdnux.com/photos/64/42/33/13772497/3/ratio3x2_800.jpg",
    "past_shows": [{
      "artist_id": 4,
      "artist_name": "",
      "artist_image_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fjammerzine.com%2Fjammerzine-exclusive-an-interview-with-nick-cove%2F&psig=AOvVaw05MI2Yi8QlKyNAMGJpFfei&ust=1607720841457000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCvi4CpxO0CFQAAAAAdAAAAABAE",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": ['local bands'],
    "past_shows_count": 1,
    "upcoming_shows_count": 1,
  }
  data2={
    "id": 2,
    "name": "The Fillmore",
    "genres": ["Rock", "R&B", "Hip-Hop", "Comedy"],
    "address": "29 East Allen Street",
    "city": "Philadelphia",
    "state": "PA",
    "phone": "215-309-0150",
    "website": "https://www.theduelingpianos.com",
    "facebook_link": "https://www.facebook.com/theduelingpianos",
    "seeking_talent": False,
    "image_link": "https://mavenprodcontent.blob.core.windows.net/media/FillmoreMPLS/Assets/The-Fillmore-Minny-Seat-View.jpg",
    "past_shows": ['The Wombats', 'Anthony Jeselnik'],
    "upcoming_shows": ['none'],
    "past_shows_count": 2,
    "upcoming_shows_count": 0,
  }
  data3={
    "id": 3,
    "name": "College Street Music Hall",
    "genres": ["Rock n Roll", "Jazz", "Alternative", "Techno", "Folk", "Spoken-word"],
    "address": "238 College Street",
    "city": "New Haven",
    "state": "CT",
    "phone": "203-867-2000",
    "website": "https://www.collegestreetmusichall.com/",
    "facebook_link": "https://www.facebook.com/CollegeStreetMusicHall",
    "seeking_talent": False,
    "image_link": "https://s.hdnux.com/photos/01/00/12/57/16821208/9/ratio3x2_1200.jpg",
    "past_shows": [{
      "artist_id": 5,
      "artist_name": "STRFKR",
      "artist_image_link": "https://www.collegestreetmusichall.com/e/strfkr-87370815461/",
      "start_time": "2020-12-10T23:00:00.000Z"
    }],
    "upcoming_shows": [{
      "artist_id": 4,
      "artist_name": "Mike Birbiglia",
      "artist_image_link": "https://bostonglobe-prod.cdn.arcpublishing.com/resizer/mPz3LVpAUaesrh85dKX-xhqtS3Y=/1280x0/filters:focal(3486x1151:3496x1141)/cloudfront-us-east-1.images.arcpublishing.com/bostonglobe/54NBTSUFP5EQDD4BQHZTQ5Q6MU.jpg",
      "start_time": "2035-04-01T10:00:00.000Z"
    }, {
      "artist_id": 6,
      "artist_name": "Jojo",
      "artist_image_link": "https://www.collegestreetmusichall.com/e/jojo-good-to-know-tour-96070343985/",
      "start_time": "2021-01-04T08:00:00.000Z"
    }, {
      "artist_id": 5,
      "artist_name": "STRFKR",
      "artist_image_link": "https://assets.simpleviewinc.com/simpleview/image/upload/crm/knoxville/strfkr-1582918421-Cropped_3e8a6085-5056-a348-3af1368a3dab2870.jpg",
      "start_time": "2035-04-15T20:00:00.000Z"
    }],
    "past_shows_count": 1,
    "upcoming_shows_count": 3,
  }
  
  data = list(filter(lambda d: d['id'] == venue_id, [data1, data2, data3]))[0]
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():

  form = VenueForm()
  if not form.validate_on_submit():
    flash('Missing fields')
    return render_template('forms/new_venue.html', form=form)

  try:
    name = request.form.get('name')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    phone = request.form.get('phone')
    image_link = request.form.get('image_link')
    website = request.form.get('website')
    facebook_link = request.form.get('facebook_link')
    seeking_talent = True if request.form.get('seeking_venue') == 'YES' else false
    seeking_description = request.form.get('seeking_description')
    new_venue=Venue(name=name, address=address, city=city, state=state, phone=phone, image_link=image_link, website=website, facebook_link=facebook_link, seeking_talent=seeking_talent)
    genres = set(request.form.getlist('genres'))
    for genre in genres:
      genre_present = Genre.query.filter_by(name=genre).all()
      if not genre_present:
        g = Genre(name=genre)
        db.session.add(g)
      else:
        g = genre_present[0]
      g.venues.append(new_venue)

      db.session.add(new_venue)
      db.session.commit() 
      flash('Venue ' + request.form['name'] + ' was successfully listed!')
  except:
    db.session.rollback()
    flash('An error occured. Venue ' + request.form['name'] + 'could not be listed.')
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  finally:
    db.session.close()
   
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  venue_id = request.form.get('venue_id', '')
  try:
    Venue.query.filter_by(id=venue_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  data=[{
    "id": 4,
    "name": "Mike Birbiglia",
  }, {
    "id": 5,
    "name": "STRFKR",
  }, {
    "id": 6,
    "name": "JoJo",
  }]
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():



  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  response={
    "count": 1,
    "data": [{
      "id": 4,
      "name": "Mike Birbiglia",
      "num_upcoming_shows": 1,
    }]
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  data1={
    "id": 4,
    "name": "Mike Birbiglia",
    "genres": ["Comedy"],
    "city": "Shrewsbury",
    "state": "MA",
    "phone": "326-123-5000",
    "website": "https://www.birbigs.com",
    "facebook_link": "https://www.facebook.com/MikeBirbiglia",
    "seeking_venue": True,
    "seeking_description": "I want to make your city laugh!",
    "image_link": "https://bostonglobe-prod.cdn.arcpublishing.com/resizer/mPz3LVpAUaesrh85dKX-xhqtS3Y=/1280x0/filters:focal(3486x1151:3496x1141)/cloudfront-us-east-1.images.arcpublishing.com/bostonglobe/54NBTSUFP5EQDD4BQHZTQ5Q6MU.jpg",
    "past_shows": [{
      "venue_id": 1,
      "venue_name": "Toad's Place",
      "venue_image_link": "",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
  data2={
    "id": 5,
    "name": "STRKFR",
    "genres": ["Alternative"],
    "city": "Portland",
    "state": "OR",
    "phone": "300-400-5000",
    "facebook_link": "https://www.facebook.com/strfkr",
    "seeking_venue": False,
    "image_link": "https://assets.simpleviewinc.com/simpleview/image/upload/crm/knoxville/strfkr-1582918421-Cropped_3e8a6085-5056-a348-3af1368a3dab2870.jpg",
    "past_shows": [{
      "venue_id": 3,
      "venue_name": "College Street Music Hall",
      "venue_image_link": "https://s.hdnux.com/photos/01/00/12/57/16821208/9/ratio3x2_1200.jpg",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
  data3={
    "id": 6,
    "name": "JOJO",
    "genres": ["Pop"],
    "city": "Brattleborro",
    "state": "VT",
    "phone": "432-325-5432",
    "facebook_link": "https://www.facebook.com/jojo",
    "website": "https://twitter.com/iamjojo",
    "seeking_venue": False,
    "image_link": "https://media.npr.org/assets/img/2020/05/01/jojo-2-credit-dennis-leupold-f4c681c74a66b24deae1936750ab534c0d8e0c60-s1300-c85.jpg",
    "past_shows": [],
    "upcoming_shows": [{
      "venue_id": 3,
      "venue_name": "College Street Music Hall",
      "venue_image_link": "https://s.hdnux.com/photos/01/00/12/57/16821208/9/ratio3x2_1200.jpg",
      "start_time": "2021-04-01T20:00:00.000Z"
    }, {
      "venue_id": 2,
      "venue_name": "The Fillmore",
      "venue_image_link": "https://mavenprodcontent.blob.core.windows.net/media/FillmoreMPLS/Assets/The-Fillmore-Minny-Seat-View.jpg",
      "start_time": "2021-06-08T20:00:00.000Z"
    }, {
      "venue_id": 1,
      "venue_name": "Toad\'s Place",
      "venue_image_link": "https://s.hdnux.com/photos/64/42/33/13772497/3/ratio3x2_800.jpg",
      "start_time": "2022-04-15T20:00:00.000Z"
    }],
    "past_shows_count": 0,
    "upcoming_shows_count": 3,
    }
  data = list(filter(lambda d: d['id'] == artist_id, [data1, data2, data3]))[0]
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist={

  }
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue=[{
    "id": 1,
    "name": "Toad's Place",
    "genres": ["Alternative", "Hip-hop", "Modern Rock", "Pop-punk", "Classic Rock"],
    "address": "300 York Street",
    "city": "New Haven",
    "state": "CT",
    "phone": "203-634-8623",
    "website": "https://www.toadsplace.com",
    "facebook_link": "https://www.facebook.com/toadsplaceofficial",
    "seeking_talent": True,
    "seeking_description": "Where the Legends Play!",
    "image_link": "https://s.hdnux.com/photos/64/42/33/13772497/3/ratio3x2_800.jpg",
    "past_shows": [{
      "artist_id": 4,
      "artist_name": "Mike Birbiglia",
      "artist_image_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fjammerzine.com%2Fjammerzine-exclusive-an-interview-with-nick-cove%2F&psig=AOvVaw05MI2Yi8QlKyNAMGJpFfei&ust=1607720841457000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCvi4CpxO0CFQAAAAAdAAAAABAE",
      "start_time": "2019-05-21T21:30:00.000Z"
    }]
  }]
    
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = Artist()
  if not form.validate_on_submit():
    flash('missing fields')
    return render_template('forms/new_artist.html')

  try:
    name = request.form.get('name')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    phone = request.form.get('phone')
    image_link = request.form.get('image_link')
    website = request.form.get('webiste')
    seeking_venue = TRUE if request.form.get('seeking_talent')
    seeking_description = request.form.get('seeking_descsription')
    new_artist = Artist(name=name, address=address, city=city, state=state, phone=phone, image_link=image_link, website=website, facebook_link=facebook_link, seeking_venue=seeking_venue)
    genres = set(reqest.form.getlist('genres'))
    if not genre in genre_present:
      g = Genre(name=genre)
      db.session.add(g)
    else:
      g = genre_present[0]
      g.artist.append(new_artist)

    db.session.add(new_artist)
    db.session.commit()
    flash('Artist ' + request.form['name'] + ' was successfully listed!')



  except:
    db.session.rollback()
    flash('Artist ' + request.form['name' + 'could not be added'])
  finally:
    db.session.close()

  


  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  # on successful db insert, flash success
  
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.

  return render_template('pages/shows.html', shows=results)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead

  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

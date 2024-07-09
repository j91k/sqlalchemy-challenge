# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt; (e.g., /api/v1.0/2016-08-23)<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt; (e.g., /api/v1.0/2016-08-23/2017-08-23)"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    most_recent_date_str = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date_str, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    precipitation_dict = {date: prcp for date, prcp in results}

    return jsonify(precipitation_dict)

@app.route('/api/v1.0/stations')
def stations():
    active_stations = session.query(Measurement.station, func.count(Measurement.station))\
    .group_by(Measurement.station)\
    .order_by(func.count(Measurement.station).desc()).all()

    active_stations_list = [{'station': station, 'count': count} for station, count in active_stations]

    return jsonify(active_stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    most_active_station = session.query(Measurement.station, func.count(Measurement.station))\
        .group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc()).first()[0]

    latest_date = session.query(func.max(Measurement.date)).filter(Measurement.station == most_active_station).scalar()
    one_year_ago = dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)

    temperature_data = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == most_active_station,
        Measurement.date >= one_year_ago
    ).all()

    temperatures_list = [{'date': date, 'temperature': temp} for date, temp in temperature_data]

    return jsonify(temperatures_list)

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temp_range(start, end=None):
    
    if not end:
        end = session.query(func.max(Measurement.date)).scalar()

    temp_stats = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(
        Measurement.date >= start,
        Measurement.date <= end
    ).all()

    temp_stats_list = [{'TMIN': min_temp, 'TAVG': avg_temp, 'TMAX': max_temp} for min_temp, avg_temp, max_temp in temp_stats]
    
    return jsonify(temp_stats_list)

if __name__ == '__main__':
    app.run(debug=True)
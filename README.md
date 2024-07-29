# SQLALCHEMY PROJECT
## Climate Analysis and Flask API

### Overview
This project involved climate analysis using an SQLite database of weather data for Hawaii. The analysis was performed using Python and SQLAlchemy, and the results were displayed via a Flask API. The API provided various endpoints to query and retrieve climate data.

### Requirements
- Python 3.8+
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

### Setup Instructions
1. Cloned the repository
2. Created and activated a virtual environment
3. Installed the required packages
4. Ran the Flask application <code style ="color:blue">Python app.py</code>

### Usage
#### Available API Endpoints
1. **Homepage**  : Listed all available routes 

    GET `/`

2. **Precipitation Data** : Retrieved the last 12 months of precipitation data.

    GET `/api/v1.0/precipitation`

3. **Stations** : Returned a list of all stations.

    GET `/api/v1.0/stations`

4. **Temperature Observations**: Returned temperature observations of the most active station for the previous year.

    GET `/api/v1.0/tobs`

5. **Temperature Stats from Start Date**: Returned the minimum, average, and maximum temperatures from the start date to the end of the dataset.

    GET `/api/v1.0/<start>`

6. **Temperature Stats from Start to End Date**: Returned the minimum, average, and maximum temperatures for the specified date range.

    GET `/api/v1.0/<start>/<end>`


# SQLALCHEMY-CHALLENGE
## Climate Analysis and Flask API

### Overview
This project involves climate analysis using SQLite database of weather data for Hawaii. The analysis is performed using Python and SQLAlchemy, and the results are displayed via a Flask API. The API provides various endpoints to query and retrieve climate data.

### Requirements
- Python 3.8+
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

### Setup Instructions
1. Clone the repository
2. Create and activate a virtual environment
3. Install the required packages
4. Run the Flask application <code style ="color:blue">[Python app.py](sqlalchemy-challenge\SurfsUp\Erna_climate_starter.ipynb)</code>

### Usage
#### Available API Endpoints
1. **Homepage**  : List all available routes 

    GET `/`

2. **Precipitation Data** : Retrieves last 12 months of precipitation data.

    GET `/api/v1.0/precipitation`

3. **Stations** : Returns a list of all stations.

    GET `/api/v1.0/stations`

4. **Temperature Observations**: Returns temperature observations of the most active station for the previous year.

    GET `/api/v1.0/tobs`

5. **Temperature Stats from Start Date**: Returns the minimun, averaget, and maximum temperatures from the start date to the end of the dataset.

    Get `/api/v1.0/<start>`

6. **Temperature Stats from Start to End Date**: Returns the minimum, average, and maximum temperatures for the specified date range.

    GET `/api/v1.0/<start>/<end>`

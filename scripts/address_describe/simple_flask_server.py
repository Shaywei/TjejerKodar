import os
import time

import requests

from flask import Flask, render_template

INSTA_ACCESS_TOKEN = ''
WEATHER_API_KEY = ''
GOOGLE_MAPS_STATIC_API_KEY = ''
GOOGLE_MAPS_STREETVIEW_API_KEY = ''

# Better way (yet still kinda bad) to load secrets
# secrets = dict()
# with open("SECRETS.json") as f:
#     secrets = json.loads(f.read())

# 'static_folder' is used for serving static files
proj_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(proj_dir, 'static')


app = Flask(__name__)


def get_photos(lati, longi):
    '''
    This method queries Instagram 'media/search' API endpoint for
    a given lati/longi and returns the reply as a json()
    '''
    raise NotImplementedError()


def _get_weather(lati, longi):
    '''
    This function queries the forcast.io '/forcast' API endpoint for
    a given lati/longi and processes the data to return a single string
    which is a description of the current temperature and summary of
    daily forecast
    '''
    raise NotImplementedError()


def _get_lati_longi(address):
    '''
    This function takes an address string and return the lati/longi for
    that address
    '''
    raise NotImplementedError()


def _save_static_file(name, content):
    '''
    This fucntion takes a name of a file to create in the
    /static folder (which can be used to load images) and
    write the 'content' given to it.

    This is useful if an API gives you a binary content
    '''

    filename = os.path.join(static_folder, name)

    # Delete it if exists
    try:
        os.remove(filename)
    except OSError:
        pass

    # Write content to file
    with open(filename, 'w+b') as f:
        f.write(content)


def get_static_map(lati, longi):
    '''
    This function queries the google maps '/staticmap' API endpoint for
    a given lati/longi gets a static map image. Since the API returns
    the image itself, this funciton need to save that image to disk in
    the /static folder and then return a STRING which is
    /static/<image_name>?<random_number>
    The latter is to avoid browser caching.
    '''

    raise NotImplementedError()


def get_streetview(lati, longi):
    '''
    This function queries the google maps '/streetview' API endpoint for
    a given lati/longi gets a static map image. Since the API returns
    the image itself, this funciton need to save that image to disk in
    the /static folder and then return a STRING which is
    /static/<image_name>?<random_number>
    The latter is to avoid browser caching.
    '''

    raise NotImplementedError()


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/describe/<address>')
def describe_address(address):
    lati, longi = _get_lati_longi(address)

    # This is just text describing the weather
    weather = _get_weather(lati, longi)

    # This is a list jsons which has a )
    photos_urls = get_photos(lati, longi)

    # These are filenames for a jpg file containing the image
    static_map = get_static_map(lati, longi)
    street_view = get_streetview(lati, longi)

    return render_template('./address.html', address=address.capitalize(),
                           lati=lati, longi=longi, weather=weather,
                           photos=photos_urls, static_map=static_map,
                           street_view=street_view)


if __name__ == "__main__":
    app.run(port=8080, debug=True)

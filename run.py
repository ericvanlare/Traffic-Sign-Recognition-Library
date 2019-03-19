import argparse
import random
from os import system
import datetime

from creds import dev_key, geocoders_name

from PIL import Image
import google_streetview.api
from geopy import geocoders

def get_latlng(location):
    gn = geocoders.GeoNames(username='evanlare')
    loc = random.choice(gn.geocode(location, exactly_one=False))
    return loc[1]

def search(latlng):
    # Define parameters for street view api
    params = [{
        'size': '600x300', # max 640x640 pixels
        'location': str(latlng[0])+','+str(latlng[1]),
        # 'heading': '151.78',
        # 'pitch': '-0.76',
        'key': dev_key
    }]

    # Create a results object
    results = google_streetview.api.results(params)

    # Download images to directory 'downloads'
    results.download_links('downloads')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', dest='city',
                        help='e.g. San\\ Jose')
    parser.add_argument('--state', dest='state',
                        help='e.g. CA')
    args = parser.parse_args()
    print ('City: ' + args.city + ", " + args.state)
    return args

def main():
    args = parse_args()
    latlng = get_latlng(args.city+', '+args.state)
    search(latlng)
    system('open downloads/gsv_0.jpg')
    is_sign = input('Does this image contain a traffic sign? ')

    img = Image.open('downloads/gsv_0.jpg')
    sign = 'not_sign'
    if is_sign.lower() == 'yes':
        sign = 'sign'
    out = '/Users/evanlare/School/ELEN239/Traffic-Sign-Recognition-Library/img/' + sign + '/gsv' + str(datetime.datetime.now()).replace(' ', '').replace(':', '.') + '.jpg'
    img.save(out)

if __name__ == "__main__":
    main()

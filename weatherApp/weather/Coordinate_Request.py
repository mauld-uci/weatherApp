import json
import urllib.parse
import urllib.request
#IpStack API

API_KEY = '954143e557452a37b7dccd70f920e750'

BASE_URL ='http://api.ipstack.com/'
#http://api.ipstack.com/169.234.77.38?access_key=954143e557452a37b7dccd70f920e750
location_string = ""
def build_search_url():
    return BASE_URL + 'check?' + 'access_key=' + API_KEY


def get_result(url:str):
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response!= None:
            response.close()


def pull_current_data(json_object):
    global location_string
    latitude = json_object['latitude']
    longitude = json_object['longitude']
    city = json_object['city']
    region_code = json_object['region_code']
    zip_code = json_object['zip_code']
    location_string = str(city) + ", " + str(region_code) + " " + str(zip_code)
    return (latitude, longitude)


def run():
    url = build_search_url()
    json_object = get_result(url)
    return pull_current_data(json_object)

def get_location_string():
    global location_string
    return location_string

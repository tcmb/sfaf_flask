from flask import Flask, redirect, request, render_template
from constants import *
from secrets import *
from urllib import urlencode
from urlparse import urljoin
import requests
import json

from stravalib.client import Client
from helpers import matches_criteria, get_min_dist, km


app = Flask(__name__)
my_host = LOCALHOST
#my_host = REMOTEHOST

my_app_params = {
    'client_id': CLIENT_ID,
    'redirect_uri': urljoin(my_host, '/authorized/'),
    'response_type': 'code',
    'approval_prompt': 'auto',
    'scope': 'public'
}

authorization_url = STRAVA_AUTH_URL + '?' + urlencode(my_app_params)


def get_user_token(authorization_code):
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorization_code
    }
    user_token_response = requests.post(STRAVA_TOKEN_URL, data=params)
    returned_data = json.loads(user_token_response.text)
    user_token = returned_data.get('access_token')
    return user_token


@app.route('/')
def authoriziation_redirect():
    """
    Redirect the user to the Strava authorization page.
    Assumptions:
    - User has not authorized this app yet
    - User has a Strava account
    (- User will authorize this app and return)
    """
    return redirect(authorization_url)


@app.route('/authorized/')
def authorized():
    """
    Run activity search for authorized user.
    Assumptions:
    - User has authorized this app
    - User agent is being sent from Strava oauth redirect back to us
    - Token exchange will succeed
    (- Getting activities will work)
    """
    authorization_code = request.args.get('code')
    if authorization_code:
        user_token = get_user_token(authorization_code)
        client = Client(user_token)
        return render_template('index.html', user_token=user_token)
    else:
        #return 400
        pass

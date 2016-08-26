# -*- coding: utf-8 -*-
import logging
import os
import sys
import json
from urlparse import urlsplit
from urlparse import urlunsplit

import requests
import random
from flask import Flask
from flask import request
from flask import Response

from mattermost_giphy.settings import *


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
app = Flask(__name__)

phrase = ['https://media4.giphy.com/media/Jp5yOwzJL8oMM/giphy.gif','http://media4.giphy.com/media/Wy0Pqicf1N21i/giphy.gif','http://media4.giphy.com/media/12MjqLSQ2wDER2/giphy.gif','https://media4.giphy.com/media/QgZOTNx3clTzO/giphy.gif',
'https://media4.giphy.com/media/Gxk0jI06myhpu/giphy.gif','https://media4.giphy.com/media/wWEoKRRgmFH20/giphy.gif','https://media4.giphy.com/media/EKNJZk5gH6QXC/giphy.gif',
'https://media4.giphy.com/media/PVhrCQyyGzAru/giphy.gif',
'https://media4.giphy.com/media/Hp8jtPPTWiH7O/giphy.gif',
'https://media4.giphy.com/media/v40h5Z4X7aLVS/giphy.gif',
'https://media4.giphy.com/media/tpWcdE3dopRhS/giphy.gif',
'https://media4.giphy.com/media/1266sbyhJZwgyk/giphy.gif',
'https://media4.giphy.com/media/rAKdqZ8nfiaZi/giphy.gif',
'https://media4.giphy.com/media/8ztjJmHGY8tva/giphy.gif'
]

@app.route('/new_post')
def root():
    """
    Home handler
    """
    print "la" 
    return "OK"


@app.route('/', methods=['POST'])
def new_post():
    """
    Mattermost new post event handler
    """
    try:
        print "ici"
        # NOTE: common stuff
        slash_command = False
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form

        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        #if MATTERMOST_GIPHY_TOKEN.find(data['token']) == -1:
        #    raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            slash_command = True
            resp_data['response_type'] = 'in_channel'

        motivation = random.choice(phrase)
        #resp_data['text'] = motivation
        resp_data['text'] = '''`{}` asked for boobs :\n
    {}'''.format(data.get('user_name').title(), motivation)
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp

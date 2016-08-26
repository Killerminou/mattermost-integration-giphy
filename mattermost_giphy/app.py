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

phrase = ['Do it', 'Just do it', 'Don\'t let your dreams be dreams', 'Make your dreams come true  Just do it', 'Yesterday you said tomorrow so just do it',
 'Some people dream of success while you\'re gonna wake up and work hard at it', 'Nothing is impossible', 
 'You should get to the point where anyone else would quit and you\'re not going to stop there  No, what are you waiting for ?',
 'Do it  Just do it',
'Yes you can',
'Just do it  *flexing muscles*',
'If you\'re tired of starting over, stop giving up',
'https://www.youtube.com/watch?v=ZXsQAXx_ao0'
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
        resp_data['text'] = '''`{}` asked for Boobs :\n
    {}'''.format(data.get('user_name').title(), motivation)
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp

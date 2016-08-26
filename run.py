#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from mattermost_giphy.app import app
from mattermost_giphy.settings import *


if __name__ == "__main__":

    port = os.environ.get('MATTERMOST_GIPHY_PORT', None) or os.environ.get('PORT', 5000)
    host = os.environ.get('MATTERMOST_GIPHY_HOST', None) or os.environ.get('HOST', '0.0.0.0')
    app.run(host=str(host), port=int(port))

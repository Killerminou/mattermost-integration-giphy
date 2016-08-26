#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from mattermost_giphy.app import app
from mattermost_giphy.settings import *


if __name__ == "__main__":
#    if not GIPHY_API_KEY:
#        print("GIPHY_API_KEY must be configured. Please see README.md for instructions")
#        sys.exit()

#    if not MATTERMOST_GIPHY_TOKEN:
#        print("MATTERMOST_GIPHY_TOKEN must be configured. Please see README.md for instructions")
#        sys.exit()

    port = os.environ.get('MATTERMOST_GIPHY_PORT', None) or os.environ.get('PORT', 5000)
    host = os.environ.get('MATTERMOST_GIPHY_HOST', None) or os.environ.get('HOST', '0.0.0.0')
    app.run(host=str(host), port=int(port))

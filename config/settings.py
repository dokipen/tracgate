# This file contains python variables that configure Lamson for email processing.
import logging

relay_config = {'host': 'localhost', 'port': 8825}

receiver_config = {'host': 'localhost', 'port': 8823}

handlers = ['app.handlers.create_ticket']

router_defaults = {'host': 'localhost'}

template_config = {'dir': 'app', 'module': 'templates'}

TRAC_URL = "http://tracgate:tracgate@localhost:7421/login/xmlrpc"

# the config/boot.py will turn these values into variables set in settings

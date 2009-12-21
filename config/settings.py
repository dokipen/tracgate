# This file contains python variables that configure Lamson for email processing.
import logging

from app.model.single_trac_resolver import SingleTracResolver

relay_config = {'host': 'localhost', 'port': 8825}

receiver_config = {'host': 'localhost', 'port': 8823}

handlers = ['app.handlers.trac_gate']

router_defaults = {'host': 'localhost'}

template_config = {'dir': 'app', 'module': 'templates'}

trac_resolver = SingleTracResolver("http://tracgate:tracgate@localhost:7421/login/xmlrpc")

# the config/boot.py will turn these values into variables set in settings

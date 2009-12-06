import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay, TRAC_URL
from lamson import view
from email import Utils
from xmlrpclib import ServerProxy


@route("(project)@(host)", project=".+", host=".+")
def START(message, project=None, host=None):
    tracserver = ServerProxy(TRAC_URL)
    ticketid = tracserver.tracgate.recieve(message.body(), message.base.headers)
    return START



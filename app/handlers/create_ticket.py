import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay, TRAC_URL
from lamson import view
from xmlrpclib import ServerProxy


@route("(project)[+](resource_uid)@(host)", project="[^+]+", resource_uid=".+", host=".+")
@route("(project)@(host)", project="[^+]+", host=".+")
def START(message, project=None, resource_uid=None, host=None):
    tracserver = ServerProxy(TRAC_URL)
    ticketid = tracserver.tracgate.recieve(
        message.body(), 
        message.base.headers,
        resource_uid or ''
    )
    return START



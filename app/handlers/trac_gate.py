import logging
from lamson.routing import route, route_like, stateless
from config.settings import trac_resolver
from lamson import view


@route("(project)[+](resource_uid)@(host)", project="[^+]+", resource_uid=".+", host=".+")
@route("(project)@(host)", project="[^+]+", host=".+")
def START(message, project=None, resource_uid=None, host=None):
    tracserver = trac_resolver.resolve(project)
    return_val = tracserver.tracgate.recieve(
        message.body(), 
        message.base.headers,
        resource_uid
    )
    return START



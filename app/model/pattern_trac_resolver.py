from xmlrpclib import ServerProxy

class PatternTracResolver:
    """
    Uses a regex pattern with on %s placeholder for the name part of the email
    to fill in. 

    For example, if the pattern were http://user:pass@host/%s/login/xmlrpc and
    the incoming email was addressed to project1+someparam@host, then tracgate
    would connect to http://user:pass@host/project1/login/xmlrpc.
    """
    def __init__(self, pattern):
        self.pattern = pattern

    def resolve(self, name):
        # TODO: cache ServerProxy
        return ServerProxy(self.pattern%name, allow_none=True)

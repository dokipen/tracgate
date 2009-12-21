from xmlrpclib import ServerProxy

class SingleTracResolver:
    """
    Use this if you only have one Trac instance.  Always returns the trac 
    address passed to __init__.
    """
    def __init__(self, addr):
        self.proxy = ServerProxy(addr, allow_none=True)

    def resolve(self, name):
        return self.proxy

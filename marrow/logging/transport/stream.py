# encoding: utf-8

import sys


__all__ = ['StreamTransport']



class StreamTransport(object):
    """Externally managed stream."""
    
    __slots__ = ('lock', 'stream', 'format')
    
    parallel = False # Note the additional 'lock' slot, above.
    
    def __init__(self, config):
        self.format = config.format
        self.stream = config.get('stream', sys.stderr)
    
    def startup(self):
        pass
    
    def deliver(self, message):
        self.stream.write(self.format(message))
    
    def shutdown(self):
        pass

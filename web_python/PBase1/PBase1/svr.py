
from xmlrpc.server import SimpleXMLRPCServer



def study():
    print ("I've using Python.!")
    port=8080
    sxr=SimpleXMLRPCServer(("", port), allow_none=True)
    sxr.register_function(study)
    sxr.serve_forever()

"""
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def get_power(n,m):
    return n**m

server = SimpleXMLRPCServer(("0.0.0.0", 8081))
print ("start service get power on 0.0.0.0 8081...")
server.register_function(get_power, "get_power")
server.serve_forever()
"""

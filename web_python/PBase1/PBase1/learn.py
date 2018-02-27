import xmlrpc.client

sp = xmlrpc.client.ServerProxy("http://192.168.1.107:8080")
sp.study()


"""
import xmlrpclib

server_power = xmlrpclib.ServerProxy("http://192.168.1.107:8081/")
print "3**2 = %d" %(server_power.get_power(3,2))
print "2**5 = %d" %(server_power.get_power(2,5))
"""

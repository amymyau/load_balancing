#Begin Portion 1#
import random
class Server:
    def __init__(self):
        self.connections = {}
    def __str__(self):
        return "{:.2f}%".format(self)
    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id]=round(connection_load,2)

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]
    def load(self):
        """Calculates the current load for all connections."""        
        total = 0
        # Add up the load for each of the connections
        for value in self.connections.values():
           total += value
        return total

    
#End Portion 1#

server = Server()
server.add_connection("10.2.3.4")
print(server.load())

server.close_connection("10.2.3.4")
print(server.load())

#Begin Portion 2#

     
class LoadBalancing:
    def __init__(self):
        self.connections = {}
        self.servers = [Server()]
        
      
    def add_connection(self, connection_id):
        if self.ensure_availability() == True:
          self.servers.append(Server())
        
        self.servers[-1].add_connection(connection_id)
        self.connections[connection_id]=self.servers[-1].load()
            
    def close_connection(self, connection_id):
        
        for server in self.servers:            
            if connection_id in server.connections:
                self.servers.remove(server)          
                        
        del self.connections[connection_id] 
        
        
            
    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        sum = 0
        avg = 0
        for server in self.servers:
           sum += server.load()
        avg = sum/len(self.servers) 
        return  avg
   
    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
           return True
           

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server.load()) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print('{:.2f}'.format(l.avg_load()))
print(l)


l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())


for connection in range(20):
    l.add_connection(connection)
print(l.avg_load())

print(l.avg_load())





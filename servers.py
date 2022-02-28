import sys, json

sys.path.append(".")
from services import Service

class Servers:

    def __init__(self):
        with open('servers.json', 'r') as f:
            self.servers = json.load(f)
    
    def updateServer(self, serverUpdate):
        for index, server in enumerate(self.servers):
            if (server["name"] == serverUpdate["name"]):
                self.servers[index] = serverUpdate
                with open("servers.json", "w") as jsonFile:
                    json.dump(self.servers, jsonFile)

    def updateServersAcordingToServices(self):
        service = Service()
        for index, server in enumerate(self.servers):
            server["active"] = service.isActive(server["serviceName"])
            server["details"] = service.serviceDetails(server["serviceName"])
            self.servers[index] = server
        
        with open("servers.json", "w") as jsonFile:
            json.dump(self.servers, jsonFile)
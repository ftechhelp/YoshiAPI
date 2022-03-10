import os, subprocess
from os.path import exists

class Service:

    def isActive(self, serviceName):
        activeCode = os.system('systemctl is-active --quiet ' + serviceName)
        if activeCode == 0:
            return True
        
        return False

    def serviceDetails(self, serviceName):
        servicePath = '/etc/systemd/system/' + serviceName + '.service'
        details = ""
        if exists(servicePath):
            details = str(subprocess.run(["cat", servicePath], capture_output=True).stdout)
        else:
            details = "Service does not exist"
        
        return details

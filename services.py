import os

class Service:

    def isActive(self, serviceName):
        activeCode = os.system('systemctl is-active --quiet ' + serviceName)
        if activeCode == 0:
            return True
        
        return False

    def serviceDetails(self, serviceName):
        details = os.system('cat /etc/systemd/system/' + serviceName + '.service')
        if details == 256:
            return "Service does not exist"
        
        return details

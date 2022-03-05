import os, subprocess

class Service:

    def isActive(self, serviceName):
        activeCode = os.system('systemctl is-active --quiet ' + serviceName)
        if activeCode == 0:
            return True
        
        return False

    def serviceDetails(self, serviceName):
        servicePath = 'cat /etc/systemd/system/' + serviceName + '.service'
        details = ""
        if os.path.isfile(servicePath):
            details = subprocess.check_output('cat /etc/systemd/system/' + serviceName + '.service', shell=True)
        else:
            details = "Service does not exist"
        
        return details

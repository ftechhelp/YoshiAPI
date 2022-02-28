import platform, sys, json, cpuinfo, GPUtil, psutil

class Stats:

    def __init__(self):
        with open('stats.json', 'r') as f:
            self.stats = json.load(f)

    def updateStatsAcordingToServer(self):
        self.stats["os"] = platform.platform()
        self.stats["cpu"] = cpuinfo.get_cpu_info()["brand_raw"]
        self.stats["gpu"] = GPUtil.getGPUs()
        self.stats["ram"] = str(round(psutil.virtual_memory().total/(1024.**3), 2)) + "GB"

        with open("stats.json", "w") as jsonFile:
            json.dump(self.stats, jsonFile)
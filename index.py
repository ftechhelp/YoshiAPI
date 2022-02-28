from flask import Flask, jsonify, request
import sys

sys.path.append(".")
from servers import Servers
from stats import Stats

app = Flask(__name__)
servers = Servers()
stats = Stats()

@app.route('/servers')
def get_servers():
    servers.updateServersAcordingToServices()
    return jsonify(servers.servers)

@app.route('/stats')
def get_stats():
    stats.updateStatsAcordingToServer()
    return jsonify(stats.stats)
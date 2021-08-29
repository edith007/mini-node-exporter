import socket
import os
from flask import Flask, request, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Gauge

# Configure application
app = Flask(__name__)

noad_load = Gauge("noad_load", "load averages for 1m 5m 15m", ["duration"])
noad_uptime = Gauge("noad_uptime", "node uptime")

def get_loadavg():
    loadavg = {}
    load1m, load5m, load15m = os.getloadavg()
    loadavg["1m"] = load1m
    loadavg["5m"] = load5m
    loadavg["15m"] = load15m
    return loadavg

def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return str(uptime_seconds)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/info/hostname", methods=["GET"])
def return_hostname():
    headers = {'Content-Type': 'text/plain'}
    return request.remote_addr, 200, headers

@app.route("/info/uptime", methods=["GET"])
def get_uptime():
    headers = {'Content-Type': 'text/plain'}
    up_time = uptime()
    noad_uptime.set(up_time)
    return up_time, headers

@app.route("/info/load", methods=["GET"])
def return_avgload():
    header = {"Content-Type": "text/plain"}
    data = get_loadavg()

    noad_load.labels("1m").set(data["1m"])
    noad_load.labels("5m").set(data["5m"])
    noad_load.labels("15m").set(data["15m"])

    return jsonify(data)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})

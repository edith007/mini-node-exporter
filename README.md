# mini-node-exporter

In order to run the application use the following command:
> docker-compose up

Several End-points are:
- `http://127.0.0.1:23333/info/hostname` show the hostname with plain text
- `http://127.0.0.1:23333/info/uptime` show the uptime of the system in seconds with plain text
- `http://127.0.0.1:23333/info/load` show the load average in 1m, 5m and 15m with JSON, example `{"1m": 0.57, "5m":0.80, "15m":0.77}`
- `http://127.0.0.1:23333/metrics` expose metrics that could be scraped by prometheus

Startup the monitoring stack of prometheus and grafana, and show the metrics on a grafana dashboard.

Implemented Features

- execute mini-node-exporter on host.
- execute prometheus on the host, and configure it for collecting metrics from `mini-node-exporter`
- execute grafana on the host, and configure it for using prometheus as the datasource
- create a grafana dashboard for showing these metrics
- orcherating the monitroing stack and `mini-node-exporter` application by `docker-compose`

### Prometheus
![prometheus](https://user-images.githubusercontent.com/53316982/131267449-95fcbc3c-dd20-4bbd-941d-7c627fbe9e4d.png)

### Grafana LoadTime
![grafana_node_load](https://user-images.githubusercontent.com/53316982/131268198-2dcad1b9-76aa-46cc-b9d2-2d0970485904.png)


#### Grafana UpTime
![grafana_noad_uptime](https://user-images.githubusercontent.com/53316982/131268212-615a94ce-d5d0-4fd4-a3a9-4e725516d0cf.png)





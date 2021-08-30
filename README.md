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
![prometheus](https://user-images.githubusercontent.com/53316982/131285539-4199bc29-13ea-49dc-b1d4-ca412a6be843.png)


### Grafana LoadTime
![grafana_node_load](https://user-images.githubusercontent.com/53316982/131285567-cb85fdf5-d460-4e76-9ae3-986576ddebb9.png)


#### Grafana UpTime
![Grafana_node_up_time](https://user-images.githubusercontent.com/53316982/131285595-8085a6af-9e3c-4ad7-ae7b-7ac72dc3c8a7.png)





## Open Telemetry - Spring Boot - Prometheus - Exemplar - Loki - Tempo - Grafana

You can find a complete tutorial in my blog -> 
https://k8staz.com/setting-up-open-source-observability-stack-on-kubernetes-from-scratch

### Demo

Download Multipass [here](https://multipass.run/)

Create Ubuntu instance on local environment:

`$ multipass launch --name demo --mem 4G --disk 30G`

Log in into the server:

```
$ multipass shell demo
$ sudo su
```

Clone the repo: 

```
$ git clone https://github.com/mangokingTW/otel-springboot-grafana-tools.git
$ cd otel-springboot-grafana-tools
```

Running demo:

```
$ chmod +x run.sh
$ ./run.sh
```

Get IP and ports for `Spring Boot App` and `Grafana`


| Service | URL |
|------|------|
| Spring Boot | 192.168.64.2:8080 |
| Grafana | 192.168.64.2:5566 |

![Kubernetes Services](img/svc.png)

Go to the browser for testing:

For `/success` endpoint:

![Success endpoint](img/success.png)

For `/fail` endpoint:

![Failed endpoint](img/fail.png)
<br /><br />

### Testing Grafana: <br /><br />

![](img/grafana1.png) <br /> <br />
![](img/grafana2.png) <br /> <br />
![](img/grafana3.png) <br /> <br />
![](img/grafana4.png) <br /> <br />
![](img/grafana5.png) <br /> <br />
![](img/grafana6.png) <br /> <br />
![](img/grafana7.png) <br /> <br />
![](img/grafana8.png) <br /> <br />
![](img/grafana9.png)

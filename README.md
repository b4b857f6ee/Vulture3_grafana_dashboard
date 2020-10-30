# Vulture3 grafana dashboard

## version 1

## Vulture Project : https://www.vultureproject.org/  You Need this for sure :) for the Version 3

## Getting status of FreeBSD services for Vulture3 using Telegraf+InfluxDB+Grafana

![Alt text](https://github.com/b4b857f6ee/Vulture3_grafana_dashboard/blob/main/services_grafana.png?raw=true "Vulture - NOC - Services")
![Alt text](https://github.com/b4b857f6ee/Vulture3_grafana_dashboard/blob/main/services_grafana1.png?raw=true "Vulture - NOC - Services")

You can use the little dashboard below the "UP" to configure alert.

Main goal of this easy script is checking list of given FreeBSD services and sending their status 
including Up/Down time in to InfluxDB and Grafana dashboards.
  
The script is written on python and I tried to use standard lib's as much as possible,
but you still need a pip install.

  This script returns a Json format with services status coded by digits: 
```
  active (running) = 1
  inactive (dead) = 0
```  

so you need to convert it back to string in Grafana. 
  
  Actually the last Telegraf version accepts the string values in json format, 
  but if you want to use Grafana alerting you still need numeric format to put it on alert graphs. 
  
  Also script provide a service name and time recent service status in seconds, 
  so you can use it in Grafana dashboards.
  
  You can find the Grafana dashboard example in the json file or on grafana.com:https://grafana.com/grafana/dashboards/13310

Telegraf configuration: 

```
    [[inputs.exec]]

    commands = [
     "/opt/srvstatus/venv/bin/python /opt/srvstatus/service.py"
    ]

    timeout = "5s"
    name_override = "services_stats"
    data_format = "json"
    tag_keys = [
      "service"
    ]
```

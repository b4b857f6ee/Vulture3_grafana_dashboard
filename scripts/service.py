#! /usr/local/bin/python3.7

import os
import re
import json
import subprocess
import configparser
import parsedatetime
from datetime import datetime
import time
import psutil

infos = {}

def JsonLoad(json_data_file) :
    with open(json_data_file) as f :
        return json.load(f)

items = JsonLoad('/opt/srvstatus/settings.json')

# Default return
for app, users in items.items():
    for user in users:
        service = '{}-{}'.format(user,app)
        infos[service] = {
            "service" : service,
            "status": 1
        }

for i in psutil.process_iter():
    service = '{}-{}'.format(i.username(),i.name())
    if service in infos.keys():
        infos[service]["status"] = 4
        infos[service]["status_time"] = int(i.create_time())

print(json.dumps([x for x in infos.values()]))
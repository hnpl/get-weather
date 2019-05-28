#!/usr/bin/python3

import requests
import csv
import os
import sys
import datetime


# Workflow
# Check if .requesttrack exists, if not, create one
# Check if .temperature exists
#   if not, create one

relative_path = os.path.dirname(__file__)
track_file_path = os.path.join(relative_path, 'requesttrack')
temperature_file_path = os.path.join(relative_path, 'temperature')

num_requested = 0
if not os.path.isfile(track_file_path):
    with open(track_file_path, 'w') as f:
        f.write('0')
else:
    with open(track_file_path, 'r') as f:
        lines = f.readlines()
        num_requested = int(lines[0])


update_temperature = True
temperature = 'error'
now = datetime.datetime.now()
#if not os.path.isfile(temperature_file_path):
#    update_temperature = True
#else:
    # read datetime from the file
#    with open(temperature_file_path,'r') as f:
#        lines = f.readlines()
#    past = datetime.datetime.strptime(lines[0].strip(), "%Y %m %d %H %M %S")
#    dtime = now - past
#    if dtime.seconds > 600:
#        update_temperature = True 
#    else:
#        temperature = lines[1].strip()

if update_temperature:
    url = "https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=csv&hoursBeforeNow=24&mostRecent=true&stationString=KEDU"
    response = requests.get(url)

    for line in response.iter_lines():
        pass

    line = str(line, "ascii")
    line = line.split(',')
    if len(line) >= 6:
        temperature = line[5]
    if temperature == "":
        temperature = "---"
    else:
        temperature = "".join([temperature, chr(176), 'C'])

    with open(temperature_file_path, 'w') as f:
        f.write('%s\n%s' % (now.strftime("%Y %m %d %H %M %S"), temperature))

    with open(track_file_path, 'w') as f:
        f.write('%i' % (num_requested + 1))

#print(''.join([temperature, chr(176), 'C']))

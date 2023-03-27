import os
import sys
import requests
import uuid
from datetime import datetime

#vars
target_api_url = "http://something.com"
num_cycles = 10
delay_secs = 2


def read_file():
    with open(os.path.join(sys.path[0],"jsonsamples.txt"), "rb") as f:
        json = f.read()
    return str(json)

def replace_values(json):
    i = json.find("GUID")
    while i > -1:
        json = json.replace("GUID",str(uuid.uuid4()),1)   # only replaces 1 each pass, will loop until all are done
        i = json.find("GUID")

    now = datetime.now()
    nowstr = now.strftime("%Y-%m-%d %H:%M:%S")  
    json = json.replace("TIMESTAMP_1", nowstr)        # replaces all timestamps
    return json

def post_api(url, msg):
    x = requests.post(url, json = msg)
    return x


json = read_file()
json_new = replace_values(json)
rtn = post_api(url, json_new)
print("1")

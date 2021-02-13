#Python3
#Author Aidan Mellin

import requests
import pprint
import math

ID = "0xA34eB873b4ffB1142948e34Dd50EE232EA15C5d3"

def request(ID):
    req = requests.get("https://eth.2miners.com/api/accounts/"+ID)
    rJson = req.json()
    req_overall(rJson)
    dec_bal = 9
    print(avg_hash(rJson['hashrate']))
    print(get_balance(rJson['stats'].get('balance'),dec_bal))
    print(get_workers(rJson["workers"]))     

def req_overall(rJson):
    print(rJson.keys())

def get_workers(workers):
    ret_str = "Workers:\n"
    for i in workers.keys():
        ret_str+="\t"+i+":\tOffline = **"+str(workers[i]['offline'])+"**"
    return ret_str

def avg_hash(hr):
    ret_hr = hr * (math.pow(10,-6))
    return ret_hr

def get_balance(bal,dec):
    #Length of returned string can be any size. However, it only counts up to 9 decimal places. 
    return bal*math.pow(10,-dec )

def minerChart(rJson):
    minerCharts = rJson["minerCharts"]
    for i in range(len(minerCharts)):
        if not (minerCharts[i]["workerOnline"] == 0):
            pprint.pprint(minerCharts[i])
request(ID)

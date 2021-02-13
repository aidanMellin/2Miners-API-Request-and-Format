#Python3
#Author Aidan Mellin

import requests
import pprint
import math

ID = "0xA34eB873b4ffB1142948e34Dd50EE232EA15C5d3"

def request(ID,call):
    req = requests.get("https://eth.2miners.com/api/accounts/"+ID)
    rJson = req.json()
    #req_overall(rJson)
    dec_bal = 9
    #print(avg_hash(rJson['hashrate']))
    #print(get_balance(rJson['stats'].get('balance'),dec_bal))
    #print(get_workers(rJson["workers"]))
    
    called = {
        'h': avg_hash(rJson['hashrate']), #Get hashrate
        'b': get_balance(rJson['stats'].get('balance'),dec_bal), #Get balance
        'w': get_workers(rJson["workers"]),
        'a': get_all(rJson['hashrate'],rJson['stats'].get('balance'),dec_bal,rJson["workers"])    
    }
    print("\n")
    print(get_all(rJson['hashrate'],rJson['stats'].get('balance'),dec_bal,rJson["workers"]))
    
def get_spaces(tmp):
    return " " * (len(ID) - len(tmp))

def get_all(hr, bal, dec, wkrs):   
    spacer = ret_str = "| "+ "-"*len(ID) +" |\n"
    ret_str = spacer
    
    calls = [
        ID,
        "Current Balance: "+ str(get_balance(bal,dec)),
        "Avg Hash: "+str(avg_hash(hr)),
    ]
    workers = get_workers(wkrs)
    
    # for i in calls:
    #     ret_str += "| "+i+get_spaces(i)+" |\n"+spacer
        
    ret_str += "".join(["| "+i+get_spaces(i)+" |\n"+spacer for i in calls])
    ret_str += "| Workers:" + get_spaces("Workers:")+" |\n" + "".join(["|      "+i+get_spaces("     "+i)+" |\n"+spacer for i in workers])
    
    return ret_str
         

def req_overall(rJson):
    print(rJson.keys())

def get_workers(workers):
    ret = []
    for i in workers.keys():
        ret.append(i+": Offline = "+str(workers[i]['offline']))
    return ret

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
request(ID,"a")

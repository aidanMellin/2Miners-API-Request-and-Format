#Python3
#Author Aidan Mellin

import requests
import pprint

ID = "0xA34eB873b4ffB1142948e34Dd50EE232EA15C5d3"
#ID = "0xbe693de86f1dc0abfe9856eee60ca54e0496a1f6" #Big Miner other guy

def request(ID):
    req = requests.get("https://eth.2miners.com/api/accounts/"+ID)
    rJson = req.json()
    #req_overall(rJson)
    #minerChart(rJson)
    
    print(rJson["stats"],"\n")
    print(avg_hash(rJson['hashrate']))
    print(get_balance(rJson['stats'].get('balance')))
     
    #print(rJson["payments"],"\n")
    #print(rJson["sumrewards"],"\n")

def req_overall(rJson):
    print(rJson.keys())

def avg_hash(hr):
    ret_str = "{}.{}".format(str(hr)[0:2],str(hr)[2::])
    return ret_str

def get_balance(bal):
    #Length of returned string can be any size. However, it only counts up to 9 decimal places. 
    dec_bal = 9
    bal_str = str(bal) #Str'd int that is balance
    dec_diff = len(bal_str) - dec_bal
    if(len(bal_str) >= dec_bal): #Balance is >= 1
        ret_str = "{}.{}".format(bal_str[0:dec_diff],bal_str[dec_diff::])
    else:
        zeros = ""
        for i in range(abs(dec_diff)):
            zeros+="0"
        ret_str = ".{}{}".format(zeros,bal_str)
        
    return ret_str

def minerChart(rJson):
    minerCharts = rJson["minerCharts"]
    for i in range(len(minerCharts)):
        if not (minerCharts[i]["workerOnline"] == 0):
            pprint.pprint(minerCharts[i])
request(ID)

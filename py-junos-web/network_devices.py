
nodes_info = ['10.40.23.52 SRXFW1','2.2.2.2 SRXFW2','3.3.3.3 SRXFW3']


def list_switches():

    j=len(nodes_info)
    tmpRet = []
    for l in range (0,j):
        ###### split the lines via /n #####
        dev = str(nodes_info[l]).split(' ')
        tmpRet.append({"name":dev[1],"ip":dev[0]})

    return tmpRet

def getNameSW(ip):
    db = list_switches()
    for i in db:
        if ip == i["ip"]:
            print i["name"]
            return i["name"]
        else:
            print i["ip"]
            return i["ip"]

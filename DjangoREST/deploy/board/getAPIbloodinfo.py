import os
import requests
import json
import pandas as pd


def path():
    return os.path.dirname(os.path.abspath(__file__))


def csvFile():
    return os.path.join(path(), "TempCSV/getAPIbloodinfo.csv")


def set_ReqURL(ReqNum):
    return 'http://localhost:8000/api/bloodinfo/' + ReqNum + "/"


"""
def getAPIinfo(ReqNum):
    res = requests.get(set_ReqURL(str(ReqNum)))
    info = json.loads(res.text)

    return info


def makeCSVFile(ReqNum):
    #infos = [getAPIinfo(ReqNum-1), getAPIinfo(ReqNum), getAPIinfo(ReqNum+1)]
    infos = [getAPIinfo(ReqNum)]

    df = pd.json_normalize(infos)
    df.to_csv(csvFile(), header=False)
"""


def getAPIinfo(ReqNum):
    res = requests.get(set_ReqURL(ReqNum))
    info = json.loads(res.text)
    df = pd.json_normalize(info)

    df.to_csv(csvFile(), header=False)


def displayCSVFile():
    with open(csvFile()) as openFile:
        print(openFile.readline(), end="")


# Test
if __name__ == '__main__':
    # line = input("bloodinfo에 접근할 번호 입력: ")

    # getAPIinfo(line)

    displayCSVFile()

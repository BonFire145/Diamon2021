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


def getAPIinfo(ReqURL):
    res = requests.get(ReqURL)
    info = json.loads(res.text)
    df = pd.json_normalize(info)
    df.to_csv(csvFile(), header=False)


def displayCSVFile():
    with open(csvFile()) as openFile:
        print(openFile.readline(), end="")


# Test
if __name__ == '__main__':
    line = input("bloodinfo에 접근할 번호 입력: ")

    getAPIinfo(
        set_ReqURL(line)
    )

    displayCSVFile()

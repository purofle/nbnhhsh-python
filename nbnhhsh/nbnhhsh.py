import requests
import json
import sys

def suo(text:str):
    r = requests.post('https://lab.magiconch.com/api/nbnhhsh/guess',data={'text':str(text)})
    tran = ""
    try:
        trans = json.loads(r.text)[0]['trans']
    except KeyError as e:
        print('可能暂时没有这个缩写！')
        print(e)
    for i in trans:
        if len(trans) == 1:
            return i
            break
        else:
            tran += i+"，"

    return tran[:-1]

if __name__=="__main__":
    assets=[{"ip":"1.1.1.1","port":443},{"ip":"2.2.2.2","port":80}]
    #端口从小到大排序
    res=sorted(assets,key=lambda x:x["port"])

    #端口从大到小
    res = sorted(assets, key=lambda x:x["port"], reverse=True)
    # [{'ip': '1.1.1.1', 'port': 443}, {'ip': '2.2.2.2', 'port': 80}]


    #先按port，port相同再按ip：
    res=sorted(assets,key=lambda x: (x["port"],x["ip"]))
    print(res)
if __name__=="__main__":
    assets=[{"ip":"1.1.1.1"},{"ip":"2.2.2.2"}]
    #start=1 ,序号从1开始  
    #enumerate(可迭代对象, start=起始数字)
    for idx,item in enumerate(assets,start=1):
        print(idx,item["ip"])
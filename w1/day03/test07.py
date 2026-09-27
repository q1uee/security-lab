if __name__=="__main__":
    asserts=[{"ip":"1.1.1.1","status":"open"},{"ip":"2.2.2.2","status":"closed"}]
    #filter:保留满足条件的数据
    open_assert=filter(lambda x:x["status"]=="open",asserts)
    print(list(open_assert))

    #map:对没交数据做转换，提取ip
    ip_list=map(lambda x:x["ip"],asserts)
    print(list(ip_list))


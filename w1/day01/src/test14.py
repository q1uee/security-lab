#字典推导
if __name__=="__main__":
    #普通循环
    data={}
    for i in range(1,6):
        data[i]=i*i
    print("普通字典循环：",data)

    #字典推导式
    data2={i:i*i for i in range(1,6)}
    print("字典推导式:",data2)

    #例子：过滤字典，只保留value大于10的键值对
    origin={"a":5,"b":12,"c":20,"d":3}
    filter_dict={k:v for k,v in origin.items() if v>10}
    print("过滤后的字典:",filter_dict)

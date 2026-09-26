#13 列表推导式，安全工具高频
if __name__=="__main__":
    #普通循环写法
    nums=[]
    for i in range(1,11):
        if i%2==0:
            nums.append(i)
    print("普通循环结果:",nums)

    #等价列表推导式
    nums2=[i for i in range(1,11) if i%2==0]
    print("列表推导式结果；",nums2)

    #例子：批量生成url路径,渗透经常用
    paths=[f"/api/{x}" for x in ["user","info","login"]]
    print("批量路径:",paths)
          

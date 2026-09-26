#15 文件读写 with自动关闭(推荐)
if __name__=="__main__":
    #写入
    with open("test.txt","w",encoding="utf-8") as f:
        f.write("第一行\n第二行")
    
    #读取
    with open("test.txt","r",encoding="utf-8") as f:
        content= f.read()
        #content=f.readlines()
        #content=f.readline()
    print("读取：",content)
#19 文件按行读取(读取日志、爆破结果)
if __name__=="__main__":
    with open("test.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    print("所有行：")
    for line in lines:
        #strip去掉换行和收尾空格
        line=line.strip()
        if line:
            print(line)

#17 导入内置模块
import random
import time

if __name__=="__main__":
    print("随机0~1小数：",random.random())
    print("随机1~10整数:",random.randint(1,10))

    print("当前时间戳：",time.time())
    print("本地时间：",time.ctime(time.time()))

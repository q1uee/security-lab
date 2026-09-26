#02 条件判断：输入分数，判断等级
if __name__=="__main__":
    score=float(input("please input your score:"))
    if(score>=90):
        print("优秀")
    elif score>=60:
        print("及格")
    else:
        print("不及格")
        
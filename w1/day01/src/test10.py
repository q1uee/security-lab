#10 综合练习：计算圆形/正方形面积
import math
def circle_area(r):
    return math.pi*r*r

def square_area(a):
    return a*a
if __name__=="__main__":
    choice=input("选择：1圆形 2正方形：")
    if choice=="1":
        r=float(input("输入半径："))
        print("圆的面积：",circle_area(r))
    elif choice=="2":
        a=float(input("输入边长："))
        print("正方形面积:",square_area(a))
    else:
        print("error1")
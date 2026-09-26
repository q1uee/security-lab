#08 判断一个数是不是质数
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n% i==0:
            return False
    return True
if __name__=="__main__":
    num=int(input("please input num:"))
    if(is_prime(num)):
        print("yes")
    else:
        print("no")
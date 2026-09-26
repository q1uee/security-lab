#16 异常捕获，写工具必备，防止程序直接崩溃
if __name__=="__main__":
    try:
        num=int(input("input num:"))
        print("数字乘2=",num*2)
    except ValueError:
        print("你输入的不是数字")
    except Exception as e:
        print("未知错误:",e)

#11 字符串基础操作:分隔、替换、切片、判断
if __name__=="__main__":
    text="Hello Python Security"
    print("原串:",text)
    print("大写:",text.upper())
    print("小写:",text.lower())
    print("按空格分隔成列表:",text.split(" "))
    print("切片去前五个字符:",text[:5])
    print("是否为He开头:",text.startswith("He"))
    print("替换:",text.replace("Python","git"))
    
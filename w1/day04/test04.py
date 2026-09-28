import re
if __name__=="__main__":
    #扫描整个字符串，找到第一个匹配就返回 Match 对象
    m=re.search(r"\d+","abc123def456")
    print(m.group())
import re
if __name__=="__main__":
    #多次使用同一个正则，先编译，提高性能
    pat=re.compile(r"\d+")
    s1=pat.findall("test123")
    s2=pat.search("abc456")
    print(s1)
    print(s2)
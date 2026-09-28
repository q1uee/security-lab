import re
if __name__=="__main__":
    s="<a>hello</a><b>world</b>"

    #贪婪 .*匹配到最后一个
    a=re.findall(r"<.*>",s)
    print(a)
    #非贪婪 .*?遇到第一个就停止
    a=re.findall(r"<.*?>",s)
    print(a)
#18 综合：列表推导式+字符串处理
#过滤，只保留长度大于4的字符串
if __name__=="__main__":
    word_list=["hi","python","web","burp","git","src"]
    res=[word.upper() for word in word_list if len(word)>4]
    print(res)
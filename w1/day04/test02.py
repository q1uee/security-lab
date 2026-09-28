import re
if __name__=="__main__":
    text="price:100,price:200"
    res=re.findall(r"price:(\d+)",text)
    res=re.findall(r"price:\d+",text)
    res=re.findall(r"price:(:?\d+)",text)
    print(res)
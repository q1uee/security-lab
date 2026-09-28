import re
if __name__=="__main__":
    s1=re.match(r"\d+","123abc")
    s2=re.match(r"\d+","abc123")
    print(s1)
    print(s2)
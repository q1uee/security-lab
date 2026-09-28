import re
from pathlib import Path
import argparse

# 参考
# ip_pat = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
# url_pat = re.compile(r"https?://[^\s]+", re.IGNORECASE)
# email_pat = re.compile(r"\b[A-Za-z0-9_\-.]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+\b")


BASE_DIR=Path(__file__).parent.resolve()

def is_exist(file_name:str):
    p=BASE_DIR/file_name
    return p.exists() and p.is_file()

def extract(file_name:str):
    p=BASE_DIR/file_name
    with open(p,"r",encoding="utf-8") as f:
        s=f.read()
        # print(s)

        ip=re.findall(r"\d+\.\d+\.\d+\.\d+",s)
        url=re.findall(r"(?:http|https):[.\w?&/=]*",s)
        email=re.findall(r"\w*@[\w-]+\.\w+",s)



        print(ip)
        print(url)
        print(email)
        #不会出现排序
        unique_ip=list(dict.fromkeys(ip))
        unique_url=list(dict.fromkeys(url))
        unique_email=list(dict.fromkeys(email))
        print("IP:")
        for ip in unique_ip:
            print(ip)
        print("邮箱:")
        for email in unique_email:
            print(email)
        print("url:")
        for url in unique_url:
            print(url)
        #会重新排序
        # unique_ip=list(set(ip))
        # unique_email=list(set(email))
        # unique_url=list(set(url))
        


def extract_to_file(file_name:str,result_name:str):
    p=BASE_DIR/file_name
    with open(p,"r",encoding="utf-8") as f:
        s=f.read()
        # print(s)
        ip=re.findall(r"\d+\.\d+\.\d+\.\d+",s)
        url=re.findall(r"(?:http|https):[.\w?&/=]*",s)
        email=re.findall(r"\w*@[\w-]+\.\w+",s)
        # print(ip)
        # print(url)
        # print(email)
        #不会出现排序
        unique_ip=list(dict.fromkeys(ip))
        unique_url=list(dict.fromkeys(url))
        unique_email=list(dict.fromkeys(email))
    p1=BASE_DIR/result_name
    with open(p1,"a",encoding="utf-8") as f:
        f.write("IP:\n")
        for ip in unique_ip:
            f.write(ip)
            f.write("\n")
        f.write("邮箱:\n")
        for email in unique_email:
            f.write(email)
            f.write("\n")
        f.write("url:\n")
        for url in unique_url:
            f.write(url)
            f.write("\n")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="混杂文本提取器（IP / URL / 邮箱）")
    parser.add_argument("file_name",help="文件名字")
    parser.add_argument("--out",help="可选，输入到文本")

    args=parser.parse_args()

    try:
        if is_exist(args.file_name):
            try:
                if args.out:
                    extract_to_file(args.file_name,args.out)
                else:
                    extract(args.file_name)
            except Exception as a:
                print(a)
        else:
            print("文件不存在")
    except Exception as a:
        print(a)

import re
from pathlib import Path
import argparse

BASE_DIR=Path(__file__).parent.resolve()

class Extract:

    def __init__(self):
        parser=argparse.ArgumentParser(description="混杂文本提取器（IP / URL / 邮箱）")
        parser.add_argument("file_name",help="文件名字")
        parser.add_argument("--out",help="可选，输入到文本")

        args=parser.parse_args()

        self.a=args

        try:
            if self.is_exist(args.file_name):
                try:
                    if args.out:
                        self.extract_to_file(args.file_name,args.out)
                    else:
                        self.extract(args.file_name)
                except Exception as a:
                    print(a)
            else:
                print("文件不存在")
        except Exception as a:
            print(a)


    def is_exist(self,file_name):
        p=BASE_DIR/file_name
        return p.exists() and p.is_file()


    def extract_to_file(self,file_name,result_name):
        p=BASE_DIR/file_name
        with open(p,"r",encoding="utf-8") as f:
            s=f.read()

            ip=re.findall(r"\d+\.\d+\.\d+\.\d+",s)
            url=re.findall(r"(?:http|https):[.\w?&/=]*",s)
            email=re.findall(r"\w*@[\w-]+\.\w+",s)

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


    def extract(self,file_name):
        p=BASE_DIR/file_name
        with open(p,"r",encoding="utf-8") as f:
            s=f.read()

            ip=re.findall(r"\d+\.\d+\.\d+\.\d+",s)
            url=re.findall(r"(?:http|https):[.\w?&/=]*",s)
            email=re.findall(r"\w*@[\w-]+\.\w+",s)

            print(ip)
            print(url)
            print(email)
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

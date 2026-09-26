import os
from pathlib import Path

def is_file_exist(file_name):
    p=Path(file_name)
    return p.exists() and p.is_file()

if __name__=="__main__":
    while True:
        file_path=os.path.abspath(__file__)
        print(f"{file_path}>>>",end="")
        log_file=input()
        paths=log_file.split(" ")
        print(os.getcwd())
        # print(paths)
        if paths[0]=="python" and paths[1]=="log_parser.py":

            if paths[2]=="-h":
                try:
                    with open("D:\\security-lab\\w1\\day02\\log_parser\\help.txt","r",encoding="utf-8")as f:
                        lines=f.readlines()
                        for line in lines:
                            print(line)  
                except Exception as a:
                    print(a)
            else:
                is_exist=is_file_exist(log_file)
                if(is_exist):
                    print("yes")
                else:
                    print("文件路径错误或者改路径下的不是文件类型")
        else:
            print("命令错误")

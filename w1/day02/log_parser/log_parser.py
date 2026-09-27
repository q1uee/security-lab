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
        #print(os.getcwd())
        #print(f"paths={paths}")
        if paths[0]=="python" and paths[1]=="log_parser.py":

            if paths[2]=="-h":
                try:
                    with open("D:\\security-lab\\w1\\day02\\log_parser\\help.txt","r",encoding="utf-8")as f:
                        lines=f.readlines()
                        for line in lines:
                            line=line.strip()
                            if line:
                                print(line)  
                except Exception as a:
                    print(a)
            else:
                is_exist=is_file_exist(paths[2])

                #print(f"paths[2]={paths[2]}")                
                if(is_exist):
                    if paths[3]=="--top" and int(paths[4])>0:
                        num=int(paths[4])
                        with open(f"{paths[2]}","r",encoding="utf-8") as f:
                            lines=f.readlines()
                            #print(lines)
                            for line in lines:
                                if(num>0):
                                    line=line.strip()
                                    if line:
                                        print(line)
                                        num-=1
                    else:
                        print("格式错误")
                                
                else:
                    print("文件路径错误或者改路径下的不是文件类型")
        else:
            print("命令错误")

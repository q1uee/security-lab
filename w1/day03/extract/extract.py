from pathlib import Path
import argparse
import json

BASE_DIR = Path(__file__).parent.resolve()

def is_exist(file_name:str):
    p=BASE_DIR/file_name
    return p.exists() and p.is_file()

#*args不定参数
def field(file_name:str,*args):
    p=BASE_DIR/file_name
    with open(p,"r",encoding="utf-8") as f:
        data_dir=json.load(f)
    arg_list=list(args)
    print(list(args))
    print("==================================================")
    i=1
    for data in data_dir["data"]["request_list"]:
        print(i,end="")
        for arg in arg_list:
            print(f"|{data[arg]}",end="")
        i+=1
        print("")
    print("==================================================")

        



if __name__=="__main__":
    parse=argparse.ArgumentParser(description="json串的过滤")
    parse.add_argument("file_name",help="json串所在文件位置")
    #nargs传不定参数
    parse.add_argument("--fields",help="过滤下来的关键字",nargs="+")

    args=parse.parse_args()
    try:
        if is_exist(args.file_name):
            try:
                #不定参数同过*args.fields传输
                field(args.file_name,*args.fields)
            except Exception as a:
                print(a)
        else:
            print("文件不存在")
    except Exception as a:
        print(a)



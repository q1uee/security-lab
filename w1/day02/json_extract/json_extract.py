from pathlib import Path
import argparse
import json

BASE_DIR = Path(__file__).parent.resolve()

def is_file_exist(file_name:str) -> bool:
    p=BASE_DIR/file_name
    return p.exists() and p.is_file()

def print_result(file_name:str,key:str):
    file_path=BASE_DIR/file_name
    data_list=[]
    with open(file_path,"r",encoding="utf-8") as f:
        data=json.load(f)
        for item in data:
           val= item.get(key)
           print(f"{key}:{val}")
      

def save_result(file_name:str,key:str,save_file:str):
    file_path=BASE_DIR/file_name
    file_save_path=BASE_DIR/save_file
    s=open(file_save_path,"a",encoding="utf-8")
    with open(file_path,"r",encoding="utf-8") as f:
        data=json.load(f)
        for item in data:
            val= item.get(key)
            s.write(f"{key}:{val}\n")
    s.close()


if __name__=="__main__":
    parser=argparse.ArgumentParser(description="json 解析小工具")
    parser.add_argument("jsonfile",help="待读取的json文件名（放在脚本同目录）")
    parser.add_argument("--key",help="查找的key值")
    parser.add_argument("--output",help="输出内容存放的文件")
    args=parser.parse_args()

    if not is_file_exist(args.jsonfile):
        print("文件路径错误或者该路径下的不是文件类型")
    else:
        if args.key is None:
            print("缺少参数key")
        else:
            if args.output is None:
                print_result(args.jsonfile,args.key)
            else:
                save_result(args.jsonfile,args.key,args.output)

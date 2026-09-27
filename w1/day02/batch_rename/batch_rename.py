from pathlib import Path
import argparse

BASE_DIR=Path(__file__).parent.resolve()

def is_dir(dir_name:str):
     p=BASE_DIR/dir_name
     return p.is_dir() and p.exists()

def add_prefix(dir_name:str,prefix:str):
    p=BASE_DIR/dir_name
    newpath=p
    for item in p.iterdir():
        name=item.name
        item.rename(f"{p}/{prefix}{name}")

#后缀为(如.txt的文件)添加前缀
def suffix_add_prefix(dir_name:str,suffix:str,prefix:str):
    p=BASE_DIR/dir_name
    for item in p.iterdir():
        if item.suffix.lower()==suffix.lower():
            name=item.name
            item.rename(f"{p}/{prefix}{name}")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description="batch_rename")
    parser.add_argument("dir_name",help="在哪个目录下操作")
    parser.add_argument("--suffix",help="后缀为XX的文件")
    parser.add_argument("--add-prefix",help="添加前缀XX")

    args=parser.parse_args()

    if is_dir(args.dir_name):
         if args.suffix:
            suffix_add_prefix(args.dir_name,args.suffix,args.add_prefix)
         else:
            add_prefix(args.dir_name,args.add_prefix)#注意add_prefix的写法
    else:
         print("路径错误或者并非文件夹")
              


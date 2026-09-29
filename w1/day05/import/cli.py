import argparse
import core

def args():
    parser=argparse.ArgumentParser(description="混杂文本提取器（IP / URL / 邮箱）")
    parser.add_argument("file_name",help="文件名字")
    parser.add_argument("--out",help="可选，输入到文本")

    args=parser.parse_args()

    try:
        if core.is_exist(args.file_name):
            try:
                if args.out:
                    core.extract_to_file(args.file_name,args.out)
                else:
                    core.extract(args.file_name)
            except Exception as a:
                print(a)
        else:
            print("文件不存在")
    except Exception as a:
        print(a)
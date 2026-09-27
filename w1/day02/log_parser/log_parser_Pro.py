from pathlib import Path
import argparse

# 脚本所在目录基准路径
BASE_DIR = Path(__file__).parent.resolve()

def is_file_exist(file_name: str) -> bool:
    """判断文件是否存在且是普通文件，基于脚本目录查找"""
    p = BASE_DIR / file_name
    return p.exists() and p.is_file()

def read_top_lines(filename: str, top_num: int):
    """读取文件前N行，空行跳过"""
    file_path = BASE_DIR / filename
    with open(file_path, "r", encoding="utf-8") as f:
        count = 0
        for line in f:
            if count >= top_num:
                break
            stripped_line = line.strip()
            if stripped_line:
                print(stripped_line)
                count += 1

if __name__ == "__main__":
    # 构建参数解析器
    parser = argparse.ArgumentParser(description="日志解析小工具：读取日志文件的前N行")
    # 位置参数：日志文件名
    parser.add_argument("logfile", help="待读取的日志文件名（放在脚本同目录）")
    # 可选参数 --top，必须传正整数
    parser.add_argument("--top", type=int, help="读取文件的前N行，N必须大于0")

    args = parser.parse_args()

    # 校验文件
    if not is_file_exist(args.logfile):
        print("文件路径错误或者该路径下的不是文件类型")
    else:
        if args.top is not None:
            if args.top <= 0:
                print("错误：--top 后面必须填写正整数")
            else:
                read_top_lines(args.logfile, args.top)
        else:
            # 不加--top，输出全部内容
            file_path = BASE_DIR / args.logfile
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        print(line)

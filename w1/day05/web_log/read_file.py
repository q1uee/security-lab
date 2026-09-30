import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()


class Read_file:
    def __init__(self):
        parser = argparse.ArgumentParser(description="扫描可疑的web访问记录")
        parser.add_argument("file_name", help="扫描文件")
        self.args = parser.parse_args()
        try:
            if self.is_exist():
                p = BASE_DIR / self.args.file_name
                self.f=open(p, "r", encoding="utf-8")
            else:
                print("文件有误")
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as a:
            print(a)


    def close_f(self):
        self.f.close()

    def is_exist(self):
        p = BASE_DIR / self.args.file_name
        return p.exists() and p.is_file()

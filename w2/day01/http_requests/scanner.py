import argparse
import json
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent.resolve()


def args():
    parse = argparse.ArgumentParser(description="扫描HTTP请求")
    parse.add_argument("--url_file", help="url文件")
    parse.add_argument("--out", help="写入文件")
    parse.add_argument("--timeout", help="超时时间")
    args = parse.parse_args()
    return args


def is_exist(file_name):
    p = BASE_DIR / file_name
    return p.exists() and p.is_file()


def read_file(file_name):
    p = BASE_DIR / file_name
    try:
        if is_exist(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    yield line
        else:
            print("文件不存在或者路径有问题")
    except FileExistsError as e:
        print(e)


def Get_request(url, timeout, f):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    session = requests.Session()
    try:
        resp = session.get(url=url, headers=headers, timeout=timeout)
        # resp.raise_for_status()
        # data=resp.json()
        # 保留状态码，不主动抛异常
        # status_code = resp.status_code

        # 判断响应头，只有是json类型才尝试解析
        content_type = resp.headers.get("Content-Type", "")
        data = None
        if "application/json" in content_type:
            try:
                data = resp.json()
            except json.JSONDecodeError:
                data = None

        # p=BASE_DIR/out_file_name
        # with open(p,"a",encoding="utf-8")as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        # json.dump("\n",f,indent=2,ensure_ascii=False)
    except requests.exceptions.RequestException as a:
        print(a)


def requests_http(gen, out, timeout=3):
    p = BASE_DIR / out
    with open(p, "a", encoding="utf-8") as f:
        for line in gen:
            print(line)
            Get_request(line, timeout, f)
            f.write("\n")


if __name__ == "__main__":
    args = args()
    gen = read_file(args.url_file)
    if not args.timeout:
        requests_http(gen, args.out)
    else:
        requests_http(gen, args.out, timeout=int(args.timeout))

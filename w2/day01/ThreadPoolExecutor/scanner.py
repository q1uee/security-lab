import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent.resolve()


def args():
    parse = argparse.ArgumentParser(description="扫描HTTP请求")
    parse.add_argument("--url_file", help="url文件")
    parse.add_argument("--out", help="写入文件")
    parse.add_argument("--timeout", help="超时时间")
    parse.add_argument("--workers", help="线程数")
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
        content_type = resp.headers.get("Content-Type", "")
        data = None
        if "application/json" in content_type:
            try:
                data = resp.json()
            except json.JSONDecodeError:
                data = None
        json.dump(data, f, indent=2, ensure_ascii=False)
    except requests.exceptions.RequestException as a:
        print(a)


def requests_http(gen, out, timeout=3, max_workers=3):
    p = BASE_DIR / out
    futures = []
    # # 创建线程池，max_workers 最大并发线程数量
    # 不要嵌套 with，把多个上下文管理器写在同一个 with 里，用逗号隔开
    with ThreadPoolExecutor(max_workers=max_workers) as executor,open(p, "a", encoding="utf-8") as f:
            for line in gen:
                line = line.strip()
                if not line:
                    continue
                print(line)
                # submit：提交任务到线程池，不会立刻执行，由线程池调度
                # 参数：函数名，后面依次是传给Get_request的参数
                fut = executor.submit(Get_request, line, timeout, f)
                futures.append(fut)
                # as_completed：迭代已经完成的任务，哪个线程先跑完，就先拿到结果
                # 持续监听 futures 里所有任务，任意一个任务完成，立刻返回该 future
                for future in as_completed(futures):
                    try:
                        # result() 获取函数返回值；如果函数内部抛出异常，这里会重新抛出
                        future.result()
                    except Exception as e:# noqa: BLE001   忽略ruff check --fix警告
                        print(f"线程任务出错:{e}")
                f.write("\n")


if __name__ == "__main__":
    args = args()
    gen = read_file(args.url_file)
    if not args.timeout:
        requests_http(gen, args.out)
    else:
        requests_http(
            gen, args.out, timeout=int(args.timeout), max_workers=int(args.workers)
        )

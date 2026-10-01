import json

import requests


def fetch_github_user(username: str):
    url = f"https://api.github.com/users/{username}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # proxies={
    #     "http": "http://127.0.0.1:8080",
    #     "https": "http://127.0.0.1:8080"
    # }

    session = requests.Session()
    try:
        resp = session.get(
            url,
            headers=headers,
            # proxies=proxies,
            timeout=10,
            # verify=False
        )
        resp.raise_for_status()
        data = resp.json()
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("保存成功")
        return data
    except requests.exceptions.RequestException as e:
        print(e)
    return None


def httpbin():
    session = requests.Session()
    # proxies={"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}
    try:
        r = session.get(
            "https://httpbin.org/get",
            params={"id": 100, "name": "demo"},
            headers={"User-Agent": "test"},
            # proxies=proxies,
            timeout=8,
            # verify=False
        )
        r.raise_for_status()
        res_data = r.json()
        with open("httpbin.json", "w", encoding="utf-8") as f:
            json.dump(res_data, f, indent=2, ensure_ascii=False)
    except requests.exceptions.RequestException as e:
        print(e)

def post_demo():
    url="https://httpbin.org/post"
    # proxies = {
    #     "http": "http://127.0.0.1:8080",
    #     "https": "http://127.0.0.1:8080",
    # }
    headers = {
        "User-Agent": "python-requests demo",
    }

    payload={
        "username": "test_user",
        "msg": "hello post",
        "num": 123
    }

    timeout=10

    session=requests.Session()
    session.headers.update(headers)
    try:
        resp=session.post(
            url,
            json=payload,
            # proxies=proxies,
            timeout=timeout
        )
        resp.raise_for_status()
        resp_data=resp.json()
        with open("post_result.json", "w", encoding="utf-8") as f:
            json.dump(resp_data, f, indent=2, ensure_ascii=False)
        print("✅ POST响应已保存至 post_result.json")

    except requests.exceptions.Timeout:
        print("❌ 请求超时")
    # except requests.exceptions.ConnectionError:
    #     print("❌ 连接失败，请检查Burp是否启动")
    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP状态异常：{err}")
    except json.JSONDecodeError:
        print("❌ 返回内容不是合法JSON")

if __name__ == "__main__":
    # fetch_github_user("octocat")
    # httpbin()
    post_demo()

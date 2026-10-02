import requests
# import socket,ssl

if __name__=="__main__":
    # 版本1：普通 requests get/post：一次性请求，不保存 Cookie，适合简单单发请求
    # import requests
    # proxies = {
    #     "http": "http://127.0.0.1:8080",
    #     "https": "http://127.0.0.1:8080"
    # }
    # resp = requests.get("https://httpbin.org/get", proxies=proxies, verify=False)
    # print(resp.text)

    
    # 版本2：requests.Session：会自动保存 Cookie，维持登录会话，多次请求共用同一个浏览器会话
    # import requests
    # proxies = {
    #     "http": "http://127.0.0.1:8080",
    #     "https": "http://127.0.0.1:8080"
    # }
    # session = requests.Session()
    # session.proxies = proxies # 所有session请求统一走burp

    # # 1.登录
    # session.post("https://httpbin.org/post", data={"user":"admin","pass":"123456"}, verify=False)
    # # 2.访问需要登录的接口，自动带上登录返回的Cookie
    # resp = session.get("https://httpbin.org/cookies", verify=False)
    # print(resp.text)

    # 版本3：原生 socket 版本：完全不用 requests 库，手动拼原始 HTTP 报文，底层裸写
    # import socket
    # s = socket.socket()
    # s.connect(("127.0.0.1",8080))
    # # 代理模式GET行必须写完整URL！
    # req = (
    #     b"GET https://httpbin.org/get HTTP/1.1\r\n"
    #     b"Host: httpbin.org\r\n"
    #     b"\r\n"
    # )
    # s.sendall(req)
    # raw = s.recv(4096)
    # print(raw.decode())
    # s.close()




    session=requests.Session()
    payload={
        "username": "test_user",
        "msg": "hello post",
        "num": 123
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp=session.post(
        url="https://httpbin.org/post",
        json=payload,
        proxies={"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"},
        headers=headers,
        timeout=5,
        verify=False
    )

    print(resp.text)
    
    
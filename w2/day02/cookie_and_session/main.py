import requests

if __name__=="__main__":
    session=requests.Session()

    login_url="https://httpbin.org/post"
    login_data={
        "username": "admin",
        "password": "123456"
    }
    resp_login=session.post(login_url,login_data)
    print("登录响应：",resp_login.json())
    # ✅ Session自动保存登录返回的Set-Cookie
    # 2. 使用同一个session访问需要登录的页面，自动携带Cookie
    resp_profile=session.get("https://httpbin.org/cookies")
    print("访问个人页，带会话Cookie：")
    print(resp_profile.json())
    # 可以手动查看当前session里面全部cookie
    print(session.cookies)
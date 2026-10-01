get / post
requests.get()：获取数据，参数拼在 URL 上（查询字符串）
requests.post()：提交数据，一般放请求体

params
params={} → 给 GET 用，自动拼接 URL 查询参数，不用自己拼?a=1&b=2
requests.get("https://httpbin.org/get", params={"name":"test", "page":1})

headers={} 请求头，模拟浏览器、带 token、UA

cookies={} 携带 Cookie 信息

timeout=5 超时，必须写！ 防止脚本卡死；单位秒，超过时间抛异常

session = requests.Session()
Session 会自动保存 cookie，多次请求之间维持会话（登录态）
推荐优先用 Session，而不是裸 requests.get/post

proxies 代理（对接 Burp Suite）
Burp 默认监听 127.0.0.1:8080
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}


r = session.get(url)
r.status_code   # 状态码 200/404/500
r.encoding      # 编码
r.text          # 文本字符串
r.json()        # 直接把返回的json字符串转成python字典（接口返回json才可以用）

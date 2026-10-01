# 批量HTTP资产探测工具
## 依赖安装
pip install requests

## 参数说明
--url_file   必选，存放待探测URL的文本文件路径，一行一个URL
--out        必选，输出结果json文件路径
--timeout    可选，单次请求超时时间，默认3秒
--workers     可选，并发线程数，默认3

## 使用示例
python scanner.py --url_file urls.txt --out result.json --timeout 5 --workers 5

## urls.txt格式要求
1. 每行一条URL，必须带http/https
2. 空行会自动跳过
3. 示例内容见下方

## 输出 result.json
字段：
url: 探测地址
status_code: HTTP状态码，探测失败为null
resp_time: 请求耗时(秒)
resp_length: 响应正文长度
title: 网页标题，提取失败为空字符串
error: 异常信息，成功则为空字符串

## 注意事项
1. 仅用于自己授权测试资产，禁止未经授权扫描外网站点
2. 探测速度单线程，大批量URL可自行改成多线程
3. 会自动过滤空行，URL首尾空白自动剔除

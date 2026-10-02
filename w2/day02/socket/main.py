import re
import socket


def socket_http_get(host: str, path: str, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # GET请求
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "User-Agent: Socket-Client/1.0\r\n"
        "Accept: */*\r\n"
        "\r\n"
    )

    s.sendall(request.encode("utf-8"))

    raw_resp = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        raw_resp += chunk
    s.close()

    resp_text = raw_resp.decode("utf-8")
    header_part, body_part = resp_text.split("\r\n\r\n", 1)
    header_lines = header_part.split("\r\n")

    status_line = header_lines[0]
    print("状态行：", status_line)
    print("响应头：")
    for line in header_lines[1:]:
        print(line)
    print("\n响应体：")
    print(body_part)


def socket_http_post(host: str, path: str, post_data: str, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    body_bytes = post_data.encode("utf-8")
    content_len = len(body_bytes)

    request_header = (
        f"POST {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "User-Agent: Socket-Client/1.0\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/x-ww-form-urlencode\r\n"
        f"Content-Length: {content_len}\r\n"
        "\r\n"
    )

    full_req = request_header.encode("utf-8") + body_bytes
    s.sendall(full_req)

    raw_resp = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        raw_resp += chunk
    s.close()

    resp_text = raw_resp.decode("utf-8")

    parse_http_response(resp_text)
    # print(resp_text)
    header_part, body_part = resp_text.split("\r\n\r\n", 1)  # 最多分隔一次
    header_lines = header_part.split("\r\n")
    status_line = header_lines[0]
    print("状态行：", status_line)
    print("响应头：")
    for line in header_lines[1:]:
        print(line)
    print("响应体：", body_part)


def parse_http_response(raw_text: str):
    header_part, body_part = raw_text.split("\r\n\r\n", 1)
    header_lines = header_part.split("\r\n")

    header_line = header_lines[0]
    match = re.match(r"HTTP/\d.\d (\d+) .+", header_line)
    status_code = int(match.group(1)) if match else None

    headers = {}
    for line in header_lines[1:]:
        if ": " in line:
            k, v = line.split(": ", 1)
            headers[k.strip()] = v.strip()
    print(status_code)
    print(headers)
    print(body_part)
    return status_code, headers, body_part


if __name__ == "__main__":
    # socket_http_get("httpbin.org", "/get")
    socket_http_post("httpbin.org", "/post", post_data="name=test&age=20")

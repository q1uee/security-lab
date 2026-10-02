import socket,ssl

if __name__=="__main__":
    host="httpbin.org"
    port=443
    raw_sock=socket.socket()
    # 包装TLS，建立加密通道
    ctx=ssl.create_default_context()
    ssl_sock=ctx.wrap_socket(raw_sock,server_hostname=host)
    ssl_sock.connect((host,port))

    req = b"GET /get HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: test\r\nAccept: */*\r\n\r\n"
    ssl_sock.sendall(req)
    resp = ssl_sock.recv(4096)
    print(resp.decode())
    ssl_sock.close()
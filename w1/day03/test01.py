if __name__=="__main__":
    data = {
    "scan_info": "test",
    "assets": [
        {"ip":"192.168.1.1", "port":80},
        {"ip":"192.168.1.2", "port":443}
        ]
    }
    print(data["assets"][0]["ip"])
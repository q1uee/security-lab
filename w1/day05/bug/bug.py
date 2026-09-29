import re

class TextExtractor:
    # Bug4：可变对象作为默认参数！经典坑
    def __init__(self, result_list=[]):
        # 私有正则属性
        self.__re_ip = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")
        self.__re_email = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
        self.__re_url = re.compile(r"https?://.*?[\s\"')>]") # Bug3：贪婪 .* 不是 .*?

        self.result = result_list

    def extract(self, text):
        # Bug1：访问 self.re_ip，实际定义是私有self.__re_ip → AttributeError
        ip_raw = self.__re_ip.findall(text)
        email_raw = self.__re_email.findall(text)
        url_raw = self.__re_url.findall(text)

        clean_url = self.__clean_url(url_raw)
        return {
            "ip": ip_raw,
            "email": email_raw,
            "url": clean_url
        }

    def __clean_url(self, url_list):
        # Bug2：直接取第0个元素，列表为空时报IndexError
        if url_list:
            first = url_list[0]
        res = []
        for u in url_list:
            u = re.sub(r'[)\s\"\'>]$', "", u)
            res.append(u)
        return res


def read_file(file_path):
    # Bug5：没有指定encoding，windows中文文件会报UnicodeDecodeError
    with open(file_path,"r",encoding="utf-8") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    extractor = TextExtractor()
    txt = read_file("log.txt")
    output = extractor.extract(txt)
    print(output)

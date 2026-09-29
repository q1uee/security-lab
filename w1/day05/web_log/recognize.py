import read_file as READ
import re

class Recognize:
    def __init__(self):
        self.Read=READ.Read_file()
        #web访问总条数
        self.all_count=0
        #url条数
        self.url_count=0
        #ip数量
        self.ip_count=0
        self.SQL_count=0
        self.XSS_count=0

    def SQL_web(self,s:str):
        data_list=re.findall(r".*sqlmap|.*order by|.*select|.*sleep|.*or [0-9]+=[0-9]+",s)
        if data_list:
            return True

        
    def XSS_web(self,s:str):
        data_list=re.findall(r".*script|.*alert|.*onerror",s)
        if data_list:
            return True

    def Index_out(self,s:str):
        data_list=re.findall(r".*/etc/passwd|.*win.ini",s)
        if data_list:
            return True

        
    def Sensitive_document(self,s:str):
        data_list=re.findall(r".*git|.*config|.*phpmyadmin|.*actuator|.*env|.*server-status",s)
        if data_list:
            return True

    def crawler_web(self,s:str):
        data_list=re.findall(r".*gobuster|.*Nikto|.*Nmap NSE|.*masscan UA",s)
        if data_list:
            return True

        
    def blasting_login(self,s:str):
        data_list=re.findall(r".*(?=POST).*(?=/admin/login).*(401|302|429)",s,re.I)#不区分大小写
        if data_list:
            return True
    
    def suspicious_web(self):
        for line in self.Read.f:

            if self.SQL_web(line):
                print(f"{line}  \033[31m 匹配SQL注入\033[0m")
                self.SQL_count+=1

            if self.XSS_web(line):
                print(f"{line}  \033[31m 匹配XSS注入\033[0m")
                self.XSS_count+=1

            if self.Index_out(line):
                print(f"{line}  \033[31m 匹配目录越界\033[0m")

            if self.Sensitive_document(line):
                print(f"{line}  \033[31m 匹配敏感文件\033[0m")

            if self.crawler_web(line):
                print(f"{line}  \033[31m 匹配爬虫扫描\033[0m")

            if self.blasting_login(line):
                print(f"{line}  \033[31m 匹配爆破扫描\033[0m")

        




    
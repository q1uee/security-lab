import re

import read_file as READ


class Recognize:
    def __init__(self):
        self.Read = READ.Read_file()
        # web访问总条数
        self.all_count = 0
        self.SQL_count = 0
        self.XSS_count = 0
        self.idex_count = 0
        self.sensitive_count = 0
        self.crawler_count = 0
        # self.blasting_count=0
        # key:val ----> ip:status
        self.login_ip_map = []

    def SQL_web(self, s: str):
        data_list = re.findall(
            r".*sqlmap|.*order by|.*select|.*sleep|.*or [0-9]+=[0-9]+", s
        )
        if data_list:
            return True

    def XSS_web(self, s: str):
        data_list = re.findall(r".*script|.*alert|.*onerror", s)
        # data_list=re.search(r"script|alert|onerror",s)
        if data_list:
            return True

    def Index_out(self, s: str):
        data_list = re.findall(r".*/etc/passwd|.*win.ini", s)
        if data_list:
            return True

    def Sensitive_document(self, s: str):
        data_list = re.findall(
            r".*git|.*config|.*phpmyadmin|.*actuator|.*env|.*server-status", s
        )
        if data_list:
            return True

    def crawler_web(self, s: str):
        data_list = re.findall(r".*gobuster|.*Nikto|.*Nmap NSE|.*masscan UA", s)
        if data_list:
            return True

    def blasting_login(self, s: str):
        data_list = re.findall(
            r".*POST.*/admin/login.*(401|302|429)", s, re.IGNORECASE
        )  # 不区分大小写
        if data_list:
            s_list = s.split(" ")
            # self.login_ip_map[s_list[0]]=s_list[8]
            self.login_ip_map.append({s_list[0]: s_list[8]})
            return True

    def blasting_login_analyse(self):

        # self.blasting_count=0
        # key:val ----> ip:status
        # self.login_ip_map=[]

        # ip:count(出现401的数量) -----> 8.210.123.55:count
        # 如果count数大于等于5，则该IP进行爆破，爆破中如果后面改IP出现302状态即爆破成功，如果出现429则被限流
        l = []

        # 存放ip,不重复存放
        ip_list = []

        # ip是否第一次出现，是则存入ip_list,不是则count+1
        # flag=True

        for item in self.login_ip_map:
            flag = False
            # current_ip, status = list(item.items())[0]
            current_ip, status = next(iter(item.items()))
            for ip in ip_list:
                if current_ip == ip:
                    flag = True
                    break

            #  print(item)  {'8.210.123.55': '401'}
            if flag == False:
                ip_list.append(current_ip)
                if status == "401":
                    l.append({current_ip: 1})
            else:
                for l_item in l:
                    # ip_key, count = list(l_item.items())[0]
                    # 告警：count 解包出来没有任何地方使用，Ruff 检测未使用变量。
                    # 约定：下划线 _ 表示这个变量是占位、不用的。
                    ip_key, _ = next(iter(l_item.items()))
                    # if l_item.key==item.key:
                    if ip_key == current_ip and status == "401":
                        l_item[ip_key] += 1
                        # break
                    if status == "302" and l_item[ip_key] >= 5:
                        print(f"{ip}爆破成功")
                        break
                    if status == "429" and l_item[ip_key] >= 5:
                        print(f"{item.key}被限流")
                        break

        # print(l)
        # print("-----------")
        # print(ip_list)

        # for d in l:
        #     ip, cnt = list(d.items())[0]
        #     if cnt >=5:
        #         print(f"爆破IP：{ip}, 401次数：{cnt}")
        #     if item[item.key]=='302' and cnt>=5:
        #         print(f"{ip}爆破成功")

        # if item[item.key]=='429' and l[ip.key]>=5:
        #     print(f"{item.key}被限流")

    def print_info(self):
        print("=" * 20)
        print("总条数：", self.all_count)
        print("SQL注入条数：", self.SQL_count)
        print("XSS条数：", self.XSS_count)
        print("目录穿越条数：", self.idex_count)
        print("敏感文件探测：", self.sensitive_count)
        print("目录扫描/爬虫：", self.crawler_count)
        print("登录爆破")

    def suspicious_web(self):
        for line in self.Read.f:
            self.all_count += 1
            if self.SQL_web(line):
                print(f"{line}  \033[31m 匹配SQL注入\033[0m")
                self.SQL_count += 1

            if self.XSS_web(line):
                print(f"{line}  \033[31m 匹配XSS注入\033[0m")
                self.XSS_count += 1

            if self.Index_out(line):
                print(f"{line}  \033[31m 匹配目录越界\033[0m")
                self.idex_count += 1

            if self.Sensitive_document(line):
                print(f"{line}  \033[31m 匹配敏感文件\033[0m")
                self.sensitive_count += 1

            if self.crawler_web(line):
                print(f"{line}  \033[31m 匹配爬虫扫描\033[0m")
                self.crawler_count += 1

            if self.blasting_login(line):
                print(f"{line}  \033[31m 匹配爆破扫描\033[0m")
                # self.blasting_count+=1

        self.print_info()
        self.blasting_login_analyse()

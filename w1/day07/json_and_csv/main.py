import json
import csv
from pathlib import Path

if __name__=="__main__":
    # ========== 模拟W2日志分析结果 ==========
    report_data = {
        "summary": {
            "total_lines": 1250,
            "error_count": 28,
            "warn_count": 45,
            "analyze_time": "2026-09-30"
        },
        "items": [
            {"line_no": 12, "level": "ERROR", "msg": "connection timeout", "ip": "192.168.1.10"},
            {"line_no": 45, "level": "WARN", "msg": "slow query", "ip": "192.168.1.11"}
        ]
    }

    json_path=Path("report.json")
    with open(json_path,"w",encoding="utf-8") as f:
        json.dump(
            report_data,
            f,
            indent=2,#开启格式化美化输出：换行 + 每一层缩进 2 个空格。
            ensure_ascii=False#中文原样保存,控制编码
        )

    csv_path=Path("report.csv")
    fieldnames=report_data["items"][0].keys() if report_data["items"] else []
    with open(csv_path,"w",encoding="utf-8",newline="")as f:#newlines不要自动转换换行符，格式问题
        # 第一个参数 f：文件句柄，数据写到这个文件
        # fieldnames：列表，定义 CSV表头顺序和列名
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        # 把 fieldnames 作为第一行写入 CSV，也就是表头
        writer.writeheader()
        # writerows()：一次性写入多行，参数是字典组成的列表
        # report_data["items"] 就是我们日志明细列表，里面每个元素是一条日志字典：
        writer.writerows(report_data["items"])

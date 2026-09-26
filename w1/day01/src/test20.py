#20 综合脚本：字符串转字典+推导式+异常捕获
def parse_user(s):
    info={}
    try:
        parts=s.split(",")
        for p in parts:
            k,v=p.split(":")
            info[k]=v
        return info
    except Exception as e:
        print("解析失败：",e)
        return None
if __name__=="__main__":
    user_str='name:root,id:1,status:active'
    user_data=parse_user(user_str)
    print("解析结果：",user_data)

    #字典推导式筛选
    active_user={k:v for k,v in user_data.items() if v=="active"}
    print("筛选active:",active_user)

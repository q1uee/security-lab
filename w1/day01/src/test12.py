#12 列表、字典基础增删查改
if __name__=="__main__":
    #列表
    name_list=["admin","test","guest"]
    name_list.append("root")
    print("列表",name_list)
    print("索引0:",name_list[0])

    #字典
    user_info={"name":"admin","pwd":"123456","enable":True}
    print("字典取值name:",user_info["name"])
    user_info["pwd"]="newpwd"
    user_info["role"]="admin"
    print("修改后的字典:",user_info)




class MyFileHandeler:
    def __init__(self,path,mode="r",encoding="utf-8"):
        self.path=path
        self.mode=mode
        self.encoding=encoding
        self.f=None
    def __enter__(self):
        self.f=open(self.path,self.mode,encoding=self.encoding)
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()
        return False

# 使用自定义上下文管理器
# with MyFileHandler("test.txt", "r") as fp:
#     print(fp.readline())
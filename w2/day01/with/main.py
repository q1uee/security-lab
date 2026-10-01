import time

# 装饰器函数，接收一个函数 func
def timer(func):
    # wrapper：包装后的新函数，*args,**kwargs 接收原函数所有参数
    # *args,**kwargs：兼容任意参数的函数（无参、多个位置参数、关键字参数都可以）
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        # 执行原来的函数，保存返回结果
        res=func(*args,**kwargs)
        cost=time.perf_counter()-start
        print(f"耗时：{func.__name__}:{cost:.4f} s")
        return res
    return wrapper

@timer
def read_big_file(file_path):
    with open(file_path,"r",encoding="utf-8")as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            '''yield 代表这是生成器函数
            调用函数不会立刻执行代码，而是返回一个生成器对象。
            循环迭代的时候，才会一行一行执行、返回一行数据。
            读取超大文件不爆内存'''
            yield line

@timer#语法糖 或 test=timer(printf)  test()
def printf():
    print("666")

if __name__=="__main__":
    # timer(printf())

    # 调用函数，此时代码还没开始读文件
    gen = read_big_file("test.log")
    # for循环迭代生成器，才会真正逐行读取
    for row in gen:
        print(row)
    timer(read_big_file("test.log"))
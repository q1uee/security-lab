if __name__=="__main__":
    ips=["1.1.1.1","2,2,2,2"]
    ports=[80,443]
    #一一配对
    for ip,port in zip(ips,ports):
        print(ip,port)

    pairs = [(1,'a'),(2,'b')]
    nums, chars = zip(*pairs)
    print(nums)  # (1, 2)
    print(chars) # ('a', 'b')

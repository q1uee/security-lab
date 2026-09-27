if __name__=="__main__":
    #普通解包：a=100,b=200
    a,b=[100,200]
    #可变解包
    #head=1 rest=[2,3,4]
    head,*rest=[1,2,3,4]
    print(head,rest)
    #front=[1,2,3] tail=4
    *front,tail=[1,2,3,4]
    print(front,tail)
    #front=1 mid=[2,3] tail=4
    front,*mid,tail=[1,2,3,4]
    print(front,mid,tail)
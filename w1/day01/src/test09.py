#09 break和continue
if __name__=="__main__":
    for i in range(1,10):
        if i==3:
            continue
        if i==7:
            break
        print(i)
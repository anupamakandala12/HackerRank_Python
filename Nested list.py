def SecondLowest(N):
    lst2=[] 
    for k in range(N):   
        name = input()
        score = float(input())
        lst1=[]
        lst1.append(name)
        lst1.append(score)
        lst2.append(lst1)

    lst3=sorted(lst2,key = lambda x: x[1])
    lst_3=lst3[1:]
    lst4=[lst_3[0][0]]  
    for i in range(1,len(lst_3)-1):
        if lst_3[0][1]==lst_3[i][1]: 
            lst4.append(lst_3[i][0])
        
    lst4=sorted(lst4,reverse=False)
   
    print(*lst4, sep='\n')        


if __name__ == '__main__':  
    N=int(input())
    SecondLowest(N)
    

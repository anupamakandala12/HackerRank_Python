def swap_case(s):
    lst=[]
    lst[:]=s #splits string into characters in a list
    lst1=[]
    for i in lst:
        if i.isupper()==True:
            i=i.lower()
            lst1.append(i)
        else:
            i=i.upper() 
            lst1.append(i)
    s="".join(lst1)  #join characters into string from list        
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

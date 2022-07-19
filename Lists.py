def Command(N):
    lst = []
    for i in range(N):
        s = input().split()
        for i in range(1,len(s)):
            s[i] = int(s[i])       
        if s[0] == "append":
            lst.append(s[1])
        elif s[0] == "extend":    
            lst.extend(s[1:])
        elif s[0] == "insert":
            lst.insert(s[1],s[2])
        elif s[0] == "remove":
            lst.remove(s[1])
        elif s[0] == "pop":
            lst.pop()
        elif s[0] == "index":
            print (lst.index(s[1]))
        elif s[0] == "count":
            print (lst.count(s[1]))
        elif s[0] == "sort":
            lst.sort()
        elif s[0] == "reverse":
            lst.reverse()
        elif s[0] == "print":
            print (lst)


if __name__ == '__main__':
    N = int(input())
    Command(N)

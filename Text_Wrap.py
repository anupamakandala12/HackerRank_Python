import textwrap

def wrap(string, max_width):
    s=len(string)
    rem= s%max_width
    z=s+rem
    L=[]
    for i in range(0,(z-1),max_width):
        if(max_width+i<=z):
            a=(string[i:max_width+i])
            L.append(a)
    print(*L,sep="\n")
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)

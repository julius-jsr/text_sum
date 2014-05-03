import sys
def noise():
    print "haha"
    f=open("abc.txt")
    print "nana"
    k=open("efgh.txt","w")
    print "jaja"
    s1=f.readline()
    if s1!="":
        l=True
    else :
        l= False
    while l is True:
        s2= f.readline()
        if s1=="":
            break
        a= s1.split('\n')
        b= s2.split('\n')
        if a[0] not in b[0]:
            k.write(s1)
        s1=s2
    k.close()
    f.close()
        
        
        

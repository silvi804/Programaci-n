c=True
while c:
    n=int(input("Altura:"))
    if n>0:
        c=False
    
for i in range(1,n+1):
    print(" "*(n-i),"#"*i,""*2,"#"*i)
    
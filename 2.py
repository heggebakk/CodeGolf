i=input()
l=list(str(i))
print(sum(map(int,str(i))) if l[::-1]==l else -1)
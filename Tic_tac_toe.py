l=[['-','-','-'],['-','-','-'],['-','-','-']]
def printlist(l):
    for i in range(len(l)):
        for j in range(len(l)):
            print(l[i][j],end=" ")
        print()
printlist(l)
heap=0
def check(l,r,c):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[r][c]=='-':
                heap=1
    return heap
xwin=0
owin=0

def diagonal_check(count,count2):
    for i in range(len(l)):
        for j in range(len(l)):
            if i==j and l[i][j]=="O":
                count+=1
                if count==3:
                    owin=1
            if i==j and l[i][j]=="X":
                count2+=1
                if count2==3:
                    xwin=1
    count=1
    count2=1
    for i in range(len(l)):
        if l[i][2-i]=="X":
            count+=1
            if count==3:
                xwin=1
        if l[i][2-i]=="O":
            count2+=1
            if count2==3:
                owin=1
        if l[0][i]==l[1][i]==l[2][i]=="X" or l[i][0]==l[i][1]==l[i][2]=="X":
            xwin=1
        
        if l[0][i]==l[1][i]==l[2][i]=="O" or l[i][0]==l[i][1]==l[i][2]=="O":
            owin=1

            

tot=0
while(tot<8):
    print("X turn:")
    r=int(input("Enter the row element:"))
    c=int(input("Enter the column element:"))
    ch=check(l,r,c)
    if ch==1:
        l[r][c]="X"
    print("O turn:")
    r=int(input("Enter the row element:"))
    c=int(input("Enter the column element:"))
    ch=check(l,r,c)
    if ch==1:
        l[r][c]="O"
    tot+=2
    print(tot)
print("X turn:")
r=int(input("Enter the row element:"))
c=int(input("Enter the column element:"))
ch=check(l,r,c)
if ch==1:
    l[r][c]="X"

printlist(l)

count=1
count2=1
diagonal_check(count,count2)
print(xwin)
print(owin)
if xwin==True:
    print("X win")
if owin==True:
    print("O win")
else:
    print("Draw Match!!!")
   
        
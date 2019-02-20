# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phonedict = {}

for i in range(0,n):
    name, phonenumber = input().split()
    phonedict[name] = phonenumber

x = input()

while len(x)>0:
    if x in phonedict:
        print(x + "=" + phonedict.get(x))
    else:
        print("Not found")
    x = input()


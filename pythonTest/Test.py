rows =int(input("请输入列数"))
i=j=k=1
flag=1
for i in range(rows):
    for j in range(rows-i-1):
        print("    ", end="\t"),
    for k in range(i+1):
        print("+   ", end="\t"),
    print("\n")

print(u'Hello World !')
print("123".join("678"))
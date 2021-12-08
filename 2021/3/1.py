f = open('input','r')
content = f.readlines()
l = [s.replace("\n", "") for s in content]

# 010
# 110
# 001

for i in l:
    for j in range(len(i)):
        print(i[j], end="")
    


import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# # 单行输入字符串
# line = sys.stdin.readline().strip()
# print(line)#输出的字符串
# l=list(map(int,input().split(" ")))
# print(l)

if __name__ == "__main__":
    data=[]
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        tmp = list(map(int, line.split(" ")))
        data.append(tmp)
    print(data)

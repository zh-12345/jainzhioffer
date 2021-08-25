class Solution:
    def f1(self):
        while True:
            a, b = map(int, input('please input a,b：').strip().split())
            if a == 0 and b == 0:
                break
            print(a + b)

    def f2(self):
        import sys
        for line in sys.stdin:
            if 'Exit' == line.rstrip():
                break
            print('Precessing message from sys.stdin *****', {line}, '******')
        print('Done')

    def f3(self):
        import sys

        while True:
            try:
                lis = list(map(int, input('please input ').split()))
                if lis[0] != 0:
                    print(sum(lis[1:]))
                else:
                    break
            except:
                break



if __name__ == "__main__":
    h = Solution()

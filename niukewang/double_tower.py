# 现在有红，绿两种颜色的石头，现在我们需要用这两种石头搭建一个塔，塔需要满足如下三个条件：
# 1． 第1层应该包含1块石头，第2层应该包含两块，第 i 层需要包含 i 块石头。
# 2． 同一层的石头应该是同一个颜色（红或绿）。
# 3． 塔的层数尽可能多。  问在满足上面三个条件的前提下，有多少种不同的建造塔的方案，
# 当塔中任意一个对应位置的石头颜色不同，我们就认为这两个方案不相同。石头可以不用完。
def solve(n, m):
    dp = [m for i in range(m + 1)]  # 记录n到当前点所需要的步数
    t = [[] for i in range(m + 1)]  # 记录每个数的质因数
    for i in range(2, m + 1):
        for j in range(i + i, m + 1, i):
            t[j].append(i)  # 倒过来，通过公因数来找原数，避免了重复计算
    dp[n] = 0
    for i in range(n, m + 1):
        if dp[i] < m:
            for x in t[i]:
                if i + x < m + 1:
                    dp[i + x] = min(dp[i + x], dp[i] + 1)
    if dp[m] < m:
        return dp[m]
    else:
        return -1


n, m = map(int, input().split())
print(solve(n, m))
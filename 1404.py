class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        while s != "1":
            if s[-1] == "0":  # 偶数
                s = s[:-1]  # 除以2
            else:  # 奇数
                num = int(s, 2) + 1  # 转十进制加1
                s = bin(num)[2:]  # 再转回二进制

            steps += 1

        return steps

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSteps("11111"))
    print(bin(123))
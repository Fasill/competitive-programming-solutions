class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = list(s)
        ans = ''
        s = [i for i in s if i != ""]
        for i in range(1,len(s)+1):
            ans += f'{s[-i]} '

        return ans[:-1]
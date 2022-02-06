next[k]串第一个元素为-1
之后若next[k+1]与needle[i]相等, k+=1
如果不相等，k = next[k]

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack)
        b = len(needle)
        if b != 0:
            next = self.getnext(needle, b)
            j = -1
            for i in range(a):
                while(j > -1 and needle[j+1] != haystack[i]):
                    j =next[j]
                if needle[j+1] == haystack[i]:
                    j += 1
                if j == b-1:
                    return i-b+1
            return -1
        else:
            return 0

    def getnext(self, needle, b):
        next = ['' for i in range(b)]
        k = -1
        next[0] = k
        for i in range(1, b):
            while (k >-1 and needle[k+1] != needle[i]):
                k = next[k]
            if needle[k+1] == needle[i]:
                k += 1
            next[i] = k  

        return next

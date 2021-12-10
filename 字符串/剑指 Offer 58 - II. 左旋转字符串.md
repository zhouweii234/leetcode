题目
----
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

限制：
1 <= k < s.length <= 10000

思路
----
1. 反转区间为前n的子串
2. 反转区间为n到末尾的子串
3. 反转整个字符串
![image](https://user-images.githubusercontent.com/62086490/145578634-3d9aacf2-06bc-4f70-a9ae-85eb865106a1.png)


代码
----
```python
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        def reverse(str):
            left, right = 0, len(str)-1
            while left < right:
                str[left], str[right] = str[right], str[left]
                left += 1
                right -= 1
            return str

        s = list(s)
        s[0:n] = reverse(s[0:n])
        s[n:] = reverse(s[n:])
        s = reverse(s)

        return ''.join(s)
```

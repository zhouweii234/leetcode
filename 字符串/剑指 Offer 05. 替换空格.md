题目
----
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."

思路
----
首先扩充数组到每个空格替换成"%20"之后的大小。

然后从后向前替换空格，也就是双指针法，过程如下：

i指向新长度的末尾，j指向旧长度的末尾。

![68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f65366339643234656c7931676f36716d6576686770673230647530396d3471702e676966](https://user-images.githubusercontent.com/62086490/145541738-0593c920-8766-4ff0-826f-dd63fc899950.gif)

代码
----
```python
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = s.count(' ')

        res = list(s)
        res.extend([' ']*count*2)
        left, right = len(s)-1, len(res)-1

        while left >= 0:
            if s[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right-2: right+1] = '%20'
                right -=3
            left -= 1

        return ''.join(res)
```

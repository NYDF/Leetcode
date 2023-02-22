#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
import collections
def findSubstring(s, words):

    res = []
    count_words = collections.Counter(words)

    for i in range(len(s) - len(words)*len(words[0])+1):
        count = []
        for j in range(i, i+len(s[i:i+len(words)*len(words[0])]), len(words[0])):
            count.append(s[j:j+len(words[0])])
        count = collections.Counter(count)
        print(count)
        if count_words == count:
            res.append(i)
    return res

# @lc code=end
words = ["word","good","best","good"]
s = "wordgoodgoodgoodbestword"
print(findSubstring(s, words))

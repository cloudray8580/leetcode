class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = ""
        max = 0
        for i in range(len(s)): # range start from 0
            # if there is a existing character
            if s[i] in current:
                # we cut a part of the current to continue
                index = current.find(s[i])

                # handle the boundary value
                if index+1 < len(current):
                    current = current[index+1:]
                    current += s[i]
                else:
                    current = s[i]
            # if the character not in there, just add it to the buffer
            else:
                current += s[i]
                if len(current) > max:
                    max = len(current)
        return max

    def lengthOfLongestSubstringBetter(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = {}
        left_boundary = 0
        max = 0
        for i in range(len(s)): # range start from 0
            #if current.has_key(s[i]):
            # the above function is for python 2.X, the latter is for python 3.X
            if current.__contains__(s[i]):
                # we update the length
                index = current[s[i]]
                if left_boundary <= index:
                    left_boundary = index + 1

            current[s[i]] = i
            length = i - left_boundary + 1
            if length > max:
                max = length

        return max

instance = Solution()
str = "tmmzuxt"
print(instance.lengthOfLongestSubstring(str))
print(instance.lengthOfLongestSubstringBetter(str))
str = "aab"
print(instance.lengthOfLongestSubstring(str))
print(instance.lengthOfLongestSubstringBetter(str))
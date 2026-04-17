class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            # Step 1: find the # that separates length from content
            j = i
            while s[j] != "#":
                j += 1
            # Now s[i:j] is the length portion
            length = int(s[i:j])
            # Step 2: read `length` characters starting after the #
            string = s[j + 1 : j + 1 + length]
            result.append(string)
            # Step 3: advance i to the start of the next length prefix
            i = j + 1 + length
        return result
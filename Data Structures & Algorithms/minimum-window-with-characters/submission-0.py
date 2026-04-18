class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window  = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if s1_count == window:
            return True

        for i in range(len(s1), len(s2)):
            # add new right char
            window[ord(s2[i]) - ord('a')] += 1
            # remove left char that's sliding out
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_count == window:
                return True

        return False
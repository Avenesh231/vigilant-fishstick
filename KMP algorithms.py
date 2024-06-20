class KMP:
    def partial(self, pattern):
        """Calculate partial match table: String -> [Int]"""
        ret = []
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, text, pattern):
        """KMP search main algorithm: String -> String -> [Int]
        Return all the matching positions of pattern string P in T
        """
        partial, result, j = self.partial(pattern), [], 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = partial[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                result.append(i - (j - 1))
                j = partial[j - 1]
        return result

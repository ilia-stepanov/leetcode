class Solution:
    def isAnagramUsingSorting(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t


    def isAnagramUsingFixedSizeArray(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        array = [0] * 26
        for index, value in enumerate(s):
            array[ord(value)-97] += 1
            array[ord(t[index])-97] -= 1
        return max(array) == 0 and min(array) == 0


    def isAnagramUsingHashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencies = dict()
        for index, value in enumerate(s):
            frequencies[value] = frequencies.get(value, 0) + 1
            frequencies[t[index]] = frequencies.get(t[index], 0) - 1
        return max(frequencies.values()) == 0 and min(frequencies.values()) == 0


    def isAnagramUsingPrimeHashing(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        prime_numbers = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        s_value = 1
        t_value = 1
        for index, value in enumerate(s):
            s_value *= prime_numbers[ord(value)-97]
            t_value *= prime_numbers[ord(t[index])-97]
        return s_value == t_value


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) <= 20:
            return self.isAnagramUsingPrimeHashing(s, t)
        return self.isAnagramUsingFixedSizeArray(s, t)

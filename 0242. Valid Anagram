class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Solution:
    def groupAnagramsUsingSorting(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(val)) for val in strs]
        result = dict()
        for index, sorted_str in enumerate(sorted_strs):
            if sorted_str not in result:
                result[sorted_str] = []
            result[sorted_str].append(strs[index])
        return list(result.values())


    def groupAnagramsUsingCharCount(self, strs: List[str]) -> List[List[str]]:
        char_counts = dict()
        for val in strs:
            count_list = [0] * 26
            for char in val:
                position = ord(char) - 97
                count_list[position] += 1
            count_tuple = tuple(count_list)
            if count_tuple not in char_counts:
                char_counts[count_tuple] = []
            char_counts[count_tuple].append(val)
        return list(char_counts.values())


    def getHashUsingPrimeHashing(self, s: str) -> int:
        prime_numbers = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        s_value = 1
        for index, value in enumerate(s):
            s_value *= prime_numbers[ord(value)-97]
        return s_value


    def groupAnagramsUsingPrimeHashing(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for s in strs:
            prime_hash = self.getHashUsingPrimeHashing(s)
            if prime_hash not in result:
                result[prime_hash] = []
            result[prime_hash].append(s)
        return list(result.values())


    def getAnagramsTrie(self, strs: List[str]) -> TrieNode:
        trie = TrieNode()
        sorted_strs = [''.join(sorted(val)) for val in strs]
        for index, sorted_str in enumerate(sorted_strs):
            curr = trie
            if sorted_str == "":
                if sorted_str not in curr.children:
                    curr.children[sorted_str] = TrieNode()
                curr = curr.children[sorted_str]
            for char in sorted_str:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.words.append(strs[index])
        return trie


    def get_groups(self, trie: TrieNode, groups: List[str]) -> None:
        if trie.words:
            groups.append(trie.words)
        for child in trie.children.values():
            self.get_groups(child, groups)


    def groupAnagramsTrieBasedGrouping(self, strs: List[str]) -> List[List[str]]:
        trie = self.getAnagramsTrie(strs)
        result = []
        self.get_groups(trie, result)
        return result
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagramsTrieBasedGrouping(strs)

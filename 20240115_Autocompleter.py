#| Implement an autocomplete system.
#| That is, given a query string s and a set of all possible query strings,
#| return all strings in the set that have s as a prefix.

#------------------#
# Define Functions #
#------------------#

class TrieNode:
    def __init__(self):
        #| Initialise a TrieNode with a dictionary to store children nodes
        self.children = {}
        #| Flag to indicate if the node marks the end of a word
        self.is_end_of_word = False

class AutocompleteSystem:
    def __init__(self, words):
        #| Initialise the autocomplete system with a root TrieNode
        self.root = TrieNode()
        #| Build the trie from the provided set of words
        self.build_trie(words)

    def build_trie(self, words):
        #| Iterate through each word in the set of words and insert it into the trie
        for word in words:
            node = self.root
            for char in word:
                #| Create a new TrieNode if the character is not present in the current node's children
                if char not in node.children:
                    node.children[char] = TrieNode()
                #| Move to the next node in the trie
                node = node.children[char]
            #| Mark the end of the word
            node.is_end_of_word = True

    def autocomplete(self, query):
        #| Initialise variables
        node = self.root
        result = []
        #| Traverse the trie based on the characters in the query
        for char in query:
            #| Check if the character is present in the current node's children
            if char in node.children:
                node = node.children[char]
            else:
                #| If the character is not present, return an empty result
                return result

        #| Perform depth-first search to find all words with the given query prefix
        self._dfs(node, query, result)
        return result

    def _dfs(self, node, path, result):
        #| If the current node marks the end of a word, add the word to the result
        if node.is_end_of_word:
            result.append(path)

        #| Recursively traverse the children nodes and update the path
        for char, child_node in node.children.items():
            self._dfs(child_node, path + char, result)

#---------------------#
# Example Application #
#---------------------#

words = ["apple", "appetizer", "banana", "bat", "batman"]
autocomplete_system = AutocompleteSystem(words)

query = "app"
suggestions = autocomplete_system.autocomplete(query)
print("Autocomplete suggestions for '{}': {}".format(query, suggestions))

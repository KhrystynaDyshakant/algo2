def initialize_dict(words):
    word_dict = {}
    for word in words:
        length = len(word)
        if length not in word_dict:
            word_dict[length] = []
        word_dict[length].append(word)
    return word_dict

def find_max_chain_length(word, word_dict, storage):
    if word in storage:
        return storage[word]

    max_chain_length = 1

    for i in range(len(word)):
        reduced_word = word[:i] + word[i + 1:]
        if len(reduced_word) in word_dict and reduced_word in word_dict[len(reduced_word)]:
            chain_length = 1 + find_max_chain_length(reduced_word, word_dict, storage)
            max_chain_length = max(max_chain_length, chain_length)

    storage[word] = max_chain_length
    return max_chain_length

def main():
    with open("wchain.in", "r") as input_file:
        n = int(input_file.readline().strip())
        
        if not (1 <= n <= 10**5):
            print("1 ≤ N ≤ 10^5")
            return

        words = [input_file.readline().strip() for _ in range(n)]

        for word in words:
            if not word.islower() or not all('a' <= c <= 'z' for c in word):
                print(f"Слово повинно складатись з малих літер: {word}")
                return

    word_dict = initialize_dict(words)

    max_chain_length = 0

    for word in words:
        chain_length = find_max_chain_length(word, word_dict, {})
        max_chain_length = max(max_chain_length, chain_length)

    with open("wchain.out", "w") as output_file:
        output_file.write(str(max_chain_length))

if __name__ == "__main__":
    main()
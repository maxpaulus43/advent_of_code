
def checksum(words):
    triples = 0
    doubles = 0

    for word in words:
        char_count = [0] * 26

        for char in word:
            char_count[ord(char) - ord("a")] += 1

        if 2 in char_count:
            doubles += 1
        if 3 in char_count:
            triples += 1

    return triples * doubles


def find_common_letters(words):

    for i in range(len(words[0])):
        changed_words = [word[:i] + word[i + 1:] for word in words]
        dejavu = set()

        for changed_word in changed_words:
            if changed_word in dejavu:
                return changed_word
            else:
                dejavu.add(changed_word)

    return "none"


if __name__ == "__main__":
    with open("input/day_2.txt") as f:
        words = [word.rstrip() for word in f.readlines()]
        print(checksum(words))
        print(find_common_letters(words))

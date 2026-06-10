from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=abs, reverse=True)


# do not modify below this line
words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]
numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(words)
print(sort_words(words))

print(numbers)
print(sort_numbers(numbers))
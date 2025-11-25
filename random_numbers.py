import random
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
def main():
 #remember to investigate why words can't be in the function
  append_random_words(words)
  print("Before:", words)
  append_random_words(words, 2)
  print("After adding 2 more:", words)
  numbers = [16.2, 75.1, 52.3]
  print("Before:", numbers)
  append_random_numbers(numbers)
  print("After:", numbers)
  append_random_numbers(numbers, 3)
  print("After adding 3 more:", numbers)


def append_random_words(word_list, quantity=1):
  for _ in range(quantity):
    word = random.choice(words)
    word_list.append(word)

def append_random_numbers(num_list, quantity=1):
  for _ in range(quantity):
    num = random.uniform(0, 100)
    num = round(num, 1)
    num_list.append(num)

if __name__ == "__main__":
  main()
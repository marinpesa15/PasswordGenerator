import random

random = random.Random()

letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_small= "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
spec_char = "!§$%&/+*-_#'."

all = letters_big + letters_small + numbers + spec_char

lenght = 16
print("".join(random.sample(all, lenght)))
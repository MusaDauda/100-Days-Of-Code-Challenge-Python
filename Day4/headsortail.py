import random
test_seed= int(input("Create a seed number: "))
random.seed(test_seed)
test = random.randint(0,1)
if test == 0:
    print("Heads")
else:
    print("Tails")

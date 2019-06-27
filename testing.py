import random
import string

def word_gen():
    word_list = string.ascii_letters[:52]
    # gen_value = ""
    ma_choice = random.randrange(5)
    num_list = string.digits[:10]

    #abcd choice indic
    a = word_list[random.randrange(52)]
    b = word_list[random.randrange(52)]
    c = word_list[random.randrange(52)]
    d = word_list[random.randrange(52)]
    num = num_list[random.randrange(10)]

    if ma_choice == 0:
        return a + b + c + d + num
    elif ma_choice == 1:
        return a + b + c + num + d
    elif ma_choice == 2:
        return a + b + num + c + d
    elif ma_choice == 3:
        return a + num + b + c + d
    else:
        return num + a + b + c + d

foo = open("lists.txt", "w")

with open("lists.txt", "w") as file:
    for x in range(100):
        file.write(str(word_gen())+"\n")

# for x in range(5):
    

import re
with open("day2.txt") as file:
    good_passwords = 0
    for line in file:
        line = line.strip()
        list_line = re.split("[- :]",line)
        #part two
        if (list_line[4][int(list_line[0]) - 1] == list_line[2]) ^ (list_line[4][int(list_line[1]) - 1] == list_line[2]):
            good_passwords += 1
            print("nice",list_line,good_passwords)
        else:
            print("naughty",list_line,good_passwords)

        """
            #part one
            letter_count = 0
            for i in list_line[4]:
            if i == list_line[2]:
                letter_count += 1
            if letter_count > int(list_line[1]) or letter_count < int(list_line[0]):
                print("nice",list_line,bad_passwords)
            else:
                bad_passwords += 1
                print("naughty",list_line,bad_passwords)
        """
    print(good_passwords)
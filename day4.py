import re
MANDATORY_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}
print(MANDATORY_FIELDS)
with open("day4.txt") as file:
    fields = set()
    valid = 0
    for line in file:
        #if the line is just \n, delete the set
        if line == "\n":
            if MANDATORY_FIELDS.issubset(fields):
                valid += 1
            fields = set()
        else:
           for i in re.split("[: ]",line.strip()):
               fields.add(i)
        print (fields)
    print(valid)
    

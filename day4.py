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
    fields = []
    valid = 0
    for line in file:
        #if the line is just \n, delete the set
        if line == "\n":
            fields.sort()
            #should look like this ['#623a2f', '087499704', '1980', '2012', '2030', '74in', 'byr', 'ecl', 'eyr', 'grn', 'hcl', 'hgt', 'iyr', 'pid']
            print(fields)
            if fields[3]
                pass
            fields = []
        else:
           for i in re.split("[: ]",line.strip()):
               fields.append(i)
        print (fields)
    print(valid) #ok I was off by one for some reason??
    

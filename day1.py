def multiply():
    input_list = []
    with open("day1in.txt") as file:
        for line in file:
            input_list.append(int(line.strip()))
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if input_list[j] + input_list[i] == 2020:
                return(input_list[j]*input_list[i])
def multiply_three():
    input_list = []
    with open("day1in.txt") as file:
        for line in file:
            input_list.append(int(line.strip()))
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            for k in range(len(input_list)):
                if input_list[j] + input_list[i] + input_list[k]  == 2020:
                    return(input_list[j]*input_list[i]*input_list[k])

def main():
    print(multiply_three())
main()
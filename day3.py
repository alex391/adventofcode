def down1(right):
    with open("day3.txt") as file:
            next_tree = 0
            trees_hit = 0
            for line in file:
                if line[next_tree] == "#":
                    trees_hit += 1
                next_tree += right
                next_tree = next_tree % 31
                #print(line.strip(),"next tree:",next_tree,"trees hit:",trees_hit)
            return trees_hit
def down2():
    with open("day3.txt") as file:
            next_tree = 0
            trees_hit = 0
            i = 0
            for line in file:
                if i % 2 != 0:
                    i += 1
                    pass
                else:
                    if line[next_tree] == "#":
                        trees_hit += 1
                    next_tree += 1
                    next_tree = next_tree % 31
                    i += 1
                    #print(line.strip(),"next tree:",next_tree,"trees hit:",trees_hit,"i:",i)
            return trees_hit
"""

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""
def main():
    trees_hit = 0
    trees_hit = down1(1) * down1(3) * down1(5) * down1(7) * down2()
    print(trees_hit)

main()
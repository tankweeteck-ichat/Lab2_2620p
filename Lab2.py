print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")



def display_main_menu():
    print(">>> display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print(">>> get_user_input")
    numlist = []
    inputstr = input()
    inputlist = inputstr.split(",")
    print(inputlist)
    for eachstr in inputlist:
        numlist.append(float(eachstr))
    return numlist


def calc_average(numlist):
    print(">>> calc_average")
    total = 0.0
    for eachnum in numlist:
        total += eachnum
    return (total/len(numlist))



def find_min_max(numlist):
    print(">>> find_min_max")
    templist = numlist.copy()
    templist.sort()
    return [templist[0], templist[-1]]


def sort_temperature(numlist):
    print(">>> sort_temperature")
    templist = numlist.copy()
    templist.sort()
    return templist    


def calc_median_temperature(numlist):
    print(">>> calc_media_temperature")




def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    MinMax = []

    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    print("Average = ", f"{average:0.2f}")
    MinMax = find_min_max(num_list)
    print("Min = ", MinMax[0])
    print("Max = ", MinMax[-1])
    sorted = sort_temperature(num_list)
    print("Sorted Temperature: ", sorted)
    #median = calc_median_temperature(num_list)
    #print("Median = ", f"{median:0.2f}")



if __name__ == "__main__":
    main()

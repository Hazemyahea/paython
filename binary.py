## Function to Make a binary search with parameter which you can add a list of numbers  
def binary(my_list):
    upper = len(my_list)
    lower = 0
    guees = 40
    mid = int((upper+lower) / 2)
    count = 0
    while (upper >= lower):
        mid = (upper + lower) // 2
        print(mid)
        count += 1
        if my_list[mid] == guees:
            print("We find guess after" + str(count) + "Try")
            break
        elif guees < my_list[mid]:
                upper = mid
                mid = int((upper+lower) / 2)
        elif guees > my_list[mid]:
                lower = mid
                mid = int((upper+lower) / 2)

## Example 
binary([10, 20, 30, 40, 50])

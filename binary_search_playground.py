 

target = 4 

numbers = [19,17,15,13,11,9,7,5,4,3] 

low = 0 

high = len(numbers) - 1 

found = False 

while low <= high: 

    mid = (low + high) // 2 
    found_index = mid
    if numbers[mid] == target: 

        print(target, 'found at index', found_index) 

        found = True 

        break 

    elif target > numbers[mid]: 

        high = mid + 1

    else: 

        low = mid

         

if not found: 

    print(target, 'not found') 
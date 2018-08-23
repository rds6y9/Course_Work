import random

'''
Function called by mergeSort() to perform recursive number sorting.
'''
def MergeSort_impl(num_list):
    # Base Case
    if len(num_list) == 1:
        return num_list
    
    # Otherwise, split list again.
    merged_list = []
    first_half_list = MergeSort_impl(num_list[:len(num_list)//2]) # First element till 1 before half
    second_half_list = MergeSort_impl(num_list[len(num_list)//2:]) # Half element till last element

    # Then merge the results
    while len(first_half_list) > 0 and len(second_half_list) > 0:
        if first_half_list[0] <= second_half_list[0]:
            merged_list.append(first_half_list[0])
            first_half_list.pop(0)
        else:
            merged_list.append(second_half_list[0])
            second_half_list.pop(0)
    
    # Return the lists added to pick up any remaining values left in a list
    return merged_list + first_half_list + second_half_list

'''
Parameters:
    num_list(type: list<Numeric>) => A list of numbers to be sorted

Returns:
    A sorted list of numbers.

Return Type: list<Numeric>
'''
def mergeSort(num_list):
    # Ensure correct parameters are sent to function
    if type(num_list) is not list:
        return "Invalid parameters sent to function \"mergeSort()\"." 

    # Call recursive merge sort function to sort list
    return MergeSort_impl(num_list)

if __name__ == "__main__":
    a = [random.randint(0, 9) for _ in range(10)] 
    b = mergeSort(a)
    print('mergeSort is', 'correct' if b == sorted(b) else 'incorrect')
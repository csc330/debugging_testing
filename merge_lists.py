def merge_sorted(list1, list2):
    '''
    Input: list1 and list2 are sorted lists of integers (ascending order)
    Returns: merged_list, a *sorted* list containing all elements of
            list1 and list2
    '''
    merged_list = []
    if len(list1) == 0 and len(list2) == 0:
        return merged_list

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            next_item = list1.pop(0)
        else:
            next_item = list2.pop(0)
        merged_list.append(next_item)

    # append remaining element from each list
    if len(list1) == 1:
        merged_list.append(list1[0])
    if len(list2) == 1:
        merged_list.append(list2[0])

    return merged_list

def main():
    l1 = [1, 3, 5, 7]
    l2 = [2, 4, 6, 8]
    print(merge_sorted(l1, l2))

if __name__ == '__main__':
    main()

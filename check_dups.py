import pdb

def all_unique(a_list):
    '''
    Input: a_list, a list of objects
    Returns: True if all elements in a_list are unique, False otherwise
    '''
    for i in range(len(a_list) - 1):
       for j in range(i+1, len(a_list)):
          if a_list[i] == a_list[j]:
             return False
    return True

def main():
    pdb.set_trace()
    my_list1 = [9, 4, 5, 10, 12, 43, 11, 2]
    no_dups = all_unique(my_list1)
    print('All elements in', my_list1, 'unique?', no_dups)

    my_list2 = [9, 4, 5, 10, 12, 4, 11, 2]
    no_dups = all_unique(my_list2)
    print('All elements in', my_list2, 'unique?', no_dups)

if __name__ == "__main__":
    main()

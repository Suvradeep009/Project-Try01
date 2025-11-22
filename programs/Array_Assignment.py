import numpy as np

def array_operations():
    my_array = np.array([915, 987, 983, 980, 975,928])

    print("Initial Array: %s" % my_array)

    # 1. Insertion
    position_insert = 2
    element_insert = 991

    if 0 <= position_insert <= len(my_array):
        my_array = np.insert(my_array, position_insert, element_insert)
        print("Array after Insertion of %s at position %s: %s" % (element_insert, position_insert, my_array))
    else:
        print("Insertion failed: Position %s is out of bounds." % position_insert)

    # 2. Deletion (Removing the element at position 3)
    position_delete = 3

    if 0 <= position_delete < len(my_array):
        deleted_element = my_array[position_delete]
        my_array = np.delete(my_array, position_delete)
        print("Array after Deletion of element %s at position %s: %s" % (deleted_element, position_delete, my_array))
    else:
        print("Deletion failed: Position %s is out of bounds." % position_delete)

    # 3. Searching (Finding the position of 983)
    search_element = 983

    if search_element in my_array:
        positions = np.where(my_array == search_element)[0]
        print("Element %s found at position(s): %s" % (search_element, positions))
    else:
        print("Element %s not found in the array." % search_element)

   

    # 4. Updation (Modifying element at position 1 to 15)
    position_update = 1
    new_value = 951

    if 0 <= position_update < len(my_array):
        old_value = my_array[position_update]
        my_array[position_update] = new_value
        print("Array after Updation of position %s (from %s to %s): %s" % (position_update, old_value, new_value, my_array))
    else:
        print("Updation failed: Position %s is out of bounds." % position_update)


    # 5. Traversing
    print("Traversing all elements:")
    for element in my_array:
        print("Current element: %s" % element)
    print("Traversing complete.")


array_operations()

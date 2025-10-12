"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start = int, end = int):
    my_list = list(range(start, end+1))
    return my_list
    

def filter_even_numbers(numbers):
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def square_numbers(numbers):
    return[n**2 for n in numbers]


def find_max_min(numbers):
    max_nbr = max(numbers)
    min_nbr = min(numbers)
    max_and_min = (max_nbr, min_nbr)
    return max_and_min

def remove_duplicates(items):
    result_list = []
    for i in items:
        if i not in result_list:
            result_list.append(i)
    return result_list


def merge_lists(list1, list2):
    merged_list = []
    max_length = max(len(list1), len(list2))
    for i in range(max_length):
        if i < len(list1):
            merged_list.append(list1[i])
        if i < len(list2):
            merged_list.append(list2[i])

    return merged_list

def list_statistics(numbers):

    if not numbers:
        return None

    
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    max_nbr = max(numbers)
    min_nbr = min(numbers)
    
    result = {"sum": total, "average": average, "count": count, "max": max_nbr, "min": min_nbr}
    return result


def chunk_list(items, chunk_size):
    list_chunked = []
    for i in range(0, len(items),chunk_size):
        list_chunked.append(items[i : i + chunk_size])
    
    return list_chunked



# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")

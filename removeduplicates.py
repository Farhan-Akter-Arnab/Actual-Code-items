def remove_duplicates_and_count(sequence):
    seen = set()
    output_list = []
    counts = {}  # Dictionary to store counts of each item
    for item in sequence:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
        counts[item] = counts.get(item, 0) + 1  # Increment the count for each item
    deleted_items = list(set(sequence) - set(output_list))
    print("Deleted items:", deleted_items)
    print("Occurrences of each item:", counts)
    return output_list
if __name__ == "__main__":
    prompt = input("Do you want to remove duplicates from a list or string? (list/string): ").strip().lower()
    if prompt == "list":
        input_list = input("Enter a list of numbers separated by spaces: ").strip().split()
        input_list = [int(x) for x in input_list]  # Convert input to a list of integers
        result_list = remove_duplicates_and_count(input_list)
        print("List after removing duplicates:", result_list)
    else:
        input_string = input("Enter a string: ").strip()
        result_list = remove_duplicates_and_count(input_string)
        print("String after removing duplicates:", ''.join(result_list))
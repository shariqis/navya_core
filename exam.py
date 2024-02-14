def find_strings_starting_with_prefix(prefix, input_list):
    result = []

    for current_string in input_list:
        # Check if the current string starts with the given prefix
        match = True
        for i in range(len(prefix)):
            print("mmmm",i,current_string)
            
            if i >= len(current_string) or prefix[i] != current_string[i]:
                print('len',len(current_string))
                print('vvvv',current_string[i])
                match = False
                break

        # If there is a match, add the string to the result list
        if match:
            result.append(current_string)

    return result

# Example usage
prefix = 'ca'
input_list = ['cat', 'car', 'fear', 'center']

output = find_strings_starting_with_prefix(prefix, input_list)
print(output)  # Output: ['cat', 'car']
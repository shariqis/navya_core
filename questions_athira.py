# # Q1: 1.	A list contains k no.of digits. Input k and digits. 
# # Rotate the list like first digit in last and last in first position.


# # def rotate_list(k, digits):
# #     # Check if the number of digits is less than or equal to k
# #     if len(digits) <= k:
# #         print("Invalid input: The number of digits should be greater than k.")
# #         return
    
# #     # Rotate the list
# #     rotated_list = digits[-k:] + digits[:-k]
    
# #     print("Original List:", digits)
# #     print("Rotated List:", rotated_list)

# # # Get input from the user
# # k = int(input("Enter the value of k: "))
# # digits = [int(x) for x in input("Enter the list of digits separated by space: ").split()]

# # # Call the function to rotate the list
# # rotate_list(k, digits)


# # ------------------------------------------------------------------------------------------

# # Q2:  2.	3 coins of 1,2,5 rupees has given. Sum of coins 
# # should be 11 using different pattern of addition.
# # Also print the shortest pattern.


# def find_coin_combinations(target_sum, coins, current_combination, all_combinations):
#     if target_sum == 0:
#         all_combinations.append(current_combination.copy())
#         return

#     for coin in coins:
#         if coin <= target_sum:
#             current_combination.append(coin)
#             find_coin_combinations(target_sum - coin, coins, current_combination, all_combinations)
#             current_combination.pop()

# def main():
#     target_sum = 11
#     coins = [1, 2, 5]
#     all_combinations = []

#     find_coin_combinations(target_sum, coins, [], all_combinations)

#     print("All combinations:")
#     for combination in all_combinations:
#         print(combination)

#     shortest_pattern = min(all_combinations, key=len)
#     print("\nShortest pattern:", shortest_pattern)

# if __name__ == "__main__":
#     main()

# # -----------------------------------------------------------------------
# # # Q4:  List of words are given. 
# # # Create sub list of words with similar letters and sort them (Anagrams)
    
    
# # from collections import defaultdict

# # def group_anagrams(words):
# #     # Use defaultdict to create a dictionary with lists as default values
# #     anagram_groups = defaultdict(list)

# #     # Group words by sorted letters
# #     for word in words:
# #         sorted_word = ''.join(sorted(word))
# #         anagram_groups[sorted_word].append(word)

# #     # Sort the groups and return the result
# #     result = [sorted(group) for group in anagram_groups.values()]
# #     return result

# # # Example usage
# # word_list = ["listen", "silent", "enlist", "heart", "earth", "rat", "tar", "art"]

# # anagram_sublists = group_anagrams(word_list)

# # # Print the result
# # for sublist in anagram_sublists:
# #     print(sublist)


# # -------------------------------------------------------------------

# # Q- New1
# # Given the input string "aaddeabbceefg" can you write a program or function 
# # that transforms the string into the desired format "2a2d1e1a2b1c2e1f1g"?

# # def encode_string(input_str):
# #     result = ""
# #     count = 1

# #     for i in range(1, len(input_str)):
# #         if input_str[i] == input_str[i - 1]:
# #             count += 1
# #         else:
# #             result += str(count) + input_str[i - 1]
# #             count = 1

# #     result += str(count) + input_str[-1]

# #     return result

# # # Example usage
# # input_str = "aaddeabbceefg"
# # encoded_str = encode_string(input_str)
# # print(encoded_str)

# # ------------------------------------------------

# # def make_bold(fn):
# #     def wrapped():
# #         return "<b>" + fn() + "</b>"
# #     return wrapped

# # def make_italic(fn):
# #     def wrapped():
# #         return "<i>" + fn() + "</i>"
# #     return wrapped

# # def make_underline(fn):
# #     def wrapped():
# #         return "<u>" + fn() + "</u>"
# #     return wrapped
# # @make_bold
# # @make_italic
# # @make_underline
# # def hello():
# #     return "hello world"
# # print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
# -------------------------------------------------

# a=[1, 2, 3, 4, 5, 5, 3, 6, 2]
# a.sort(reverse=True)
# print(a)
# n=4
# print(a[:4])



# -------------------------------------------------


# a="aaddeabbceegg" #"2a2d1e1a2b1c2e1f1g"
# out=""
# cout=1
# for i in range(1,len(a)):    
#     if a[i]==a[i-1]:
#         cout+=1
#     else:
#         out+=str(cout)+a[i-1]
#         cout=1
# out+=str(cout)+a[i]        
# print(out)            
        
# -------------------------------------------------
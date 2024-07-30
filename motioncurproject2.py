def get_user_input():
    #Prompt the user to enter a sentence or paragraph.
    user_input = input("Please enter a sentence or paragraph: ")
    return user_input

def count_words(input_string):
    """Count the number of words in the input string."""
    words = input_string.split()
    return len(words)

def display_output(word_count):
    #Display the word count as the output of the program.
    print(f"The input contains {word_count} words.")

def main():
    user_input = get_user_input()
    if user_input:  # Check for empty input
        word_count = count_words(user_input)
        display_output(word_count)
    else:
        print("Please enter a valid input.")
#  (#)This notation is used for the single line comment 
"""
This is a multi-line comment.
It can span multiple lines.
"""


if __name__ == "__main__":
    main()
def main():
  # Prompt the user to input a string
  user_input = input("Please enter a list (limited to 500 characters): ")
  
  # Split the string into a list of words
  words = user_input.split()
  
  # Sort the list of words alphabetically
  words.sort()
  
  # Print the sorted list of words
  print("Alphabetical order:")
  for word in words:
    print(word)

# Run the main function
if __name__ == "__main__":
  main()
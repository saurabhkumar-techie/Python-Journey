def convert_to_dashed_string(text: str) -> str:
    """
    Converts a given string to a dashed format by:
    - Removing special characters
    - Replacing spaces with dashes
    - Converting the string to lowercase
    """
    # Define allowed characters: alphanumeric and space
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    
    # Remove any character that is not in allowed_chars
    cleaned_text = ''.join(c for c in text if c in allowed_chars)
    
    # Split the cleaned text by spaces and join using dashes
    dashed_text = '-'.join(cleaned_text.split())
    
    # Convert to lowercase for consistency
    return dashed_text.lower()

# Example usage
input_text = "hey  you are good!"
output_text = convert_to_dashed_string(input_text)
print(output_text)  # Output: "hey-you-are-good"

# Additional test cases
print(convert_to_dashed_string("Hello, World!"))  # Output: "hello-world"
print(convert_to_dashed_string("Python@3.9 is great"))  # Output: "python39-is-great"
print(convert_to_dashed_string("   Spaces    everywhere   "))  # Output: "spaces-everywhere"
print(convert_to_dashed_string("123 456 789"))  # Output: "123-456-789"
print(convert_to_dashed_string("MixED cAsE & Special!!"))  # Output: "mixed-case-special"

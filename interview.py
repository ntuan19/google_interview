# You are given a string that supposedly represents a phone number. Convert it to a standardized format including country code.
# For example, "(475) 777-0132" => "+14757770132"
# You may throw an error if you believe the input string does not correspond to a valid phone number. 
# For simplicity, you can assume that the country code should always be "+1".

# You are allowed to use any resources you want - Google, ChatGPT, Copilot, etc.

# Context: 
# There is a text field on an external website where a user is told to input a phone number.
#  The text field has no built in checking to determine that the phone number is valid,
#   and does not currently do any processing to standardize the text in any way -
#    it stores the user's input exactly as raw text. We do an API call to get the phone number 
#    from this website, and we would like to send a text to this phone number, but in order to call our separate API to do so, we need 
#    the user's phone number in a standardized format (e.g. "+14757770132").

'''
firstly, we need a libary that basically would remove all the (,* and only keep the number. 
-> join all the number together. 
Once we have all the numbers, then check the length of the number, if the number is larger than expected length, the throw an error => "Length is more than expected"
If the length is smaller than expected length => throw "Length is smaller than expected". 

Ex: "+ 2fswsdwd 2332323" => remove 


Write me a difrferent test cases with input as such:

empty_case = "" -> empty value 
number_larger_than_expected = " 232342242424242" => larger than expected 
number_smaller_than_expected = " 2442"
scrappy_number_with_characters = "+fsfsf 1212121"

second_scrappy_number_with_characters = "+fsfs1ff2wesd1+)()"

12344645545
 []
'''
import re

def validate_and_process_number(input_string, expected_length):
    if len(input_string) == 0:
        raise ValueError("Empty value")
    
    # Check if the input starts with "+1" and remove it
    if input_string.startswith("+1"):
        input_string = input_string[2:]
    
    # Step 1: Remove all non-numeric characters
    numbers_only = ''.join(re.findall(r'\d', input_string))
    #If the length is 11 and the number starts with 1. 
    #then we can just return "+" + numbers_only
    if len(numbers_only) == 1 and numbers_only[0] == "1":
        return "+" + numbers_only
    
    # Step 2: Check the length of the processed number
    if len(numbers_only) > expected_length:
        raise ValueError("Length is more than expected")
    elif len(numbers_only) < expected_length:
        raise ValueError("Length is smaller than expected")
    
    # Return the processed number if it's the correct length
    return "+1" + numbers_only



def test_function():
    #Working test case 
    try:
        result = validate_and_process_number("+12345678910", 10)
        assert result == "+12345678910", "Working test case 1 failed: Expected +1234567891"
    except ValueError as e:
        raise AssertionError(f"Working test case 1 failed with error: {e}")
    #Working test case 
    try:
        result = validate_and_process_number("12345678910", 10)
        assert result == "+12345678910", "Working test case 1 failed: Expected +1234567891"
    except ValueError as e:
        raise AssertionError(f"Working test case 1 failed with error: {e}")


    # Working test case 2: Valid input without "+1" prefix
    try:
        result = validate_and_process_number("2345678910", 10)
        assert result == "+12345678910", "Working test case 2 failed: Expected +12345678910"
    except ValueError as e:
        raise AssertionError(f"Working test case 2 failed with error: {e}")
    
    #Working test case with characer:

    # Working test case 2: Valid input without "+1" prefix
    try:
        result = validate_and_process_number("2345dsdsd678910abdce", 10)
        assert result == "+12345678910", "Working test case 2 failed: Expected +12345678910"
    except ValueError as e:
        raise AssertionError(f"Working test case 3 failed with error: {e}")
    # Working test case 2: Valid input without "+1" prefix
    try:
        result = validate_and_process_number("(23456)78910abdce", 10)
        assert result == "+12345678910", "Working test case 2 failed: Expected +12345678910"
    except ValueError as e:
        raise AssertionError(f"Working test case 3 failed with error: {e}")
     # Working test case 2: Valid input without "+1" prefix
    try:
        result = validate_and_process_number("234-567-8910", 10)
        assert result == "+12345678910", "Working test case 2 failed: Expected +12345678910"
    except ValueError as e:
        raise AssertionError(f"Working test case 3 failed with error: {e}")
    # Test Case: Empty Case
    try:
        validate_and_process_number("", 10)
    except ValueError as e:
        assert str(e) == "Empty value"
    
    # Test Case: Number Larger Than Expected
    try:
        validate_and_process_number(" 232342242424242", 10)
    except ValueError as e:
        assert str(e) == "Length is more than expected"

    # Test Case: Number Smaller Than Expected
    try:
        validate_and_process_number(" 2442", 10)
    except ValueError as e:
        assert str(e) == "Length is smaller than expected"

    # Test Case: Scrappy Number With Characters
    try:
        validate_and_process_number("+fsfsf 1212121", 10)
    except ValueError as e:
        assert str(e) == "Length is smaller than expected"

    # Test Case: Second Scrappy Number With Characters
    try:
        validate_and_process_number("+fsfs1ff2wesd1+)()", 10)
    except ValueError as e:
        assert str(e) == "Length is smaller than expected"

    # Test Case: Additional Test Case 1
    result = validate_and_process_number("+1 4232324232", 10)
    assert result == "+14232324232"

    # Test Case: Additional Test Case 2
    try:
        validate_and_process_number("+1 dadadada3434343", 10)
    except ValueError as e:
        assert str(e) == "Length is smaller than expected"
    try:
        validate_and_process_number(" - ) +", 10)
    except ValueError as e:
        assert str(e) == "Length is smaller than expected"

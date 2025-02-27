def number_to_words(n):
    # Dictionary for numbers from 0 to 19
    num_to_words = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 
        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
        15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
    }

    # Dictionary for multiples of 10 (20, 30, ..., 90)
    tens = {
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 
        60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
    }

    # Dictionary for large number units
    powers_of_ten = {
        100: "Hundred", 
        1000: "Thousand", 
        1000000: "Million", 
        1000000000: "Billion"
    }

    # Base case: If the number is in num_to_words, return directly
    if n in num_to_words:
        return num_to_words[n]
    
    # Handle numbers from 20 to 99
    elif n < 100:
        tens_part, ones_part = divmod(n, 10)
        return tens[tens_part * 10] + ("-" + num_to_words[ones_part] if ones_part else "")

    # Handle numbers from 100 to 999
    elif n < 1000:
        hundreds_part, remainder = divmod(n, 100)
        return num_to_words[hundreds_part] + " " + powers_of_ten[100] + (
            " " + number_to_words(remainder) if remainder else ""
        )

    # Handle large numbers (1000, 1 million, 1 billion, etc.)
    else:
        for power in [1000000000, 1000000, 1000]:  # Billion → Million → Thousand
            if n >= power:
                major_part, remainder = divmod(n, power)
                return number_to_words(major_part) + " " + powers_of_ten[power] + (
                    " " + number_to_words(remainder) if remainder else ""
                )

# ✅ Input from user
num = int(input("Enter a number: "))
print("Output:", number_to_words(num))

def safe_divide(numerator, denominator):
    try:
         num = float(numerator)
         den = float(denominator)

         division= num/den
         return(f"The result of the division is {division}")
    except ZeroDivisionError:
         return("Error: Cannot divide by zero")
    except ValueError:
         return("Error: Please enter numeric values only")

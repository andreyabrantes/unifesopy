# 1- Write a program that reads a sequence of numbers and displays their sum.

def main() -> None:
    quantity_sum: int = int(input("Please, enter the quantity of numbers you want to sum: "))
    if quantity_sum < 0: 
        print("Please, enter a valid number")
    
    else: 
        result: int = 0 
        i: int = 0
        
        while i < quantity_sum:
            read_number: int = int(input(f"Please, enter number {i+1}: "))
            result = result + read_number
            i = i + 1
        
        print (f"The sum of the entered numbers is {result}")
    
if __name__ == "__main__":
    main()
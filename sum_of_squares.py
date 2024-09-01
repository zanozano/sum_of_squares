def sum_of_squares(numbers):
    if not numbers:
        return 0
    return (numbers[0] ** 2 if numbers[0] >= 0 else 0) + sum_of_squares(numbers[1:])

def process_cases(num_cases):
    if num_cases == 0:
        return []
    
    num_elements = int(input().strip())
    
    numbers = list(map(int, input().strip().split()))
    
    result = sum_of_squares(numbers)
    
    return [result] + process_cases(num_cases - 1)

def main():
    num_cases = int(input().strip())
    
    results = process_cases(num_cases)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()

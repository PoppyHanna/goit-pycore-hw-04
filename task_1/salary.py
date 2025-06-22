# import os
# print(os.getcwd())
  
def total_salary(path):
    total = 0
    count = 0

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    salary = float(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    continue    
    if count == 0:
        return 0, 0
    average = total / count
    return round(total), round(average)           
total, average = total_salary("salaries.txt")
print(f"Загальна сума: {total}, Середня: {average}")
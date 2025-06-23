# import os
# print(os.getcwd())
  
def total_salary(path):
    total = 0
    count = 0

    try:
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
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return 0, 0
    
    if count == 0:
        return 0, 0
    average = total / count
    return round(total), round(average)
total, average = total_salary("task_1/salaries.txt")
print(f"Загальна сума: {total}, Середня: {average}")
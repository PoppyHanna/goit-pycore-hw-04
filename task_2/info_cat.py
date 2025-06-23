def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_dict = {'id': cat_id, 'name': name, 'age': age}
                    cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    return cats_list

cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)
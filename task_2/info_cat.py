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
        print(f"File '{path}' not found")
    except Exception as e:
        print(f"An error occurred while reading file: {e}")
    return cats_list

cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)
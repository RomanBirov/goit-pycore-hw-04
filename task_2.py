def get_cats_info(path: str):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  
                
                try:
                    cat_id, name, age = line.split(",")
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_list.append(cat_dict)
                except ValueError:
                    print(f"ERROR: Not valide line: {line}")
                    continue

        return cats_list

    except FileNotFoundError:
        print("ERROR:File not found")
        return []
    except Exception as e:
        print(f"ERROR:File not read {e}")
        return []

# test function
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
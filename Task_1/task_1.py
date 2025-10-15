def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()
                if not line:
                    continue 
                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1

                except ValueError:
                    print(f"ERROR: Not valide line: {line}")
                    continue

            if count == 0:
                return (0, 0)

            average = total // count
            return total, average

    except FileNotFoundError:
        print(f"ERROR:File not found")
        return (0, 0)
    except Exception as e:
        print(f"ERROR:File not read {e}")
        return (0, 0)
    

total, average = total_salary("Task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
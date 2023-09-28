
list_problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
quantity_list_problems = len(list_problems)

num1 = None
operand = ""
num2 = None
result = None

dashes = "----"

num1_list = []
operand_list = []
num2_list = []
dashes_list = []
result_list = []

for i in range(quantity_list_problems):
    if "+" in list_problems[i]:
        extract_numbers = list_problems[i].split(" + ")

        num1 = extract_numbers[0]
        operand = "+"
        num2 = extract_numbers[1]
        result = int(extract_numbers[0]) + int(extract_numbers[1])

        len_result = len(str(result))

        if len_result > 3:
            dashes += "-" * (len_result - len(dashes))

        num1_list.append(num1)
        operand_list.append(operand)
        num2_list.append(num2)
        dashes_list.append(dashes)
        result_list.append(str(result))

    elif "-" in list_problems[i]:
        extract_numbers = list_problems[i].split(" - ")

        num1 = extract_numbers[0]
        operand = "-"
        num2 = extract_numbers[1]
        result = int(extract_numbers[0]) - int(extract_numbers[1])

        if len_result > 3 or len_result:
            dashes += "-" * (len_result - len(dashes))

        num1_list.append(num1)
        operand_list.append(operand)
        num2_list.append(num2)
        dashes_list.append(dashes)
        result_list.append(str(result))

print(num1_list, operand_list, num2_list, dashes_list, result_list)

quantity_list_others = len(num1_list)

for i in range(quantity_list_others):
    print(f"{num1_list[i]:>{10}}", end=" ")
print()

for i in range(quantity_list_others):
    print(f"   {operand_list[i]} {num2_list[i]:>{5}}", end=" ")
print()

for i in range(quantity_list_others):
    print(f"{dashes_list[i]:>{10}}", end=" ")
print()

for i in range(quantity_list_others):
    print(f"{result_list[i]:>{10}}", end=" ")
print()

















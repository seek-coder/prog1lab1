#Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

def arithmetic_arranger(list_problems: list, flag: bool) -> str:
    if type(list_problems) is list:
        quantity = len(list_problems)
        for i in range(quantity):
            if " + " in list[i]:
                splited_string = list[i].split(" + ")
    print(splited_string)

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\n 请输入姓: ")
    if first == 'q':
        break
    last = input("请输入名: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\t名字是: " + formatted_name + '.')
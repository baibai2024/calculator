def find_xy_combinations_a(n):
    # Function to find combinations for x + y = n
    # 用于查找满足 x + y = n 的组合的函数
    combinations = []
    for i in range(n+1):
        for j in range(n+1):
            if i+j == n:
                combinations.append((i, j))
    return combinations


def find_xy_combinations_b(n):
    # Function to find combinations for x * y = n
    # 用于查找满足 x * y = n 的组合的函数
    combinations = []
    for i in range(n+1):
        for j in range(n+1):
            if i*j == n:
                combinations.append((i, j))
    return combinations


def find_xy_combinations_c(n):
    # Function to find combinations for x / y = n
    # 用于查找满足 x / y = n 的组合的函数
    combinations = []
    for i in range(n+1):
        for j in range(n+1):
            try:
                if int(i/j) == n:
                    combinations.append((i, j))
            except ZeroDivisionError:
                pass
    return combinations


def find_xy_combinations_d(n):
    # Function to find combinations for x - y = n
    # 用于查找满足 x - y = n 的组合的函数
    combinations = []
    for i in range(n+1):
        for j in range(n+1):
            if i-j == n:
                combinations.append((i, j))
    return combinations


a = int(input("Enter a number a: "))  # 用户输入一个数字 a>0 / The user inputs a number, a>0

with open('main.txt', 'w') as f:
    f.write("# Hello\n")
    f.write("num1 = int(input('Enter num1:'))\n")  # Prompt user to enter num1 / 翻译成中文是 "提示用户输入 num1
    f.write("fu = input('Enter operation (+-*/):')\n")  # Prompt user to enter the operation / 提示用户输入运算符
    f.write("num2 = int(input('Enter num2:'))\n")  # Prompt user to enter num2 / 提示用户输入 num2

    for i in range(a+1):
        # Generate conditions for x + y = n/生成方程 x + y = n 的条件
        conditions_a = [f"num1 == {j[0]} and num2 == {j[1]} and fu == '+'" for j in find_xy_combinations_a(i)]
        # Generate conditions for x * y = n/生成方程 x * y = n 的条件
        conditions_b = [f"num1 == {j[0]} and num2 == {j[1]} and fu == '*'" for j in find_xy_combinations_b(i)]
        # Generate conditions for x / y = n/生成方程 x / y = n 的条件
        conditions_c = [f"num1 == {j[0]} and num2 == {j[1]} and fu == '/'" for j in find_xy_combinations_c(i)]
        # Generate conditions for x - y = n/生成方程 x - y = n 的条件
        conditions_d = [f"num1 == {j[0]} and num2 == {j[1]} and fu == '-'" for j in find_xy_combinations_d(i)]

        # Combine all conditions/合并所有条件
        all_conditions = conditions_a + conditions_b + conditions_c + conditions_d

        for condition in all_conditions:
            f.write(f"if {condition}:\n")  # Check each condition/检查每个条件
            f.write(f"    print('{i}')\n")  # Print the result if the condition is true/如果条件为真，则打印结果

# !!! x+y=n 0<x<=n 0<y<=n 0<n<=n
# !!! x*y=n 0<x<=n 0<y<=n 0<n<=n
# !!! x/y=n 0<x<=n 0<y<=n 0<n<=n
# !!! x-y=n 0<x<=n 0<y<=n 0<n<=n
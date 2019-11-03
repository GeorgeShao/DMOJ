input_text = input().split()

operations = ["+", "-", "*", "/", "%", "^"]

def operate(text):
    # print(text)
    if len(text) > 1:
        op_index = 0
        op_type = 0
        new_num = 0
        for each in text:
            if each in operations:
                op_index = text.index(each)
                op_type = each
                break
        num1 = float(text[op_index-2])
        num2 = float(text[op_index-1])
        if op_type == "+":
            new_num = num1 + num2
        elif op_type == "-":
            new_num = num1 - num2
        elif op_type == "*":
            new_num = num1 * num2
        elif op_type == "/":
            new_num = num1 / num2
        elif op_type == "%":
            new_num = num1 % num2
        elif op_type == "^":
            new_num = num1 ** num2
        text[op_index] = new_num
        del text[op_index-1]
        del text[op_index-2]
        operate(text)
    else:
        print(text[0])

operate(input_text)
def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    string_stack = []
    opening_bracs = ['(','{','[']
    closing_bracs = [')','}',']']
    for char in s:
        if char in opening_bracs:
            string_stack.append(char)
        elif char in closing_bracs and len(string_stack) == 0:
                return False
        else:
            for value in string_stack:
                if char == ')' and string_stack[-1] == '(':
                    string_stack.pop()
                    break
                if char == ']' and string_stack[-1] == '[':
                    string_stack.pop()
                    break
                if char == '}' and string_stack[-1] == '{':
                    string_stack.pop()
                    break
                else:
                    return False
    if len(string_stack) == 0:
        return True
    else:
        return False
    
s = r"(([]){})"#"([])"#r"([}}])"
print(isValid(s))

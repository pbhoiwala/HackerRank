# https://www.hackerrank.com/challenges/balanced-brackets/

n = int(input())

def get_top():
    if stack: return stack[-1]
    return None

for _ in range(n):
    s = input()
    stack = []
    for b in s:
        if b == '(' or b == '{' or b == '[':
            stack.append(b)
        else:
            top = get_top()
            if (top == '(' and b == ')' or 
                top == '{' and b == '}' or
                top == '[' and b == ']' ): 
                    stack.pop()
            else:
                stack.append(b)
                break
    print("YES" if not stack else "NO")

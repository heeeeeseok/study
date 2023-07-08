rank = {'(': 0, '*': 1, '/': 1, '+': 2, '-': 2}

def solution(expr):
    answer = ''
    stack = []
    for semantic in expr:
        if semantic in ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                             'H', 'I', 'J', 'K', 'L', 'M', 'N',
                             'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                             'V', 'W', 'X', 'Y', 'Z']:
            answer += semantic
            continue
        elif semantic in ['+', '-', '*', '/']:
            if not stack or stack[-1] == '(':
                stack.append(semantic)
            elif rank[semantic] >= rank[stack[-1]]:
                while stack and stack[-1] != '(' and rank[semantic] >= rank[stack[-1]]:
                    answer += stack.pop()
                stack.append(semantic)
            else:
                stack.append(semantic)
        elif semantic == '(':
            stack.append(semantic)
        elif semantic == ')':
            while True:
                element = stack.pop()
                if element == '(':
                    break
                else:
                    answer += element
    while len(stack) > 0:
        answer += stack.pop()

    return answer


if __name__=='__main__':
    print(solution(input()))

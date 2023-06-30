def is_all_zeros(input_string):
    return all(char == '0' for char in input_string)

def partition(b_string):
    if len(b_string) == 1:
        return 1

    if is_all_zeros(b_string):
        return 1

    half = len(b_string) // 2
    if b_string[half] != '1':
        return 0

    return partition(b_string[:half]) & partition(b_string[half + 1:])


def solution(numbers):
    answer = []

    for number in numbers:
        b_string = format(number, 'b')
        b_size = len(b_string)

        i = 1
        while b_size > pow(2, i) - 1:
            i += 1

        total_size = pow(2, i) - 1
        attach_zero = ''
        for i in range(0, total_size - len(b_string)):
            attach_zero += '0'
        b_string = attach_zero + b_string

        answer.append(partition(b_string))
    return answer


if __name__=='__main__':
    print(solution([1, 2, 10]))
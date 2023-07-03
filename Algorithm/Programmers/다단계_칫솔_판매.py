def solution(enroll, referral, seller, amount):
    answer = []
    dic_enroll = {}

    for i in range(len(enroll)):
        dic_enroll[enroll[i]] = [referral[i], 0]

    def division(current_seller, money):
        if current_seller == "-":
            return

        money_to_send = money // 10
        if money_to_send == 0:
            dic_enroll[current_seller][1] += money
            return
        else:
            division(dic_enroll[current_seller][0], money_to_send)
            dic_enroll[current_seller][1] += (money - money_to_send)

    for i in range(len(seller)):
        division(seller[i], amount[i]*100)

    for i in range(len(enroll)):
        answer.append(dic_enroll[enroll[i]][1])

    return answer

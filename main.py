import random


class WheelNumber:
    def __init__(self, number, odd,winamount):
        self.number = number
        self.odd = odd
        self.winamount = winamount


class Bet:
    def __init__(self, wheel_nubmer, betamount):
        self.wheel_nubmer = wheel_nubmer
        self.betamount = betamount


num1 = WheelNumber(1,0.48,2)
num3 = WheelNumber(3,0.24,4)
num5 = WheelNumber(5,0.16,6)
num10 = WheelNumber(10,0.08,11)
num20 = WheelNumber(20,0.04,21)

numberList = [num1,num3,num5,num10,num20]
numbersList = [1,3,5,10,20]

def spinWheel(bets):
    wonNumber = random.choices(numbersList, weights=(numberList[0].odd, numberList[1].odd, numberList[2].odd, numberList[3].odd, numberList[4].odd),k=1)[0]
    for bet in bets:
        if bet.wheel_nubmer.number == wonNumber:
            return wonNumber,bet.wheel_nubmer.winamount * bet.betamount
    return wonNumber, 0

start_amount = 50000

all_count = 100000
for betnumber in numberList:
    
    operations = 0
    
    results = []
    
    for i in range(all_count):
        operations = 0
        total = start_amount
        while True:
            bet_amount = int(2 ** operations)
            operations +=1
            if bet_amount > total:
                #print(i,":","Not enough scrap:",total,"| Needed",bet_amount,"-----","Total operations:", operations)
    
                results.append(total)
                break
            else:
                total -= bet_amount
                bet_number = betnumber
                wonNumber,winnigs = spinWheel([Bet(bet_number,bet_amount)])
                """
                print("BET:",bet_amount,"ON",bet_number.number)
                print("SPIN:",i)
                print("Number won:",wonNumber)
                print(f"Total:{total}+{winnigs}={total+winnigs}")
                """
                total+= winnigs
                #print("-----")
                if winnigs > 0:
                    results.append(total)
                    #print(i,":","Won and left with",total,"which is",round(total/start_amount*100-100,8),"% more")
                    break
    print("--------")
    print("BETTING ON", betnumber.number)
    print()
    results = sorted(results)
    lost = []
    lost_count = 0
    
    won = []
    win_count = 0
    for i in range(len(results)):
        if results[i] > start_amount:
            win_count +=1
            won.append(results[i])
        else:
            lost_count+=1
            lost.append(results[i])
    
    print("Won in:",win_count)
    print("Lost in:",lost_count)
    risk = lost_count/all_count
    print("Risk percentage:", round(risk*100,3),"%")
    #print(results)
    print()
    avg_won = sum(won)/len(won) -start_amount
    print("Average won amount: ",avg_won)
    print("Max win: ",max(won)-start_amount)
    print()
    avg_lost = start_amount - sum(lost)/len(lost)
    print("Average lost amount: ", avg_lost)
    print("Max lost:",start_amount-min(lost))

    probability_of_winning = win_count / all_count
    probability_of_losing = lost_count / all_count
    ev = (probability_of_winning * avg_won) + (probability_of_losing * -avg_lost)
    print("Expected Value (EV): ", ev)

    max_loss = start_amount - min(lost)
    worth_coefficient = ev / max_loss
    print("Worth Coefficient: ", worth_coefficient)
    print()
    #print("WORTH COOFICIENT:", ((1/(risk*100)))*(avg_won/avg_lost),"%")
    #print((1/(risk*100)))
    #print(avg_won/avg_lost)
    #exit()
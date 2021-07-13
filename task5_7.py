import json

dict_of_firm = {}
average_profit = {'average_profit': 0}
with open('data5_7.txt', 'r') as f:
    for line in f:
        data = line.strip().split('   ')
        dict_of_firm[data[0]] = float(data[-2]) - float(data[-1])
    profit_sum = [elem for elem in dict_of_firm.values() if elem > 0]
    average_profit['average_profit'] += round(sum(profit_sum) / len(profit_sum), 2)

with open('data5_7.json', 'w') as f:
    json.dump([dict_of_firm, average_profit], f, ensure_ascii=False)

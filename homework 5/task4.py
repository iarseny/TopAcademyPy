def get_pay(cost):
    if cost < 500:
        return cost * 1.03
    elif 500 <= cost <= 1000:
        return cost * 1.05
    elif cost > 1000:
        return cost * 1.08
    else:
        return cost

cost1 = int(input())
cost2 = int(input())
cost3 = int(input())

costs = [get_pay(cost1) + 200, get_pay(cost2) + 200, get_pay(cost3) + 200]

print(max(costs))
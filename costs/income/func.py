def prepare(qs):
    d = dict()
    for obj in qs:
        acc, price = obj.account, obj.price
        if price == '':
            price = 0
        d[acc] = d.get(acc, 0) + price
    return d


def summarize(qs):
    d = dict()
    for obj in qs:
        acc_id, sm, bal = obj.account, obj.price, obj.balance
        if sm == '':
            sm = 0
        bal += sm
        d[acc_id] = d.get(acc_id, 0) + bal
    return d


def balances(d1, d2):
    d = dict()
    for acc_id in set(list(j for j in d1.keys())):
        d[acc_id] = d1.get(acc_id, 0) - d2.get(acc_id, 0)
    for acc_id in set(list(j for j in d2.keys())):
        d[acc_id] = d1.get(acc_id, 0) - d2.get(acc_id, 0)
    return dict(sorted(d.items()))


def parser(qs1, qs2):
    d = dict()
    bal = 0
    prev = -1
    tempgoal = ''
    temptitle = ''
    for obj in qs1:
        acc_id, sm, goal, goal_title = obj.account, obj.price, obj.goal, obj.goal_title
        if acc_id != prev:
            bal = 0
            prev = acc_id
        bal += sm
        if goal is None:
            if sm != 0:
                d[acc_id] = [bal, tempgoal, temptitle]
            else:
                d[acc_id] = [bal, '', '']
        else:
            tempgoal = goal
            temptitle = goal_title
            d[acc_id] = [bal, goal, goal_title]
    bal = 0
    for obj in qs2:
        acc_id, sm = obj.account, obj.price
        if sm == '':
            sm = 0
        bal -= sm
        if acc_id not in d.keys():
            d[acc_id] = [0, '', '']
        d[acc_id][0] += bal
        bal = 0
    return dict(sorted(d.items()))



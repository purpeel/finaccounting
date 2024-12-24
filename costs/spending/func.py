def prepare(qs):
    d = dict()
    for obj in qs:
        cat, price = obj.category, obj.price
        d[cat] = d.get(cat, 0) + price
    return d


def summarize(qs):
    d = dict()
    prev = -1
    for obj in qs:
        acc_id, sm, bal = obj.account, obj.price, obj.balance
        if sm == '':
            sm = 0
        bal += sm
        if prev != acc_id:
            d[acc_id] = d.get(acc_id, 0) + bal
    return d
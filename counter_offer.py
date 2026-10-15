
def counter_offer(listed_price, buyer_offer, floor_price):
    if buyer_offer >= listed_price:
        return {"action": "accept", "price": buyer_offer}

    if buyer_offer < floor_price:
        return {"action": "counter", "price": floor_price}

    midpoint = (listed_price + buyer_offer) / 2
    return {"action": "counter", "price": round(midpoint, 2)}


print(counter_offer(100, 85, 80))
print(counter_offer(100, 70, 80))
print(counter_offer(100, 100, 80))

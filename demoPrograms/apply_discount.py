def apply_discount(product,discount):
    price = int(product['price']*(1.0 - discount))
    assert 0 <= price <= product['price']
    return price

res = apply_discount({"name":"pencil", "price": 5.00},0.1)
print(res)

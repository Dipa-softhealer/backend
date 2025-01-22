def apply_discount(product,discount):
    price = int(product['price']*(1.0 - discount))
    assert 0 <= price <= product['price']
    return price

res = apply_discount({"name":"pencil", "price": 5.00},0.1)
print(res)

# demo : just testing backspace
print("hello \b World")

# demo : just testing the form feed
print("Dipa \f Chiniya".casefold())
print(type('\f'))

# octal to text
print('\144\151\160\141\134')

# center method trial for string
print("rooftop".center(984,"/"))
print("".center(369,"|"))


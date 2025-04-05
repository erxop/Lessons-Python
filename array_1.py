products = ["pepsi", "diapers", "mentos"]
print(products)

products.extend(["beverages", "noodles", "detergent", "clippers", "bodyspray"])
print(products)
print(len(products))

products.pop(4)
print(products)

products.pop(5)
print(products)

list_products = ["pepsi", "diapers", "mentos", "beverages", "detergent", "bodyspray"]
tuple_products = tuple(list_products)
print(tuple_products)
print(type(tuple_products))



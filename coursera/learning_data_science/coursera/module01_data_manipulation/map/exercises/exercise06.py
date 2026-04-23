# Filtrar apenas os produtos com preço maior que 1000.
# Aplicar um desconto de 10% nesses produtos usando map().
# Somar todos os preços finais usando reduce().

from functools import reduce

products = [
    {"name": "TV", "price": 1800},
    {"name": "Notebook", "price": 3500},
    {"name": "Mouse", "price": 80},
    {"name": "Tablet", "price": 1200},
    {"name": "Cadeira Gamer", "price": 900},
]

filtered_and_discounted_products = list(
    map(
        lambda price: price["price"] * 0.9,
        filter(lambda p: p["price"] > 1000, products)
    )
)

final_value = reduce(lambda acc, price: acc + price, filtered_and_discounted_products)
print(f"The final value is R${final_value:.2f} ")
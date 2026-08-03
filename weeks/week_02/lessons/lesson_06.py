product = {
    "name": "Monitor",
    "price": 149.90,
    "stock": 8,
    "available": True
}

print("--- Produto inicial ---")
print(f"Nome: {product['name']}")
print(f"Preço: {product['price']:.2f} €")
print(f"Stock: {product['stock']}")

quantity_sold = int(input("\nQuantidade vendida: "))

if quantity_sold <= 0:
    print("Quantidade inválida.")

elif quantity_sold > product["stock"]:
    print("Stock insuficiente.")

else:
    product["stock"] -= quantity_sold

    if product["stock"] == 0:
        product["available"] = False

    print()
    print("--- Produto atualizado ---")

    for key, value in product.items():
        print(f"{key}: {value}")
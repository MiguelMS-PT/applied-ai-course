product_name = input("Produto: ")
price = float(input("Preço: "))
discount = float(input("Desconto: "))



if price <= 0:
    print(f"Preço: {price}")
    print("Preço inválido.")

elif discount < 0:
    print(f"Desconto: {discount}")
    print("Desconto inválido.")
elif discount > 100:
    print(f"Desconto: {discount}")
    print("Desconto inválido.")
else:
    discount_value = price * (discount/100)
    final_price = price - discount_value
    print()
    print(f"Produto: {product_name}")
    print(f"Preço original: {price:.2f} €")
    print(f"Desconto: {discount:.2f}%")
    print(f"Preço final: {final_price:.2f} €")

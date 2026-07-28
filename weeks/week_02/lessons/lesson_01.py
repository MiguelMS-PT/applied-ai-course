product_name = input("Nome do produto: ")
unit_price = float(input("Preço unitário: "))
quantity = int(input("Quantidade comprada: "))
stock = int(input("Stock disponível: "))

if quantity <= 0:
    print()
    print("Erro: a quantidade tem de ser superior a zero.")

elif quantity > stock:
    print()
    print("Erro: stock insuficiente.")
    print(f"Quantidade pedida: {quantity}")
    print(f"Stock disponível: {stock}")

else:
    subtotal = unit_price * quantity
    stock -= quantity

    print()
    print("--- Encomenda aceite ---")
    print(f"Produto: {product_name}")
    print(f"Quantidade: {quantity}")
    print(f"Subtotal: {subtotal:.2f} €")
    print(f"Stock restante: {stock}")

    
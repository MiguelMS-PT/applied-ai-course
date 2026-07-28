product_name = input("Produto: ")
price = float(input("Preço: "))
quantity = int(input("Quantidade: "))
stock = int(input("Stock: "))
discount = float(input("Desconto (%): "))

has_valid_price = price > 0
has_valid_quantity = quantity > 0
has_enough_stock = quantity <= stock
has_valid_discount = 0 <= discount <= 100

can_purchase = (
    has_valid_price
    and has_valid_quantity
    and has_enough_stock
    and has_valid_discount
)

if can_purchase:
    subtotal = price * quantity
    discount_value = subtotal * (discount / 100)
    final_price = subtotal - discount_value
    stock -= quantity

    print()
    print("--- Encomenda aceite ---")
    print(f"Produto: {product_name}")
    print(f"Preço final: {final_price:.2f} €")
    print(f"Stock restante: {stock}")

else:
    print()
    print("--- Encomenda rejeitada ---")

    if not has_valid_price:
        print("Motivo: preço inválido.")

    if not has_valid_quantity:
        print("Motivo: quantidade inválida.")

    if not has_enough_stock:
        print("Motivo: stock insuficiente.")

    if not has_valid_discount:
        print("Motivo: desconto inválido.")
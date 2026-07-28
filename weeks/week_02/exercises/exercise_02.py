product_name = input("Produto: ")
price = float(input("Preço: "))
quantity = int(input("Quantidade: "))
stock = int(input("Stock: "))
discount = float(input("Desconto (%): "))

is_possible_price = price > 0
is_quantity_validy = quantity > 0
is_quantity_available = quantity <= stock
is_discount_possible = discount >= 0 and discount <= 100

can_buy = (
    is_discount_possible
    and is_possible_price
    and is_quantity_available
    and is_quantity_validy
)

if can_buy:
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

    if not is_possible_price:
            print("Motivo: preço inválido.")
    
    if not is_quantity_validy:
            print("Motivo: quantidade inválida.")
    
    if not is_quantity_available:
            print("Motivo: stock insuficiente.")
    
    if not is_discount_possible:
            print("Motivo: desconto inválido.")
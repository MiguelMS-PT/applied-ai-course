product = input("Nome do produto:")
unit_price = float(input("Preço unitário:"))
quantity = int(input("Quantidade comprada:"))
discount = float(input("Desconto (%):"))
stock = int(input("Stock inicial:"))

subTotal = unit_price * quantity
discount_value = subTotal * (discount/100)
final_price = subTotal - discount_value
stock -= quantity

print()
print("--- Resumo da encomenda ---")
print(f"Produto: {product}")
print(f"Preço unitário: {unit_price:.2f} €")
print(f"Quantidade comprada: {quantity}")
print(f"Subtotal: {subTotal:.2f} €")
print(f"Desconto: {discount:.2f}%")
print(f"Valor do desconto: {discount_value:.2f} €")
print(f"Preço final: {final_price:.2f} €")
print(f"Stock restante: {stock}")

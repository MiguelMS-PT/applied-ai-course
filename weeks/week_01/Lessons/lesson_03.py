product_name = input("Produto: ")
unit_price = float(input("Preço unitário: "))
quantity = int(input("Quantidade comprada: "))
discount_percentage = float(input("Desconto (%): "))
initial_stock = int(input("Stock inicial: "))

subtotal = unit_price * quantity
discount_value = subtotal * (discount_percentage / 100)
final_price = subtotal - discount_value
remaining_stock = initial_stock - quantity

print()
print("--- Resumo da compra ---")
print(f"Produto: {product_name}")
print(f"Preço unitário: {unit_price:.2f} €")
print(f"Quantidade: {quantity}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Desconto: {discount_percentage:.2f}%")
print(f"Valor do desconto: {discount_value:.2f} €")
print(f"Preço final: {final_price:.2f} €")
print(f"Stock restante: {remaining_stock}")
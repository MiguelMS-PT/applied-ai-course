product_name = "Rato sem fios"
unit_price = 24.99
quantity = 3
discount_percentage = 10

subtotal = unit_price * quantity
discount_value = subtotal * (discount_percentage / 100)
final_price = subtotal - discount_value

print(f"Produto: {product_name}")
print(f"Preço unitário: {unit_price:.2f} €")
print(f"Quantidade: {quantity}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Desconto: {discount_percentage}%")
print(f"Valor do desconto: {discount_value:.2f} €")
print(f"Preço final: {final_price:.2f} €")
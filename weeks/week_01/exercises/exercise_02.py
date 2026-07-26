product = "Auscultadores"
price = 39.90
quantity = 3
discount = 15
stock = 20

sub_total = price * quantity

discount_value =  sub_total * (discount / 100)

final_price = sub_total - discount_value

stock -= quantity

print(f"Produto: {product}")
print(f"Preço unitário: {price:.2f} €")
print(f"Quantidade comprada: {quantity}")
print(f"Subtotal: {sub_total:.2f} €")
print(f"Desconto: {discount}%")
print(f"Valor do desconto: {discount_value:.2f} €")
print(f"Preço final: {final_price:.2f} €")
print(f"Stock restante: {stock}")


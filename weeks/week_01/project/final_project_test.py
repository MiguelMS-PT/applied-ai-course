product_name = input("Nome do produto: ")
unit_price = float(input("Preço unitário: "))
quantity = int(input("Quantidade comprada: "))
discount = float(input("Desconto (%): "))
iva = float(input("IVA (%): "))
stock = int(input("Stock inicial: "))

subtotal = unit_price * quantity
discount_value = subtotal * (discount/100)
price_discount = subtotal - discount_value
iva_value = price_discount * (iva/100)
final_price = price_discount + iva_value
stock -= quantity

print()
print(f"Produto: {product_name}")
print(f"Preço unitário: {unit_price:.2f} €")
print(f"Quantidade comprada: {quantity}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Desconto: {discount:.2f}%")
print(f"Valor do desconto: {discount_value:.2f} €")
print(f"Preço depois do desconto: {price_discount:.2f} €")
print(f"IVA: {iva:.2f}%")
print(f"Valor do IVA: {iva_value:.2f} €")
print(f"Preço final: {final_price:.2f} €")
print(f"Stock restante: {stock}")



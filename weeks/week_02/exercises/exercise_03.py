sales_value = 0
number_of_sales = 0
sale_value = float(input("Valor da venda — introduza 0 para terminar: "))


while sale_value != 0:
    if sale_value < 0:
        print("Valor inválido.")
    else:
        sales_value += sale_value
        number_of_sales += 1

        print("Venda registada.")
    print()    
    sale_value = float(input("Valor da venda — introduza 0 para terminar: "))

if number_of_sales > 0:
    sale_average = sales_value / number_of_sales

    print(f"Número de vendas: {number_of_sales}")
    print(f"Total vendido: {sales_value:.2f} €")
    print(f"Média por venda: {sale_average:.2f} €")
else:
    print("Não foram registadas vendas.")
        
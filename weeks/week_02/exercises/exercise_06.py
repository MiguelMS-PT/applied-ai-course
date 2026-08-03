model_name = input("Nome do modelo: ")
company_name = input("Empresa: ")
price_for_tokens = float(input("Preço por 1 milhão de tokens: "))
contex_window = float(input("Context window: "))
active_program = input("Está ativo? ")

while (active_program != "sim") and (active_program != "não"):
    print("Escreva sim ou não")
    active_program = input("Está ativo? ")


is_active = False

if active_program == "sim":
    is_active = True

ai_model = {
    "name": model_name,
    "company": company_name,
    "price": price_for_tokens,
    "context_window": contex_window,
    "active": is_active
}    

print()

for key, value in ai_model.items():
    print(f"{key}: {value}")
ai_model["tested"] = False

ai_model["tested"] = True

print()
for key, value in ai_model.items():
    print(f"{key}: {value}")



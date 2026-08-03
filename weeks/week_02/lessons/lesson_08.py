model_configuration = (
    "GPT-X",
    "OpenAI",
    128000,
    True
)

print("--- Configuração ---")

for value in model_configuration:
    print(value)

print()

model_name, company, context_window, is_active = model_configuration

print(f"Modelo: {model_name}")
print(f"Empresa: {company}")
print(f"Context window: {context_window}")
print(f"Ativo: {is_active}")
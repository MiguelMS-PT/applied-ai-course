correct_code = "AI2026"
attempts_left = 3
is_authenticated = False

while attempts_left > 0 and not is_authenticated:
    entered_code = input("Introduz o código: ")

    if entered_code == correct_code:
        is_authenticated = True
        print("Acesso autorizado.")

    else:
        attempts_left -= 1
        print("Código incorreto.")
        print(f"Tentativas restantes: {attempts_left}")

if not is_authenticated:
    print("Acesso bloqueado.")
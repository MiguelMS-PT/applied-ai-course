aproved_responses = 0
reviewing_responses = 0
rejected_responses = 0
sum_score = 0
highest_score = 0

number_of_responses = int(input("Número de respostas avaliadas: "))
while number_of_responses <= 0:
    print()
    print("Escolha um número válido.")
    number_of_responses = int(input("Número de respostas avaliadas: "))

for response_number in range(1, number_of_responses + 1):
    score = float(input(f"Pontuação da resposta {response_number}: "))
    while score < 0 or score > 100:
        print()
        print("Escolha um valor válido.")
        score = float(input(f"Pontuação da resposta {response_number}: "))

    if highest_score < score:
        highest_score = score
    if score < 50:
        rejected_responses += 1
    elif score < 80 and score >= 50:
        reviewing_responses += 1
    else:
        aproved_responses += 1
    sum_score += score

average_score = sum_score / number_of_responses

print()
print("--- Relatório de qualidade ---")
print(f"Respostas aprovadas: {aproved_responses}")
print(f"Respostas para revisão: {reviewing_responses}")
print(f"Respostas rejeitadas: {rejected_responses}")
print(f"Pontuação média: {average_score:.2f}")
print(f"Maior pontuação: {highest_score:.2f}")

            

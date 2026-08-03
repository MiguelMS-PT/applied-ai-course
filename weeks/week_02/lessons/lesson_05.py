scores = []
number_of_responses = int(input("Número de respostas: "))

for response_number in range(1, number_of_responses + 1):
    score = float(input(f"Pontuação da resposta {response_number}: "))
    scores.append(score)

print()
print(f"Pontuações guardadas: {scores}")
print(f"Número de pontuações: {len(scores)}")

print()
print("--- Pontuações individuais ---")

for score in scores:
    print(f"{score:.2f}")
    
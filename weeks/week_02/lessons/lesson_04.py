number_of_requests = int(input("Número de pedidos testados: "))

total_latency = 0.0
slow_requests = 0
highest_latency = 0.0

for request_number in range(1, number_of_requests + 1):
    latency = float(
        input(f"Latência do pedido {request_number} em ms: ")
    )

    total_latency += latency

    if latency > highest_latency:
        highest_latency = latency

    if latency > 1000:
        slow_requests += 1

average_latency = total_latency / number_of_requests

print()
print("--- Relatório de latência ---")
print(f"Número de pedidos: {number_of_requests}")
print(f"Latência média: {average_latency:.2f} ms")
print(f"Maior latência: {highest_latency:.2f} ms")
print(f"Pedidos lentos: {slow_requests}")
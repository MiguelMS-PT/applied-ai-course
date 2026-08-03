executions_list = []
executions_success = 0
executions_failed = 0
executions_above_1000ms = 0
number_of_executions = int(input("Número de execuções: "))

for execution_number in range(1, number_of_executions +1):
    success = False
    latency = int(input(f"Latência da execução {execution_number}: "))
    did_work = input("Teve sucesso? ")


    while did_work != "sim" and did_work != "nao":
        print("Escreva sim ou nao")
        did_work = input("Teve sucesso? ")


    if did_work == "sim":
        success = True


    execution = (
        execution_number,
        latency,
        success
    )
    executions_list.append(execution)

print()
print("--- Resultados ---")
print(executions_list)
print()

for number_, latency_, success_ in executions_list:
    if latency_ > 1000:
        executions_above_1000ms += 1

    if success_ == True:
        executions_success += 1
    else:
        executions_failed += 1        

print(f"Execuções com sucesso: {executions_success}")
print(f"Execuções falhadas: {executions_failed}")
print(f"Execuções acima de 1000 ms: {executions_above_1000ms}")
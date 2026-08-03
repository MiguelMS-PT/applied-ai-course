rapid_shores = 0
normal_speed_shores = 0
slow_shores = 0
time = []


number_of_shores = int(input("Número de tarefas: "))

for number_shore in range(1, number_of_shores +1):
    shore_time = float(input(f"Tempo da tarefa {number_shore}: "))
    time.append(shore_time)

    if shore_time < 2:
        rapid_shores += 1
    elif shore_time <= 5:
        normal_speed_shores += 1
    else:
        slow_shores += 1


print()
print(f"Tempos registados: {time}")
print(f"Primeiro tempo: {time[0]:.2f} s")
print(f"Último tempo: {time[-1]:.2f} s")
print(f"Tarefas rápidas: {rapid_shores}")
print(f"Tarefas normais: {normal_speed_shores}")
print(f"Tarefas lentas: {slow_shores}")

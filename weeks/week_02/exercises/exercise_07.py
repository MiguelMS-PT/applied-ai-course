access_user_list = []
access_usernames = set()

number_of_access = int(input("Número de acessos: "))



while number_of_access <= 0:
    print()
    print("Número de acessos inválido.")
    number_of_access = int(input("Número de acessos: "))


for access_username in range(1, number_of_access + 1):
    username = input(f"Username do acesso {access_username}: ")
    access_user_list.append(username)
    access_usernames.add(username)


print("--- Relatório ---")
print(f"Todos os acessos: {access_user_list}")
print(f"Número total de acessos: {number_of_access}")
print(f"Utilizadores únicos: {access_usernames}")
print(f"Número de utilizadores únicos: {len(access_usernames)}")
print()

search_username = input("Username a pesquisar: ")

if search_username in access_usernames:
    print("O utilizador apareceu nos acessos.")
else:
    print("O utilizador não apareceu nos acessos.")    

tags = set()

number_of_tags = int(input("Número de tags: "))

while number_of_tags <= 0:
    print("Número inválido.")
    number_of_tags = int(input("Número de tags: "))

for tag_number in range(1, number_of_tags + 1):
    tag = input(f"Tag {tag_number}: ")
    tags.add(tag)

print()
print("--- Tags registadas ---")
print(f"Tags únicas: {tags}")
print(f"Número de tags únicas: {len(tags)}")

search_tag = input("\nTag a procurar: ")

if search_tag in tags:
    print("A tag existe.")
else:
    print("A tag não existe.")
    
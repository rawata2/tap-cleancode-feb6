# ---- Session on Clean Coding, Data types, Functions, TDD ----
horizontal_rule = "-" * 40

# Refactor the following

# Assigning Lists
list_sample = [1, 2, 3, "Four", 5, 6]

# Access Lists
print("     Item 1:", list_sample[0])
print("     Item 4:", list_sample[3])
print("  Item Last:", list_sample[-1])
print("Slice items:", list_sample[2:len(list_sample)],f'array length: {list_sample}')
# Loop through Lists
print(" ---- Listing Items in List ----")
for item in list_sample:
  print(item)
print(" ---- Listing Items using range() ----")
# for using range(start,stop,step) / range(stop)
for ctr in range(len(list_sample)):
  print(ctr, ":", list_sample[ctr])
print(horizontal_rule)

em = "j@em2.com"

# Dictionary : { key_1: value_1, key_2: value_2, ..... key_n: value_n }
dictionary_sample = {
  "id" : 123,
  "name": "John",
  "email" : [
      "j@em.com",
      em
  ]
}

# Access dictionaries individually
print("   ---- Access Dictionaries ----")
print("     Id:", dictionary_sample["id"])
print("   Name:", dictionary_sample["name"])
print(" Emails:", dictionary_sample["email"])
print("Email 1:", dictionary_sample["email"][0])
print("Email 2:")
print(horizontal_rule)
# Loop through dictionaries print key : value - element type
for key in dictionary_sample:
  print(key, ":", dictionary_sample[key])
print("-"*20)


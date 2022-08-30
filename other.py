# print(hash(address_to_compare))
# concat_address = h.get(1).address + "\n(" + str(h.get(1).zip) + ")"
concat_address = h.get(address_to_compare)

# print(concat_address)
# print(hash(concat_address))

# Compare strings char by char
# for i in range(0, len(concat_address)):
#     print(concat_address[i] + " ")
#     print(hex(id(concat_address[i])))
#     print(address_to_compare[i] + " ")
#     print(hex(id(address_to_compare[i])))
#     print("\n")


# print(address_to_compare is concat_address)
# print(address_to_compare.__eq__(concat_address))
# print(address_to_compare == concat_address)
full_mask = 4294967295
prefix = input("Enter a prefix length: ")
subnet = 32 - int(prefix)
subnet = 2 ** subnet
subnet = subnet - 1
bin_subnet = bin(full_mask - subnet)
bin_subnet = str(bin_subnet[2:])
bin_wildcard = 11111111111111111111111111111111 - int(bin_subnet)
bin_wildcard = str(bin_wildcard).zfill(32)
result = full_mask - subnet
result = bin(result)
result = str(result[2:])

octet_size = 8

octet = []
octet_wildcard = []

for i in range(0, 25, octet_size):
    octet.append(result[i:i + octet_size])
    octet_wildcard.append(bin_wildcard[i:i + octet_size])

for i in range(len(octet)):
    octet[i] = int(octet[i], 2)
    octet_wildcard[i] = int(octet_wildcard[i], 2)

for i in range(len(octet)):
    octet[i] = str(octet[i])
    octet_wildcard[i] = str(octet_wildcard[i])

octet = '.'.join(octet)
octet_wildcard = '.'.join(octet_wildcard)

print("The subnet mask is: " + octet)
print("The wildcard mask is: " + octet_wildcard)
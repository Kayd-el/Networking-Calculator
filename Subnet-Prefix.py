print("Will you be using a subnet or wildcard mask?\n")
print("#1 Subnet mask\n")
print("#2 Wildcard mask\n")
selection = input("Enter a number: ")

if selection == "1":
    Subnet_mask = input("Enter a subnet mask (eg. 255.255.255.0): ")
    Mask_octets = Subnet_mask.split('.')
    mask_binary = ''

    for i in Mask_octets:
        mask_binary += '.'.join(bin(int(i))[2:])

    prefix = mask_binary.count('1')
    print("The prefix length for that subnet mask" + prefix)

if selection == "2":
    Wildcard_mask = input("Enter a wildcard mask (eg. 0.0.0.255): ")
    Mask_octets = Wildcard_mask.split('.')
    mask_binary = ''

    for i in Mask_octets:
        mask_binary += '.'.join(bin(int(i))[2:].zfill(8))

    prefix = mask_binary.count('0')
    print("The prefix length for that wildcard mask" + prefix)


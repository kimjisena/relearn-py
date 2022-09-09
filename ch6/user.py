#! /bin/python3

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for item in user_0.items():
    print(f"\nItem: {item}")
    print(f"Key: {item[0]}")
    print(f"Value: {item[1]}")


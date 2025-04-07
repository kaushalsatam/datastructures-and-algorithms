# NOTE:  With Numbers

num1 = 11
num2 = num1

print("Before num 2 value is updated: ")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

print(f"\nnum1 points to: {id(num1)}")
print(f"\nnum2 points to: {id(num2)}")

num2 = 22

print("After num 2 value is updated: ")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

print(f"\nnum1 points to: {id(num1)}")
print(f"\nnum2 points to: {id(num2)}")

# NOTE:  With Dictionary

dict1 = {
    'value': 11,
}

dict2 = dict1

print("Before dict2[\"value\"] is updated: ")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"\ndict2 points to: {id(dict2)}")

dict2["value"] = 22

print("After dict2[\"value\"] is updated: ")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"\ndict2 points to: {id(dict2)}")

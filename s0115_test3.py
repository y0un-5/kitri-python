# s0115_test3.py

text="20010331Rainy"
ssn="870730-1133555"
year=ssn[0:2]
month=ssn[2:4]
day=ssn[4:6]

print("생년:", year)
print("생월:", month)
print("생일:", day)


date = text[:8]
weather = text[8:]

print(date)
print(weather)


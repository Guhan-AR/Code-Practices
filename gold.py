Gold = 0.0
# amount = 10
amount = 9.7
while True:
    data = input("Gold Rate on day:")
    # print(data.isdigit())
    if not data.isdigit():
        break
    Gold += amount/int(data)
    print("Gold:",Gold)
print("Thank you")
print(Gold)

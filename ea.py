def masterA_user():
    userA = input("Input your userA name: ")
    empA = input("Input Your EmpA Id card: ")
    if userA == "nattakit" and empA == "1234":
        data_userA = userA + " " + empA
        print(data_userA)
    else:
        print("error")
    
def masterB_user():
    userB = input("Input your userB name: ")
    empB = input("Input Your EmpB Id card: ")
    if userB == "nattahee" and empB == "5678":
        data_userB = userB + " " + empB
        print(data_userB)
    else:
        print("error")

# Example usage
masterA_user()
masterB_user()
def masterA_user ():  #สร้างกล่องฟังก์ชั่นการใช้งานของ A user
    userA = input(str("Input your userA name :")) #รับค่า A user ผ่านแป้นพิมพ์ที่เป็น string
    empA = input(str("Input Your EmpA Id card :")) #รับค่า emp A user ผ่านแป้นพิมพ์ที่เป็น string
    if userA == "nattakit" and empA =="1234":  #ถ้าUser A  = nattakit (และ) EmpA = 1234
        data_userA = userA +"  "+  empA #นำค่า user A และ EmpA มารับกันแล้วเก็บไว้ใน data_userA
        print(data_userA) #แสดงค่าผลัพท์
    else:  #ถ้าค่าไม่ตรงกัน
        print("error")
  
    
    
def masterB_user ():     #สร้างกล่องฟังก์ชั่นการใช้งานของ B user
    userB = input(str("Input your userB name :")) #รับค่า B user ผ่านแป้นพิมพ์ที่เป็น string
    empB = input(str("Input Your EmpB Id card :")) #รับค่า emp B user ผ่านแป้นพิมพ์ที่เป็น string
    if userB == "nattahee" and empB =="5678": #ถ้าUser B  = nattahee (และ) EmpB = 5678
        data_userB = userB +"  "+  empB #นำค่า user B และ EmpB มารับกันแล้วเก็บไว้ใน data_userB
        print(data_userB) #แสดงค่าผลัพท์
    else: #ถ้าค่าไม่ตรงกัน
        print("error")


 

masterA_user()
masterB_user()
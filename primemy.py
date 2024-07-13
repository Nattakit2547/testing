def primey(number):
    if number <= 1:
        return False
    if number <=2 :
        return True
    if number %2 == 0:
        return False
    
    sqare_num=int(number**0.5)+1
    for i in range(3 , sqare_num , 2):
        if number % i == 0 :
            return False
        
    return True

def mainru():
    while True:
        try:
            number = int(input("ใส่ข้อมูลมาไอ่สาสสส"))
            if number == 0:
                print('ออกแม่งละสัส')
                break
            if number <= 1:
                print("ใส่มาอีกดิ้สัส")
                continue

            if primey(number):
                print(f"เลขนี้แหละฉลาดนี่หว่า")
            else:
                print(f"ไม่ใช่ไอควายยยย")
        except ValueError:
            print("มั่วละพี่ชาย")

if __name__ == "__main__":
    mainru()




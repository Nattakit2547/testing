def prime(number): #ฟังก์ชันคำสั่งสำหรับเช็ค prime
    if number <= 1:
        return False
    if number <= 2:
        return True   #เลขที่ 2 เป็นเลข prime
    if number % 2 == 0:
        return False
    
    square_num =int (number**0.5)+1
    for i in range(3, square_num, 2):  #รูปแบบการเช็คเลข prime 
        if number % i == 0:
            return False
    

    return True

def main():  #รูปแบบฟังก์ชันหลักสำหรับป้อนข้อมูลของผู้ใช้
    while True:   #วนลูปเมื่อข้อมูลเป็นจริง
        try:
            number = int (input("กรุณาใส่เลขจำนวนเต็ม ถ้าใส่ 0 จะเป็นการออกจากระบบ"))
            if number == 0 :  #ถ้าระบบตัวเลขที่ uesr ใส่มามีค่าเท่ากับ 0
                print("ออกจากระบบ")
                break
            if number < 0:
                print("กรุณาใส่เลขจำนวนเต็มเชิงบวก")
                continue

            if prime(number):
                print(f"เลขนี้เป็นเลข Prime")
            else:
                print(f"เลขนี้ไม่ใช่เลข prime ")

        except ValueError:
            print("ค่าไม่ถูกต้อง")

if __name__ == "__main__":
    main()           



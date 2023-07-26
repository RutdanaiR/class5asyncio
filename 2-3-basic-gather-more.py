import asyncio
import time
#ฟังก์ชันแบบ asynchronous
async def hello(i):
    print(f"{time.ctime()}hello{i}started")#ข้อความเริ่มต้นพร้อมกับเวลาปัจจุบัน
    await asyncio.sleep(4)#ระบบการทำงานเป็นเวลา 4 วินาที
    print(f"{time.ctime()}hello{i}done")#ข้อความเมื่อเสร็จสิ้นพร้อมกับเวลาปัจจุบัน

async def main():
    coros = [hello(i)for i in range(10)]  #สร้างรายการของ coroutine 10 ตัว ที่เรียกใช้ hello(i)
    await asyncio.gather(*coros) #รวม coroutine ทั้งหมดด้วย asyncio.gather()

if __name__ == '__main__':
    start = time.time()#บันทึกเวลาเริ่มต้นของโปรแกรม
    asyncio.run(main())#รันฟังก์ชันหลักโดยใช้ asyncio.run 
    end = time.time() #บันทึกเวลาสิ้นสุดของโปรแกรม
    print(f'Time:{end-start:.2f}sec') #คำนวณเเละเรียกใช้โปรแกรมทั้งหมด


#ผลลัพท์
#Wed Jul 26 15:15:33 2023hello0started
#Wed Jul 26 15:15:33 2023hello1started
#Wed Jul 26 15:15:33 2023hello2started
#Wed Jul 26 15:15:33 2023hello3started
#Wed Jul 26 15:15:33 2023hello4started
#Wed Jul 26 15:15:33 2023hello5started
#Wed Jul 26 15:15:33 2023hello6started
#Wed Jul 26 15:15:33 2023hello7started
#Wed Jul 26 15:15:33 2023hello8started
#Wed Jul 26 15:15:33 2023hello9started
#Wed Jul 26 15:15:37 2023hello0done
#Wed Jul 26 15:15:37 2023hello2done
#Wed Jul 26 15:15:37 2023hello6done
#Wed Jul 26 15:15:37 2023hello9done
#Wed Jul 26 15:15:37 2023hello8done
#Wed Jul 26 15:15:37 2023hello5done
#Wed Jul 26 15:15:37 2023hello7done
#Wed Jul 26 15:15:37 2023hello4done
#Wed Jul 26 15:15:37 2023hello1done
#Wed Jul 26 15:15:37 2023hello3done
#Time:4.01sec
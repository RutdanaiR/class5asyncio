import asyncio
import time
#ฟังก์ชันแบบ asynchronous
async def hello(i):
    print(f"{time.ctime()} hello {i} started")#ข้อความเริ่มต้นพร้อมกับเวลาปัจจุบัน
    await asyncio.sleep(4)#หยุดระบบ 4 วินาที
    print(f"{time.ctime()} hello {i} done")#ข้อความเมื่อเสร็จสิ้นพร้อมกับเวลาปัจจุบัน

async def main():
    task1 = asyncio.create_task(hello(1)) #สร้างงาน asynchronous เพื่อเรียกใช้ hello(1)
    task2 = asyncio.create_task(hello(2)) #สร้างงาน asynchronous เพื่อเรียกใช้ hello(2)
    await asyncio.gather(task1, task2)
# ตรวจสอบว่าสคริปต์นี้กำลังถูกเรียกใช้เป็นโมดูลหลักไหม
if __name__ == '__main__':
    start = time.time()#บันทึกเวลาเริ่มต้น
    asyncio.run(main())#รันฟังก์ชันหลักโดยใช้ asyncio.run
    end = time.time()#บันทึกเวลาสิ้นสุด
    print(f'Time: {end-start:.2f} sec')#คำนวณและพิมพ์เวลาที่ใช้ในการเรียกใช้โปรแกรมทั้งหมด

#ผลลัพท์
#Wed Jul 26 15:14:41 2023 hello 1 started
#Wed Jul 26 15:14:41 2023 hello 2 started
#Wed Jul 26 15:14:45 2023 hello 1 done
#Wed Jul 26 15:14:45 2023 hello 2 done
#Time: 4.00 sec
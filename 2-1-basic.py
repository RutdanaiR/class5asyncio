import asyncio
import time
#พิมพ์ข้อความเริ่มต้น หยุดระบบการทำงานเป็นเวลา 4 วินาที และพิมพ์ข้อความเมื่อเสร็จสิ้น
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
        task1 =asyncio.create_task(hello(1)) #สร้างงาน asynchronous เพื่อเรียกใช้ hello(1)
        task2 =asyncio.create_task(hello(2))# สร้างงาน asynchronous เพื่อเรียกใช้ hello(2)
        await task1#รอ task1 เสร็จสิ้นก่อนที่จะดำเนินการต่อ
        await task2#รอtask2 เสร็จสิ้นก่อนที่จะจบฟังก์ชันหลัก
#ตรวจสอบว่าสคริปต์นี้กำลังถูกเรียกใช้เป็นโมดูลหลักไหม
if __name__ == '__main__':
      start = time.time()#บันทึกเวลาเริ่มต้น
      asyncio.run(main())#รันฟังก์ชันหลักโดยใช้ asyncio.run
      end = time.time() #บันทึกเวลาสิ้นสุด
      print(f'Time: {end-start:.2f} sec')#คำนวณและพิมพ์เวลาที่ใช้ในการเรียกใช้โปรแกรมทั้งหมด
     
#ผลลัพท์
#Wed Jul 26 15:13:49 2023 hello 1 started
#Wed Jul 26 15:13:49 2023 hello 2 started
#Wed Jul 26 15:13:53 2023 hello 1 done
#Wed Jul 26 15:13:53 2023 hello 2 done
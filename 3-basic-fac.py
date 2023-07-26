import asyncio
import time
#ฟังก์ชันแบบ asynchronous
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1) #หยุดระบบการทำงานเป็นเวลา 1 วินาที
        f *= i
    return f
#ฟังก์ชันหลักแบบ asynchronous
async def main():
    L = await asyncio.gather(factorial(2),  factorial(3), factorial(4))
    print(L)    # [2, 6, 24]

if __name__ == '__main__':
    start = time.time() #บันทึกเวลาเริ่มต้นของโปรแกรม
    asyncio.run(main()) #รันฟังก์ชันหลักโดยใช้ asyncio.run
    end = time.time()#บันทึกเวลาสิ้นสุดของโปรแกรม
    print(f'Time: {end-start:.2f} sec') #คำนวณเเละเรียกใช้โปรแกรมทั้งหมด


#ผลลัพท์
#Wed Jul 26 15:16:18 2023hello0started
#Wed Jul 26 15:16:18 2023hello1started
#Wed Jul 26 15:16:18 2023hello2started
#Wed Jul 26 15:16:18 2023hello3started
#Wed Jul 26 15:16:18 2023hello4started
#Wed Jul 26 15:16:18 2023hello5started
#Wed Jul 26 15:16:18 2023hello6started
#Wed Jul 26 15:16:18 2023hello7started
#Wed Jul 26 15:16:18 2023hello8started
#Wed Jul 26 15:16:18 2023hello9started
#Wed Jul 26 15:16:22 2023hello0done
#Wed Jul 26 15:16:22 2023hello2done
#Wed Jul 26 15:16:22 2023hello6done
#Wed Jul 26 15:16:22 2023hello9done
#Wed Jul 26 15:16:22 2023hello8done
#Wed Jul 26 15:16:22 2023hello5done
#Wed Jul 26 15:16:22 2023hello7done
#Wed Jul 26 15:16:22 2023hello4done
#Wed Jul 26 15:16:22 2023hello1done
#Wed Jul 26 15:16:22 2023hello3done
#Time:4.01sec
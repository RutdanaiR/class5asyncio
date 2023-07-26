import asyncio
import time
#แสดงเวลาที่ผ่านไปตั้งแต่เวลาเริ่มต้น
async def sleep():
    print(f'Time: {time.time() - start:.2f}') #แสดงเวลาที่ผ่านไปตั้งแต่เวลาเริ่มต้นโปรแกรม
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))#เรียกใช้งานสองงานพร้อมกัน

if __name__ == "__main__":
    start = time.time()#เก็บเวลาเริ่มต้นของโปรแกรม
    asyncio.run(main())#เรียกใช้งานฟังก์ชัน main ด้วย asyncio.run()
    end = time.time()#เก็บเวลาที่โปรแกรมทำงานเสร็จสิ้น
    print(f'Time: {end-start:.2f} sec')#แสดงเวลาที่รวมเวลาในการทำงานของโปรแกรมทั้งหมด

#ผลลัพท์
#Task A: Computing 0+1
#Time: 0.00
#Task B: Computing 0+1
#Time: 0.00
#Task A: Computing 1+2
#Time: 1.01
#Task B: Computing 1+2
#Time: 1.01
#Task A: Sum = 3
#Task B: Computing 3+3
#Time: 2.01
#Task B: Sum = 6
#Time: 3.03 sec
import asyncio
import time 
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f'Time: {time.time() - start:.2f}') #แสดงเวลาที่ผ่านไปตั้งแต่เวลาเริ่มต้นของโปรแกรม
    time.sleep(1)

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0 
    for number in numbers:
        print(f'Task {name}: Computer {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}:Sum = {total}\n')# แสดงผลรวม

start =time.time()#บันทึกเวลาเริ่มต้นของโปรแกรม

loop = asyncio.get_event_loop() #รันevent loop สำหรับ asyncio
task = [
        loop.create_task(sum("A", [1,2])),
        loop.create_task(sum("B", [1,2,3])),
]
loop.run_until_complete(asyncio.wait(task))# รันด้วยasyncio
loop.close#ปิดเมื่อเสร็จสิ้นการทำงาน

end= time.time() #บันทึกเวลาที่โปรแกรมทำงานเสร็จสิ้น
print(f'Time: {end-start:.2f} sec')#แสดงเวลาที่รวมเวลาในการทำงานของโปรแกรมทั้งหมด

#ผลลัพท์
#Task A: Computer 0+1
#Time: 0.00
#Task B: Computer 0+1
#Time: 0.00
#Task A: Computer 1+2
#Task B: Computer 1+2
#Time: 1.02
#Time: 1.02
#Task B: Computer 3+3
#Task A:Sum = 3
#Time: 2.03
#Task B:Sum = 6
#Time: 3.04 sec

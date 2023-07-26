import asyncio
import time
#แสดงเวลาที่ผ่านไปตั้งแต่เวลาเริ่มต้น
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
#หาผลรวมของตัวเลขในลิสต์ numbers
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()#เวลาเริ่มต้นการทำงาน

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))#รันการทำงาน asyncio tasks
loop.close()#ปิด event loop เมื่อเสร็จสิ้น

end = time.time()#เวลาสิ้นสุดการทำงาน
print(f'Time {end-start:.2f} sec')#เเสดงเวลาที่ใช้ในการทำงานทั้งหมด

#ผลลัพท์
#Task A: Computing 0+1
#Time: 0.00
#Task B: Computing 0+1
#Time: 0.00
#Task A: Computing 1+2
#Time: 1.00
#Task B: Computing 1+2
#Time: 1.00
#Task A: Sum = 3
#Task B: Computing 3+3
#Time: 2.01
#Task B: Sum = 6
#Time 3.02 sec
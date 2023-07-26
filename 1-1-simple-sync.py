#import time.
import time 
#นิยามฟังก์ชัน sleep
def sleep():
    #แสดงผลเป็นทศนิยม 2 ตำแหน่ง
    print(f'time:{time.time() - start:.2f}')
    #หน่วงเวลาการทำงาน
    time.sleep(1)

#นิยามฟังก์ชัน sum ที่รับชื่องาน (name) และลิสต์ของตัวเลข (numbers) เป็นพารามิเตอร์
def sum(name, numbers):
    total = 0 # กำหนดค่าเริ่มต้นของผลรวมเป็น 0
    for number in numbers:# วนลูปตามตัวเลขในลิสต์ numbers
        print(f'Task{name}: Computing {total}+{number}')
        sleep()
        total += number #ทำการรวมตัวเลขในผลรวม (total)
    #
    print(f'Task {name}: Sum = {total}\n')
#บันทึกเวลาเริ่มต้นของการทำงาน
start = time.time()

task = [
#เรียกใช้ฟังก์ชันsum("A",[1,2]) ทำการรวมค่าในลิสต์ [1,2]
        sum("A",[1,2]),
#เรียกใช้ฟังก์ชัน sum("b",[1,2,3]) ทำการรวมค่าในลิสต์ [1,2,3]
        sum("b",[1,2,3]),
]
#สิ้นสุดการทำงานที่เพื่อบันทึกเวลาสิ้นสุดของการ
end = time.time()
print(f'Time: {end-start:.2} sec')

#ผลลัพท์  
#time:0.00
#TaskA: Computing 1+2
#time:1.00
#Task A: Sum = 3
#Taskb: Computing 0+1
#time:2.00
#Taskb: Computing 1+2
#time:3.00
#Taskb: Computing 3+3
#time:4.00
#Task b: Sum = 6
#Time: 5.0 sec
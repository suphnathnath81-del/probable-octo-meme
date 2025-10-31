# Import modules
import time
import os
import random
import shutil
import shlex
import urllib.request

d=0 

print("《จำลอง os โดย python3》")

# ฟังก์ชันสำหรับจำลองการรอด้วยจุดไข่ปลา
def animate_wait(message, min_dots=5, max_dots=15, min_sleep=0.3, max_sleep=0.8):
    """แสดงข้อความและจำลองการรอด้วยการพิมพ์จุดไข่ปลา"""
    print(message, end="", flush=True)
    for _ in range(random.randint(min_dots, max_dots)):
        print(".", end="", flush=True)
        time.sleep(random.uniform(min_sleep, max_sleep))
    print()

while True:
    # แสดง prompt และรับคำสั่ง
    # os.getcwd() จะแสดงพาธปัจจุบัน
    current_dir = os.path.basename(os.getcwd())
    prompt_dir = current_dir if current_dir else "~"
    a = (input(f"รอคำสั่ง {prompt_dir}/< "))
    
    # หากมีการกด Enter โดยไม่มีข้อความ (vars ไม่ได้ใช้ในการตรวจสอบนี้)
    if not a.strip():
        continue
    
    # แยกคำสั่งและอาร์กิวเมนต์
    try:
        parts = shlex.split(a)
    except ValueError as e:
        print(f"ข้อผิดพลาดในการแยกคำสั่ง: {e}")
        continue

    คำสั่ง = parts[0]
    คำสั่งรอง = parts[1:] if len(parts) > 1 else []
    
    
    if คำสั่ง == 'exit':
       print("กำลังปิด", end="")
       for _ in range(random.randint(5, 20)):
           print(".", end="", flush=True)
           if _ == 19:
               print("\nอาจจะนานนิดนึงนะ") 
           time.sleep(random.uniform(0.3,1.3))
              
       break
    
    
    
                
    elif คำสั่ง == 'vim':
        if not คำสั่งรอง:
            print("วิธีใช้: vim <ชื่อไฟล์>")
            continue
        
        อ = 0
        ไฟล์ = คำสั่งรอง[0]
        print("      《เขียนข้อความด้วย vim》")
        print("พิมพ์ 'ออก' หรือ '#exit' เพื่อบันทึกและออก")
        
        while True:
           อ += 1
           x = str(input(f"{อ}# "))
           
           if x == 'ออก' or x == '#exit':
             animate_wait("กำลังบันทึกไฟล์", 5, 15, 0.3, 0.8)
             print(f"บันทึก '{ไฟล์}' เเล้ว")
             break

           with open(ไฟล์, "a", encoding="utf-8") as f:
               f.write(x + "\n")
           
           
    
    elif คำสั่ง == 'rf':
        if not คำสั่งรอง:
            print("วิธีใช้: rf <ชื่อไฟล์>")
            continue
            
        อ่านไฟล์vim = คำสั่งรอง[0]
        try:
            with open(อ่านไฟล์vim, "r", encoding="utf-8") as f:
                ตัวอ่าน = f.read()
                print("      《เนี้อหาไฟล์》")
                print(ตัวอ่าน)
                print("*****************************")
        except FileNotFoundError:
            print(f"ไม่มีไฟล์ '{อ่านไฟล์vim}'")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")       
    
    elif คำสั่ง == 'df':
       if not คำสั่งรอง:
            print("วิธีใช้: df <ชื่อไฟล์>")
            continue
            
       ลบไฟล์ = คำสั่งรอง[0]
       if os.path.exists(ลบไฟล์) and os.path.isfile(ลบไฟล์):
           os.remove(ลบไฟล์)
           animate_wait("กำลังลบ", 8, 15, 0.5, 0.8)
           print("ลบเเล้ว")    
        
       else:
           print(f"ไม่มีไฟล์ '{ลบไฟล์}'") 
           
    elif คำสั่ง == 'mkdir':
        if not คำสั่งรอง:
            print("วิธีใช้: mkdir <ชื่อโฟลเดอร์>")
            continue
            
        fb = คำสั่งรอง[0]
        if not os.path.exists(fb):
            try:
                os.mkdir(fb)
                animate_wait("กำลังสร้างโฟลเดอร์", 3, 9, 0.3, 1)
                print(f"สร้างโฟลเดอร์ '{fb}' เเล้ว")
            except Exception as e:
                print(f"สร้างโฟลเดอร์ไม่สำเร็จ: {e}")
          
        else:
            print(f"มีโฟลเดอร์ '{fb}' อยู่เเล้ว")  
    
        
    
    elif คำสั่ง == 'mv':
        if len(คำสั่งรอง) < 2:
            print("วิธีใช้: mv <ไฟล์/โฟลเดอร์ต้นทาง> <ปลายทาง>")
            continue
            
        f = คำสั่งรอง[0]
        fd = คำสั่งรอง[1]
        
        if os.path.exists(f) and os.path.exists(fd) and os.path.isdir(fd):
            try:
                shutil.move(f, fd)
                animate_wait("กำลังย้าย", 3, 9, 0.3, 1)
                print("ย้ายเสร็จเเล้ว")
            except Exception as e:
                print(f"ย้ายไม่สำเร็จ: {e}")
        elif not os.path.exists(f):
            print(f"ไม่มีไฟล์/โฟลเดอร์ต้นทาง '{f}'")
        elif not os.path.exists(fd):
            print(f"ไม่มีปลายทาง '{fd}'")
        elif not os.path.isdir(fd):
            print(f"ปลายทาง '{fd}' ไม่ใช่โฟลเดอร์")

    
    elif คำสั่ง == 'cd':
     if not คำสั่งรอง:
         print("วิธีใช้: cd <ชื่อโฟลเดอร์> หรือ cd ~/")
         continue   
         
     cdfd = คำสั่งรอง[0]
     if cdfd == '~/':
        # ในสภาพแวดล้อมนี้ อาจไม่สามารถเปลี่ยนไปสู่ home directory จริงได้
        # แต่เพื่อจำลองการทำงาน จะใช้ root ของไดเรกทอรีที่รัน script
        try:
            # ใช้ root ของไดเรกทอรีปัจจุบัน
            os.chdir(os.path.abspath(os.path.dirname(__file__))) 
        except Exception:
            # หากล้มเหลวในการกลับไปที่ root, ให้กลับไปที่ CWD (Current Working Directory)
            pass
     elif os.path.isdir(cdfd):
        try:
            os.chdir(cdfd)
        except Exception as e:
            print(f"ไม่สามารถเข้าถึง '{cdfd}': {e}")
     else:
        print(f"ไม่พบโฟลเดอร์ '{cdfd}'")
    
    elif คำสั่ง == 'rmdir':
        if not คำสั่งรอง:
            print("วิธีใช้: rmdir <ชื่อโฟลเดอร์>")
            continue
            
        rdir = คำสั่งรอง[0]
        if os.path.isdir(rdir):
            try:
                os.rmdir(rdir)
                animate_wait("กำลังลบ", 8, 15, 0.5, 0.8)
                print("ลบเเล้ว")
            except OSError as e:
                print(f"ลบโฟลเดอร์ไม่สำเร็จ (อาจจะไม่ว่างเปล่า): {e}")
            
        else:
            print(f"ไม่มีโฟลเดอร์ '{rdir}'")   
    
    elif คำสั่ง == 'rpy':
        if not คำสั่งรอง:
            print("วิธีใช้: rpy <ชื่อไฟล์.py>")
            continue
            
        rd = คำสั่งรอง[0]
        if os.path.exists(rd) and os.path.isfile(rd):
           print(f"----- รันไฟล์ {rd} -----")
           try:
               # exec(open(rd).read()) # การใช้ exec อาจก่อให้เกิดปัญหาได้
               # แทนที่ด้วยการรันอย่างง่าย
               code = open(rd).read()
               exec(code)
           except Exception as e:
               print(f"เกิดข้อผิดพลาดขณะรันไฟล์ Python: {e}")
           print(f"----- สิ้นสุดการรันไฟล์ {rd} -----")
        
        else:
            print(f"ไม่มีไฟล์ Python '{rd}'")
        
    
    elif คำสั่ง == 'ls':
         # ดูเนื้อหาในไดเรกทอรีปัจจุบัน
         print("รายการไฟล์/โฟลเดอร์:")
         for ไฟล์ in os.listdir('.'):
            # ตรวจสอบว่าเป็น Directory หรือ File เพื่อแสดงผลที่เหมือน OS มากขึ้น
            is_dir = os.path.isdir(ไฟล์)
            print(f"{'D' if is_dir else 'F'}  {ไฟล์}")
    
    elif คำสั่ง == 'loadpy':
     # ปรับปรุง: รองรับการระบุชื่อไฟล์ปลายทาง
     if len(คำสั่งรอง) < 1:
        print("ใช้แบบนี้: loadpy <url> [ชื่อไฟล์ปลายทาง]")
        continue

     url = คำสั่งรอง[0]
     
     if len(คำสั่งรอง) >= 2:
        filename = คำสั่งรอง[1]  # ใช้ชื่อไฟล์ที่ผู้ใช้ระบุ
     else:
        # หากไม่ได้ระบุชื่อไฟล์ปลายทาง ให้ใช้ชื่อไฟล์จาก URL
        filename = url.split("/")[-1]
        if not filename:
            # Fallback in case URL ends with /
            filename = "downloaded_file.dat"

     try:
        animate_wait(f"กำลังดาวน์โหลดไฟล์จาก {url} ไปยัง {filename}", 5, 10, 0.3, 1)
        urllib.request.urlretrieve(url, filename)
        print(f"โหลดไฟล์ '{filename}' เสร็จแล้ว")
     except Exception as e:
        print(f"\nดาวน์โหลดไม่สำเร็จ: เกิดข้อผิดพลาด {e}")        
            
    elif คำสั่ง == '~h':
        print("---------------------------------")
        print("   รายการคำสั่งจำลอง OS")
        print("---------------------------------")
        print("[exit] ใช้ออกทุกอย่าง หรือ [~/exit]")
        print("[mkdir] <ชื่อโฟลเดอร์> ใช้สร้างโฟลเดอร์")
        print("[cd] <ชื่อโฟลเดอร์> หรือ [cd ~/] ใช้เข้าโฟลเดอร์")
        print("[rmdir] <ชื่อโฟลเดอร์> ใช้ลบโฟลเดอร์ (ต้องว่างเปล่า)")
        print("[df] <ชื่อไฟล์> ใช้ลบไฟล์")
        print("[rf] <ชื่อไฟล์> ใช้อ่านเนื้อหาไฟล์")
        print("[ls] ดูไฟล์และโฟลเดอร์ทั้งหมด")
        print("[mv] <ไฟล์/โฟลเดอร์ต้นทาง> <ปลายทาง> ย้ายไฟล์เข้าโฟลเดอร์")
        print("[rpy] <ชื่อไฟล์.py> รันไฟล์ Python")
        print("[loadpy] <url> [ชื่อไฟล์ปลายทาง] ใช้ดาวน์โหลดไฟล์จากอินเทอร์เน็ต")
        print("[pwd] แสดงไดเรกทอรีปัจจุบัน")
        print("[vim] <ชื่อไฟล์> ใช้เขียนข้อความลงไฟล์")
        print("---------------------------------")
         
        
    elif คำสั่ง == 'pwd':
        print(os.getcwd())                     
    
    else:
        print(f"ไม่รู้จักคำสั่ง~/ [ {a} ]")
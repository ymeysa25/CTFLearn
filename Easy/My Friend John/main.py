from zipfile import ZipFile
import time
import logging
import threading
import time

start = time.time()
def extract_zip(namefile, password = None):
   with ZipFile(namefile, 'r') as zipObj:
      password = bytes(password, 'utf-8')
      try:
         zipObj.extractall(pwd= password)
      except:
         zipObj.extractall()
         print("I don't know what happen, buat is open by itself")

def load_pass(namefile):
   with open(namefile, 'r', errors="ignore") as f:
      data = f.read().strip().split("\n")
   return data

def crack_zip_thread(args):
   global is_find
   zip_file, passwords = args
   for idx, pwd in enumerate(passwords):
      print("Try :", idx, pwd)
      if is_find:
         break
      try:
         extract_zip(zip_file, pwd)
         print("Yee Find PASS" , pwd)
         is_find = True
         break
      except:
         pass

def CrackPass(passwords, zipname):
   global is_find
   num_threda = 2
   len_data = len(passwords)
   diff = len_data // num_threda
   c = 0
   for index in range(num_threda):
      if index == num_threda - 1:
         start, end = c, len_data
      else:
         start, end = c, diff

      logging.info("Main    : create and start thread %d.", index)
      args = (zipname, passwords[start:end])
      x = threading.Thread(target=crack_zip_thread, args=(args,))
      x.start()
      start += diff

   while True:
      if is_find:
         end = time.time()
         print("Time Taken", (end - start) / 60, "minutes")
         break
   is_find = False

if __name__ == "__main__":
   is_find = False
   format = "%(asctime)s: %(message)s"
   logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

   threads = list()
   rockyou_pass = sorted(load_pass("rockyou.txt"))
   CrackPass(rockyou_pass, "use-rockyou.zip")

   rockyou_pass = sorted(load_pass("custom-list.txt"))
   CrackPass(rockyou_pass, "custom-list.zip")

   pin_passwords = [str(pwd) for pwd in list(range(999999))]      
   CrackPass(pin_passwords, "brute-force-pin.zip")

   print('flag.txt')

   


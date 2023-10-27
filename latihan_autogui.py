import pyautogui
import time

def kordinat_waktu(detik):
    while detik:
        mins, secs = divmod(detik, 60)
        formatWaktu = '{:02d}:{:02d}'.format(mins, secs)
        kordinat = pyautogui.position()
        print("kordinat:", kordinat)
        print("sisa waktu:", formatWaktu, end='\r')
        time.sleep(1)
        detik -= 1
def autoclik(item,x,y):
    x = x
    y = y
    while True:
        time.sleep(1)
        pyautogui.press('item')
        pyautogui.moveTo(x, y)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(0,3)
        pyautogui.press('enter')
        time.sleep(0,3)
        pyautogui.press('enter')

print("""
pilihan:
[1].melihat kordinat
[2].membuat autoclick
""")
opsi = int(input("masukan opsi di atas: "))

if opsi == 1:
    timer = int(input("Berapa lama waktu hingga habis: "))
    print(kordinat_waktu(timer))
elif opsi == 2:
    x = int(input("masukan kordinat x: "))
    y = int(input("masukan kordinat y: "))
    try:
        hotKey = int(input("item yang nomer berapa yang ingin di break pada hotbar: "))
        autoclik(hotKey,x,y)
    except ValueError:
      print("Masukkan harus berupa angka.")
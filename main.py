import time
import pyautogui
import keyboard

while True:
    try:
        time.sleep(12)

        for _ in range(9):
            pyautogui.scroll(-80)
            time.sleep(0.5)


        button_location = pyautogui.locateOnScreen("download.PNG", confidence=0.8)


        if button_location:
            x, y = pyautogui.center(button_location)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            print("Button has been clicked!")
        else:
            time.sleep(1)

        if keyboard.is_pressed("o"):
            print("Stopping script.")
            break

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)




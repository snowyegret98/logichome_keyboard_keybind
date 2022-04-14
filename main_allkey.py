from pynput.keyboard import Key, Listener, KeyCode, Controller
import mouse
import json


def on_press(key):
    check_key(key)


def on_release(key):
    if key == Key.esc:
        print("prevent esc")


def check_key(key):
    if key in [
        KeyCode(char=up),
        KeyCode(char=down),
        KeyCode(char=left),
        KeyCode(char=right),
        KeyCode(char=left_mouse),
        KeyCode(char=right_mouse),
        KeyCode(char=shift_left_mouse),
        KeyCode(char=shift_right_mouse),
    ]:
        if key == KeyCode(char=up):
            mouse.move(0, -pixel, absolute=False, duration=0)
        if key == KeyCode(char=down):
            mouse.move(0, pixel, absolute=False, duration=0)
        if key == KeyCode(char=left):
            mouse.move(-pixel, 0, absolute=False, duration=0)
        if key == KeyCode(char=right):
            mouse.move(pixel, 0, absolute=False, duration=0)
        if key == KeyCode(char=left_mouse):
            mouse.click(button="left")
        if key == KeyCode(char=right_mouse):
            mouse.right_click()
        if key == KeyCode(char=shift_left_mouse):
            Controller().press(Key.shift)
            mouse.click(button="left")
            Controller().release(Key.shift)
        if key == KeyCode(char=shift_right_mouse):
            Controller().press(Key.shift)
            mouse.right_click()
            Controller().release(Key.shift)


print("---프로그램 시작---")

try:
    with open("setting.json") as json_file:
        data = json.load(json_file)
        pixel = data["pixel"]
        left_mouse = data["left_mouse"]
        right_mouse = data["right_mouse"]
        shift_left_mouse = data["shift_left_mouse"]
        shift_right_mouse = data["shift_right_mouse"]
        up = data["up"]
        down = data["down"]
        left = data["left"]
        right = data["right"]
except:
    print("setting.json 파일을 찾을 수 없거나, json 형식이 맞지 않습니다.")
    input("종료하려면 엔터를 누르세요.")

print(f"픽셀 너비 : {pixel}")
print(f"위: {up}")
print(f"아래: {down}")
print(f"왼쪽: {left}")
print(f"오른쪽: {right}")
print(f"왼쪽 마우스 버튼 : {left_mouse}")
print(f"오른쪽 마우스 버튼 : {right_mouse}")
print(f"왼쪽 마우스 버튼 + shift : {shift_left_mouse}")
print(f"오른쪽 마우스 버튼 + shift : {shift_right_mouse}")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

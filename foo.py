from pynput import keyboard
from pynput.keyboard import Listener, Key


def on_press(key):
    print("press：{0}".format(key))

def on_release(key):
# press esc quit
    if key == keyboard.Key.esc:
        return False
    else:
        print("release：{0}".format(key))


if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

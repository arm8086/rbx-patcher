import os, glob, sys, requests

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

list_of_files = glob.glob(os.path.expanduser('~') + '\AppData\Local\Roblox\Versions\*')
latest_dir = max(list_of_files, key=os.path.getctime)

s = requests.get('https://github.com/zer0mania/roblox-oof-patcher/raw/main/ouch.ogg').content
i1 = requests.get('https://github.com/problematic-scripter/rbx-patcher/raw/main/ArrowCursor.png').content
i2 = requests.get('https://github.com/problematic-scripter/rbx-patcher/raw/main/ArrowFarCursor.png').content

with open(latest_dir + '\content\sounds\ouch.ogg', 'wb') as f:
    f.truncate(0)
    f.write(s)
    f.close()
with open(latest_dir + '\content\textures\Cursors\KeyboardMouse\ArrowCursor.png', 'wb') as f:
    f.truncate(0)
    f.write(i1)
    f.close()
with open(latest_dir + '\content\textures\Cursors\KeyboardMouse\ArrowFarCursor.png', 'wb') as f:
    f.truncate(0)
    f.write(i2)
    f.close()
print("patched sound and image")
input()

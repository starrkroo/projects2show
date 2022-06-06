import win32gui


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd))


win32gui.EnumWindows(winEnumHandler, None)

# win32gui.PostMessage(0x30072, win32con.WM_CLOSE, 0, 0)

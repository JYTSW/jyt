import pygetwindow as gw

# 获取所有窗口
windows = gw.getWindowsWithTitle('MuMu模拟器12')

if windows:
    # 假设你只需要第一个匹配的窗口
    window = windows[0]
    window_x, window_y = window.left, window.top
    print(f"模拟器窗口位置: ({window_x}, {window_y})")
else:
    print("未找到匹配的窗口")

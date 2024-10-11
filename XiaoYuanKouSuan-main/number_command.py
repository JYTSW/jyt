import subprocess
import pyautogui
pyautogui.FAILSAFE = False

# 打开 adb shel会话
def run_adb_command(command):
    shell_process = subprocess.Popen(["E:\\ADB\\platform-tools\\adb.exe", "shell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    shell_process.communicate(command)
    shell_process.stdin.close()


# 转换模拟器坐标
def convert_to_simulator_coords(coord):
    simulator_x, simulator_y, simulator_width, simulator_height = (1125, 49, 543, 991)

    x, y = coord  # 解包坐标元组30

    # 将坐标从屏幕坐标转换为模拟器内的坐标
    converted_x = x - simulator_x
    converted_y = y - simulator_y
    return converted_x, converted_y  # 返回转换后的坐标

def swipe_screen(str):
    xy = str_to_xy(str)
    all_commands = "\n"
    if xy:
        for i in range(len(xy)):
            for j in range(len(xy[i]) - 1):
                start_x, start_y = xy[i][j]
                end_x, end_y = xy[i][j + 1]

                # 确保将坐标元组传递给转换函数
                start_x, start_y = convert_to_simulator_coords((start_x, start_y))
                end_x, end_y = convert_to_simulator_coords((end_x, end_y))

                # 构建滑动命令
                command = f"input swipe {start_x} {start_y} {end_x} {end_y} 0"
                all_commands += command + "\n"
        all_commands += "exit\n"
        print(all_commands)
        run_adb_command(all_commands)


def str_to_xy(str):
    match str:
        case "1":
            return [[1480, 1050], [1440, 1470]]
        case "2":
            return [[1255, 1100], [1700, 1100], [1255, 1470], [1700, 1470]]
        case "3":
            return [[1344, 1040], [1600, 1200], [1270, 1323], [1635, 1379], [1249, 1588]]
        case "4":
            return [[1716, 1274],[1245,1296],[1450,1030],[1450,1466]]
        case "5":
            return [[1558,1020],[1290,1211],[160,1348],[1300.1472]]
        case "6":
            return [[1533,1027],[1265,1428],[1663,1439]]
        case ">":
            return [[[1350, 1080], [1545, 1172], [1295, 1297]]]
        case "<":
            return [[[1578,1058],[1308,1231],[1560,1292]]]
        case "=":
            return [[[1284, 1122], [1700, 1122]],[[1280, 1300], [1700, 1300]]]

if __name__ == "__main__":
    
    # 执行滑动操作
    swipe_screen("<")
    swipe_screen("=")
    

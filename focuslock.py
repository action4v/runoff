import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, sec)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Focus time is up!")

# 设置专注时长为25分钟（可以根据需要进行调整）
focus_timer(25)

import time
import pyautogui as pa

meet_join_button = (1001,391)
# print(pa.size())
# pa.moveTo(100,150)
# pa.moveTo(meet_join_button)
time.sleep(5)

current_pos = pa.position()
print(current_pos)
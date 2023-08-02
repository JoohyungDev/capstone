# 그냥 led만 제어하는 예제
# import serial
# import time

# ser = serial.Serial('COM4', 9600)

# time.sleep(2)

# ser.write(b'H')

# time.sleep(3)

# ser.write(b'L')

# ser.close()

# exit()

# 커맨드창에서 번호를 누르는 걸 반영해서 led 제어
import serial
import time

ser = serial.Serial('COM4', 9600)
time.sleep(2)

def flash():
    while(True):
        cmd = input('\n0.LED 끄기 1.LED 켜기 2.종료: 0/1/2입력')\
        
        if cmd == "0":
            print("LED 끄기")
            ser.write(b'L')
        elif cmd == "1":
            print("LED 켜기")
            ser.write(b'H')
        elif cmd == "2":
            ser.write(b'L')
            print("종료")
            break
        else:
            print("입력 오류. 0/1/2 입력바람")

flash()
ser.close()
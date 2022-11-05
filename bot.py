
import datetime
import pyautogui as pt
import random
import time 

WORK_HISTORY = 'access\mange\work_history.txt'
class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = 0.1
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 20, position[1] + 15, duration=self.speed)
            pt.click()

        except:
            print('No image found...1')
            return 0
class DoubleClicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = 0.1
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)  # region=(0, 84, 1277, 793)
            pt.moveTo(position[0] + 30, position[1] + 15, duration=self.speed)
            pt.doubleClick()

        except:
            return 0


if __name__ == '__main__':
    # Initialises the clicker
    SearchBox = Clicker('access/img/searchbox.png', speed=1)
    Start = DoubleClicker('access/img/start.png', speed=1)
    VpnPlus = DoubleClicker('access/img/vpnplus.png', speed=1)
    Connect = DoubleClicker('access/img/connect.png', speed=1)
    Home = DoubleClicker('access/img/home.png', speed=1)
    Bondex = DoubleClicker('access/img/bondex.png', speed=1)
    BNDX = DoubleClicker('access/img/bndx.png', speed=1)
    Close = DoubleClicker('access/img/close.png', speed=1)
    Confirm = DoubleClicker('access/img/confirm.png', speed=1)
    Earning = DoubleClicker('access/img/earning.png', speed=1)




    ACCOUNT = 5
    COUNT = 0
    LPD_ID = 0
    STATUS = ''
    global x, y

    # f = open(WORK_HISTORY, "a")
    # dt = datetime.datetime.now()
    # TIME_START = '==> TIME START: ' + str(dt)
    # f.write('\n' + TIME_START + '\n')
    # f.close()

    
    while True:
        # f = open(WORK_HISTORY, "a")  
        x = datetime.datetime.now()
        CurrentTime = str(x) + " - "
        if LPD_ID == ACCOUNT:
            break

        if SearchBox.nav_to_image() == 0:
            time.sleep(1)
        time.sleep(1)
        LPD_ID += 1
        
        if LPD_ID < 10:
            id = '00' + str(LPD_ID)
        elif LPD_ID > 9 and LPD_ID < 100:
            id = '0' + str(LPD_ID)
        else:
            id = str(LPD_ID)

        for i in range (0, len(id) + 3):
            pt.press('backspace')

        LDP = ''
        LDP = 'LDP-' + id
        STATUS = STATUS + LDP
        print(LDP + ' ==> START', end=' ')
        pt.typewrite(id, interval=0.1)
        time.sleep(1)


        if Start.nav_to_image() == 0:
            time.sleep(1)

        while True: 
            if VpnPlus.nav_to_image() != 0:
                time.sleep(1)
                break
        
        print('=> TURN ON VPN', end=' ')

        while True: 
            if Connect.nav_to_image() != 0:
                time.sleep(1)
                break

        time.sleep(5)
        if Home.nav_to_image() != 0:
            time.sleep(1)

        time.sleep(1)
        if Bondex.nav_to_image() != 0:
            time.sleep(1)
        
        print('=> OPEN BONDEX', end=' ')


        while True: 
            if BNDX.nav_to_image() != 0:
                time.sleep(1)
                break

        
        pt.scroll(-250)
        time.sleep(3)

        if Earning.nav_to_image() != 0:
            time.sleep(1)
        
        print('=> EARNING !!!', end=' ')


        time.sleep(1)
        
        if Close.nav_to_image() == 0:
            time.sleep(1)

        time.sleep(1)
        if Confirm.nav_to_image() == 0:
            time.sleep(1)


        y = datetime.datetime.now()
        CurrentTime = CurrentTime + str(y)
        STATUS = STATUS + ' ===> Done!' + ' || ' + CurrentTime
        print(" ==> Done!", end=" || ")
        print(x, " - ", y)
        # f.writelines(STATUS + '\n')
        # f.close()


                
    

        

        
        
        


            
                
                


            








            

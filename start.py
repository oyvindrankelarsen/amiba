from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from tkinter import *

#board = PyMata3()

SENS_1_PIN = 20
SENS_1_REF = 19
BUTTON_PIN = 23
BUTTON_REF = 22
BUTTON_LED_RED = 12
BUTTON_LED_GREEN = 13
BUTTON_LED_BLUE = 21
TV_REL_CTRL = 11
TV_REL_DIR = 18
TV_GEN_CTRL = 10
TV_GEN_DIR = 9

# board.set_pin_mode(SENS_1_PIN, Constants.INPUT)
# board.set_pin_mode(SENS_1_REF, Constants.OUTPUT)
# board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
# board.set_pin_mode(BUTTON_REF, Constants.OUTPUT)
# board.set_pin_mode(BUTTON_LED_RED, Constants.OUTPUT)
# board.set_pin_mode(BUTTON_LED_GREEN, Constants.PWM)
# board.set_pin_mode(BUTTON_LED_BLUE, Constants.OUTPUT)
# board.set_pin_mode(TV_REL_CTRL, Constants.OUTPUT)
# board.set_pin_mode(TV_REL_DIR, Constants.OUTPUT)
# board.set_pin_mode(TV_GEN_CTRL, Constants.PWM)
# board.set_pin_mode(TV_GEN_DIR, Constants.OUTPUT)

root = Tk()
root.geometry("800x600")
frame = Frame(root)
frame.pack()

def discharge():
    print("300V DC Residual Voltage ON ")

   #  board.digital_write(TV_REL_DIR, 1)
   #  board.digital_write(TV_GEN_DIR, 0)
   #  board.digital_write(TV_REL_CTRL, 0)
   #  board.analog_write(TV_GEN_CTRL, 21)
   #  board.digital_write(SENS_1_REF, 1)
   #  board.digital_write(BUTTON_REF, 1)
   #  board.digital_write(BUTTON_LED_RED, 1)
    
   #  board.sleep(5.0)
    
    print("Residual discharge for 1 minute -ACTIVE-")
        
   #  board.digital_write(BUTTON_LED_RED, 0)
   #  board.digital_write(BUTTON_LED_BLUE, 1)
   #  board.analog_write(BUTTON_LED_GREEN, 0)

   #  board.analog_write(TV_GEN_CTRL, 21)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 20)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 19)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 18)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 17)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 16)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 15)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 14)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 13)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 12)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 11)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 10)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 9)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 8)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 7)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 6)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 5)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 4)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 3)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 2)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 1)
   #  board.sleep(3)
   #  board.analog_write(TV_GEN_CTRL, 0)
    
   #  board.digital_write(BUTTON_LED_RED, 0)
   #  board.digital_write(BUTTON_LED_BLUE, 0)
   #  board.analog_write(BUTTON_LED_GREEN, 88)

def reset():
    print("Reset")
    
   #  board.digital_write(TV_REL_DIR, 1)
   #  board.digital_write(TV_GEN_DIR, 0)
   #  board.digital_write(TV_REL_CTRL, 0)
   #  board.analog_write(TV_GEN_CTRL, 0)
   #  board.digital_write(SENS_1_REF, 1)
   #  board.digital_write(BUTTON_REF, 1)
   #  board.digital_write(BUTTON_LED_RED, 0)
   #  board.digital_write(BUTTON_LED_BLUE, 0)
   #  board.analog_write(BUTTON_LED_GREEN, 25)
    
    board.sleep(2.0)

def setVoltage(value):
    
    if value == '100':
       # board.analog_write(TV_GEN_CTRL, 08)
       print("Setting voltage to 100V")
    elif value == '200':
       # board.analog_write(TV_GEN_CTRL, 15)
       print("Setting voltage to 200V")
    elif value == '300':
       # board.analog_write(TV_GEN_CTRL, 23)
       print("Setting voltage to 300V")
    elif value == '400':
       # board.analog_write(TV_GEN_CTRL, 29)
       print("Setting voltage to 400V")
    elif value == '500':
       # board.analog_write(TV_GEN_CTRL, 38)
       print("Setting voltage to 500V")
    elif value == '600':
       # board.analog_write(TV_GEN_CTRL, 50)
       print("Setting voltage to 600V")
    elif value == '700':
       # board.analog_write(TV_GEN_CTRL, 60)
       print("Setting voltage to 700V")
    elif value == '800':
       # board.analog_write(TV_GEN_CTRL, 70)
       print("Setting voltage to 800V")
    elif value == '900':
       # board.analog_write(TV_GEN_CTRL, 80)
       print("Setting voltage to 900V")
    elif value == '1000':
       # board.analog_write(TV_GEN_CTRL, 90)
       print("Setting voltage to 1000V") 
    else:
        print(value)

def short():
   print("Short")
   #  board.digital_write(TV_REL_DIR, 1)
   #  board.digital_write(TV_GEN_DIR, 0)
   #  board.digital_write(TV_REL_CTRL, 1)
   #  board.analog_write(TV_GEN_CTRL, 0)
   #  board.digital_write(SENS_1_REF, 1)
   #  board.digital_write(BUTTON_REF, 1)
   #  board.digital_write(BUTTON_LED_RED, 1)
    
   #  board.sleep(2.0)

def short600V():
   
   print("Short600V")
   #  board.digital_write(TV_REL_DIR, 1)
   #  board.digital_write(TV_GEN_DIR, 0)
   #  board.digital_write(TV_REL_CTRL, 1)
   #  board.analog_write(TV_GEN_CTRL, 50)
   #  board.digital_write(SENS_1_REF, 1)
   #  board.digital_write(BUTTON_REF, 1)
   #  board.digital_write(BUTTON_LED_RED, 1)
    
   #  board.sleep(2.0)  
    
def showhelp():
    print = "Copyleft 2023 RC&C AB Company"

# Main Menu
mainmenu = Menu(root)

# Menu 1
filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Open", command = reset)
filemenu.add_command(label = "Save", command = reset)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)
mainmenu.add_cascade(label = "File", menu=filemenu)

# Menu 2
toolmenu = Menu(mainmenu, tearoff = 0)
toolmenu.add_command(label = "Discharge", command = discharge)
toolmenu.add_command(label = "Reset", command = reset)
toolmenu.add_command(label = "Short", command = short)
toolmenu.add_command(label = "Short600V", command = short600V)
toolmenu.add_command(label = "Set voltage", command = setVoltage)
mainmenu.add_cascade(label = "Tools", menu = toolmenu)

# Menu 3
helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = "Show Help", command = showhelp)
helpmenu.add_separator()
helpmenu.add_command(label = "About AMIBA-ALPHA", command = showhelp)
mainmenu.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = mainmenu)

# labelText = StringVar()
# labelText.set("TESTARrrrrrrrrrrrrrrrrr")
# label = Label(frame, textvariable = labelText)
# label.pack()

# leftframe = Frame(root)
# leftframe.pack(side=LEFT)

# rightframe = Frame(root)
# rightframe.pack(side=RIGHT)

# Scala = Scale(frame, from_ = 0, to = 1000, orient = HORIZONTAL, label = "Volt", resolution = "100", command = setVoltage)
# Scala.pack(padx=5, pady=5)

# Var1 = IntVar()
# Var2 = IntVar()
# ChkBttn = Checkbutton(frame, text = "Option1", variable = Var1)
# ChkBttn.pack(padx = 5, pady = 5)
# ChkBttn2 = Checkbutton(frame, text = "Option2", variable = Var2)
# ChkBttn2.pack(padx = 5, pady = 5)

root.title("AMIBA-ALPHA") 
root.mainloop()

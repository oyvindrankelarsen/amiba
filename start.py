from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from tkinter import *

# Python PEP8 style guide
# board = PyMata3()

'''
When Volta preparing for evaluation, he can generate code snippet from the UI and save it in the format that is compatible with MS PowerPoint to be used as active link to activate simulations.
Some kind of import of the scenario will be required for Volta to be able to use scenarios created for other training rigs. Format is not defined and can be adopted based on UI needs.
'''

def evrig_init():
      msgbox.insert(INSERT, "evrig_init\n")
      root.update()
      SENS_1_PIN=20
      SENS_1_REF=19
      BUTTON_PIN=23
      BUTTON_REF=22
      BUTTON_LED_RED=12
      BUTTON_LED_GREEN=13
      BUTTON_LED_BLUE=21
      TV_REL_CTRL=11
      TV_REL_DIR=18
      TV_GEN_CTRL=10
      TV_GEN_DIR=9

def evsim_init():
   msgbox.insert(INSERT, "evsim_init\n")
   root.update()
   SENS_1_PIN=20
   SENS_1_REF=19
   BUTTON_PIN=23
   BUTTON_REF=22
   BUTTON_LED_RED=12
   BUTTON_LED_GREEN=13
   BUTTON_LED_BLUE=21
   TV_REL_CTRL=11
   TV_REL_DIR=18
   TV_GEN_CTRL=10
   TV_GEN_DIR=9
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

def discharge():
   msgbox.insert(INSERT, "300V DC Residual Voltage ON \n")
   root.update()
   # board.digital_write(TV_REL_DIR, 1)
   # board.digital_write(TV_GEN_DIR, 0)
   # board.digital_write(TV_REL_CTRL, 0)
   # board.analog_write(TV_GEN_CTRL, 21)
   # board.digital_write(SENS_1_REF, 1)
   # board.digital_write(BUTTON_REF, 1)
   # board.digital_write(BUTTON_LED_RED, 1)    
   # board.sleep(5.0)  
   # print("Residual discharge for 1 minute -ACTIVE-")    
   # board.digital_write(BUTTON_LED_RED, 0)
   # board.digital_write(BUTTON_LED_BLUE, 1)
   # board.analog_write(BUTTON_LED_GREEN, 0)
   # board.analog_write(TV_GEN_CTRL, 21)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 20)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 19)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 18)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 17)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 16)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 15)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 14)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 13)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 12)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 11)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 10)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 9)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 8)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 7)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 6)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 5)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 4)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 3)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 2)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 1)
   # board.sleep(3)
   # board.analog_write(TV_GEN_CTRL, 0)
   # board.digital_write(BUTTON_LED_RED, 0)
   # board.digital_write(BUTTON_LED_BLUE, 0)
   # board.analog_write(BUTTON_LED_GREEN, 88)

def reset():
   msgbox.insert(INSERT, "Reset\n")
   root.update()    
   # board.digital_write(TV_REL_DIR, 1)
   # board.digital_write(TV_GEN_DIR, 0)
   # board.digital_write(TV_REL_CTRL, 0)
   # board.analog_write(TV_GEN_CTRL, 0)
   # board.digital_write(SENS_1_REF, 1)
   # board.digital_write(BUTTON_REF, 1)
   # board.digital_write(BUTTON_LED_RED, 0)
   # board.digital_write(BUTTON_LED_BLUE, 0)
   # board.analog_write(BUTTON_LED_GREEN, 25)    
   # board.sleep(2.0)

def setVoltage(value):
   if value=='0':
      # msgbox.insert(INSERT,"Setting voltage to 0V\n")
      value='60'      
   if value=='60':
      # board.analog_write(TV_GEN_CTRL, 08)
      msgbox.insert(INSERT, "Setting voltage to 60V\n")
      root.update()  
   elif value=='100':
      # board.analog_write(TV_GEN_CTRL, 08)
      #msgbox.delete(DELETE)
      msgbox.insert(INSERT, "Setting voltage to 100V\n")
      root.update()
   elif value=='200':
      # board.analog_write(TV_GEN_CTRL, 15)
      #msgbox.delete(1,90)
      msgbox.insert(INSERT, "Setting voltage to 200V\n")
      root.update()
   elif value=='300':
      # board.analog_write(TV_GEN_CTRL, 23)
      msgbox.insert(INSERT, "Setting voltage to 300V\n")
      root.update()
   elif value=='400':
      # board.analog_write(TV_GEN_CTRL, 29)
      msgbox.insert(INSERT, "Setting voltage to 400V\n")
      root.update()
   elif value=='500':
      # board.analog_write(TV_GEN_CTRL, 38)
      msgbox.insert(INSERT, "Setting voltage to 500V\n")
      root.update()
   elif value=='600':
      # board.analog_write(TV_GEN_CTRL, 50)
      msgbox.insert(INSERT, "Setting voltage to 600V\n")
      root.update()
   elif value=='700':
      # board.analog_write(TV_GEN_CTRL, 60)
      msgbox.insert(INSERT, "Setting voltage to 700V\n")
      root.update()
   elif value=='800':
      # board.analog_write(TV_GEN_CTRL, 70)
      msgbox.insert(INSERT, "Setting voltage to 800V\n")
      root.update()
   elif value=='900':
      # board.analog_write(TV_GEN_CTRL, 80)
      msgbox.insert(INSERT, "Setting voltage to 900V\n")
      root.update()
   elif value=='1000':
      # board.analog_write(TV_GEN_CTRL, 90)
      msgbox.insert(INSERT, "Setting voltage to 1000V\n")
      root.update()

def short():
   msgbox.insert(INSERT, "Short\n")
   root.update()
   #print("Short")
   # board.digital_write(TV_REL_DIR, 1)
   # board.digital_write(TV_GEN_DIR, 0)
   # board.digital_write(TV_REL_CTRL, 1)
   # board.analog_write(TV_GEN_CTRL, 0)
   # board.digital_write(SENS_1_REF, 1)
   # board.digital_write(BUTTON_REF, 1)
   # board.digital_write(BUTTON_LED_RED, 1)    
   # board.sleep(2.0)

def short600V():
      msgbox.insert(INSERT, "Short600V\n")
      root.update()  
   #print("Short600V")
   # board.digital_write(TV_REL_DIR, 1)
   # board.digital_write(TV_GEN_DIR, 0)
   # board.digital_write(TV_REL_CTRL, 1)
   # board.analog_write(TV_GEN_CTRL, 50)
   # board.digital_write(SENS_1_REF, 1)
   # board.digital_write(BUTTON_REF, 1)
   # board.digital_write(BUTTON_LED_RED, 1)
    
   # board.sleep(2.0)  
    
def showhelp():
   msgbox.insert(INSERT, "This software runs tests on electrical vehicle training rigs\n")
   root.update()
   
def ESS_Short():
   if var1.get() == 1:
      msgbox.insert(INSERT, "ESS_Short ON\n")
   else:
      msgbox.insert(INSERT, "ESS_Short OFF\n")
   root.update()  
    
def Contactors_Close():
   if var2.get() == 1:
      msgbox.insert(INSERT, "Contactors_Close ON\n")
   else:
      msgbox.insert(INSERT, "Contactors_Close OFF\n")
   root.update() 

def OBC_Insulation():
   if var3.get() == 1:
      msgbox.insert(INSERT, "OBC_Insulation ON\n")
   else:
      msgbox.insert(INSERT, "OBC_Insulation OFF\n")
   root.update() 

def HVIL_JB_Open():
   if var4.get() == 1:
      msgbox.insert(INSERT, "HVIL_JB_Open ON\n")
   else:
      msgbox.insert(INSERT, "HVIL_JB_Open OFF\n")
   root.update() 

def HVIL_DC_Open():
   if var5.get() == 1:
      msgbox.insert(INSERT, "HVIL_DC_Open ON\n")
   else:
      msgbox.insert(INSERT, "HVIL_DC_Open OFF\n")
   root.update() 

def retrieve():
   rig = my_entry.get()
   if rig == 'SN005' or rig == 'SN006':
      evrig_init()
      maingui()
      submit_button.config(state=DISABLED)
   elif rig == 'SN001':
      evsim_init()
      maingui()
      submit_button.config(state=DISABLED)

def maingui():
   button = Button(right_frame, text="Discharge", command=discharge)
   button.pack(padx=5, pady=5)
   button2 = Button(right_frame, text="Reset", command=reset)
   button2.pack(padx=5, pady=5)
   button3 = Button(right_frame, text="Short", command=short, justify=LEFT)
   button3.pack(padx=5, pady=5)
   button4 = Button(right_frame, text="Short600V", command=short600V, justify=LEFT)
   button4.pack(padx=5, pady=5)

   scala = Scale(right_frame, from_=0, to=1000, orient=HORIZONTAL, label="Volt 60 - 1000", resolution="100", relief=RAISED, showvalue=False, command=setVoltage)
   scala.pack(padx=5, pady=15)

   msgbox = Text(root, height=35, width=40)
   msgbox.place(x=20, y=40)
   msgbox.pack()

   ChkBttn1 = Checkbutton(right_frame, text="ESS_Short", variable=var1, relief=RAISED, command=ESS_Short, justify=LEFT)
   ChkBttn1.pack(padx=5, pady=5)

   ChkBttn2 = Checkbutton(right_frame, text="Contactors_Close", variable=var2, justify=LEFT, relief=RAISED, command=Contactors_Close)
   ChkBttn2.pack(padx=5, pady=5)

   ChkBttn3 = Checkbutton(right_frame, text="OBC_Insulation", variable=var3, justify=LEFT, relief=RAISED, command=OBC_Insulation)
   ChkBttn3.pack(padx=5, pady=5)

   ChkBttn4 = Checkbutton(right_frame, text="HVIL_JB_Open", variable=var4, relief=RAISED, command=HVIL_JB_Open, justify=RIGHT)
   ChkBttn4.pack(padx=5, pady=0)

   ChkBttn5 = Checkbutton(right_frame, text="HVIL_DC_Open", variable=var5, relief=RAISED, command=HVIL_DC_Open, justify=LEFT)
   ChkBttn5.pack(padx=5, pady=5)      

root = Tk()
root.geometry("480x640")
frame = Frame(root)
frame.pack()

# left_frame = Frame(root)
# left_frame.pack(side=LEFT)
 
right_frame = Frame(root)
right_frame.pack(side=RIGHT)

my_entry = Entry(frame, width=13)
my_entry.pack(padx=5, pady=5)

submit_button = Button(frame, text="Submit", command=retrieve)
submit_button.pack(padx=5, pady=5)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
msgbox = Text(root, height=35, width=40, yscrollcommand=scrollbar.set)
msgbox.place(x=20, y=40)
msgbox.pack()
scrollbar.config(command=msgbox.yview)

root.title("AMIBA-ALPHA") 
root.mainloop()

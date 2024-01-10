from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
from tkinter import *

board = PyMata3()
SENS_1_PIN=20
SENS_1_REF=19
TV_REL_CTRL=11
TV_REL_DIR=18
TV_GEN_CTRL=10
TV_GEN_DIR=9
BUTTON_PIN=23
BUTTON_REF=22
BUTTON_LED_RED=12
BUTTON_LED_GREEN=13
BUTTON_LED_BLUE=21
HVIL_DC_PIN1=7
HVIL_DC_PIN2=8
HVIL_JB_PIN1=4
HVIL_JB_PIN2=12
TV_OBC_CTRL=5
TV_CON_CTRL=6

# Initializing the big rigs: SN005 and SN006
def evrig_init():
    board.set_pin_mode(SENS_1_PIN, Constants.INPUT)
    board.set_pin_mode(SENS_1_REF, Constants.OUTPUT)
    board.set_pin_mode(HVIL_DC_PIN1, Constants.OUTPUT)
    board.set_pin_mode(HVIL_DC_PIN2, Constants.OUTPUT)
    board.set_pin_mode(HVIL_JB_PIN1, Constants.OUTPUT)
    board.set_pin_mode(HVIL_JB_PIN2, Constants.OUTPUT)
    board.set_pin_mode(TV_OBC_CTRL, Constants.OUTPUT)
    board.set_pin_mode(TV_CON_CTRL, Constants.OUTPUT)
    board.set_pin_mode(TV_REL_CTRL, Constants.OUTPUT)
    board.set_pin_mode(TV_REL_DIR, Constants.OUTPUT)
    board.set_pin_mode(TV_GEN_CTRL, Constants.PWM)
    board.set_pin_mode(TV_GEN_DIR, Constants.OUTPUT)

# Initializing the small rig: SN001
def evsim_init():
    board.set_pin_mode(SENS_1_PIN, Constants.INPUT)
    board.set_pin_mode(SENS_1_REF, Constants.OUTPUT)
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
    board.set_pin_mode(BUTTON_REF, Constants.OUTPUT)
    board.set_pin_mode(BUTTON_LED_RED, Constants.OUTPUT)
    board.set_pin_mode(BUTTON_LED_GREEN, Constants.PWM)
    board.set_pin_mode(BUTTON_LED_BLUE, Constants.OUTPUT)
    board.set_pin_mode(TV_REL_CTRL, Constants.OUTPUT)
    board.set_pin_mode(TV_REL_DIR, Constants.OUTPUT)
    board.set_pin_mode(TV_GEN_CTRL, Constants.PWM)
    board.set_pin_mode(TV_GEN_DIR, Constants.OUTPUT)

# Step by step reduction of the voltage
def discharge():
    msgbox.insert(INSERT, "300V DC Residual Voltage ON \n")
    board.digital_write(TV_REL_DIR, 1)
    board.digital_write(TV_GEN_DIR, 0)
    board.digital_write(TV_REL_CTRL, 0)
    board.analog_write(TV_GEN_CTRL, 21)
    board.digital_write(SENS_1_REF, 1)
    board.digital_write(BUTTON_REF, 1)
    board.digital_write(BUTTON_LED_RED, 1)    
    board.sleep(5.0)  
    msgbox.insert(INSERT, "Residual discharge -ACTIVE-\n")    
    board.digital_write(BUTTON_LED_RED, 0)
    board.digital_write(BUTTON_LED_BLUE, 1)
    board.analog_write(BUTTON_LED_GREEN, 0)
    board.analog_write(TV_GEN_CTRL, 21)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 20)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 19)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 18)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 17)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 16)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 15)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 14)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 13)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 12)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 11)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 10)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 9)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 8)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 7)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 6)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 5)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 4)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 3)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 2)
    board.sleep(3)
    board.analog_write(TV_GEN_CTRL, 1)
    board.sleep(3)
    
    if rig =='SN001':
       board.analog_write(TV_GEN_CTRL, 0)
       board.digital_write(BUTTON_LED_RED, 0)
       board.digital_write(BUTTON_LED_BLUE, 0)
       board.analog_write(BUTTON_LED_GREEN, 88)

    msgbox.insert(INSERT, "Residual discharge -DONE-\n")   

# Resetting the pins
def reset():
    msgbox.insert(INSERT, "Reset\n") 
    board.digital_write(TV_REL_DIR, 1)
    board.digital_write(TV_GEN_DIR, 0)
    board.digital_write(TV_REL_CTRL, 0)
    board.analog_write(TV_GEN_CTRL, 0)
    board.digital_write(SENS_1_REF, 1)
    
    if rig =='SN001':
       board.digital_write(BUTTON_REF, 1)
       board.digital_write(BUTTON_LED_RED, 0)
       board.digital_write(BUTTON_LED_BLUE, 0)
       board.analog_write(BUTTON_LED_GREEN, 25)    
    
    board.sleep(2.0)

# Sets the voltage between 60 and 100 volt
def set_voltage(value):
    if value=='0':
       value='60'  
          
    if value=='60':
       board.analog_write(TV_GEN_CTRL, 10)
       msgbox.insert(INSERT, "Setting voltage to 60V\n")
       root.update()  
      
    elif value=='100':
         board.analog_write(TV_GEN_CTRL, 14)
         msgbox.insert(INSERT, "Setting voltage to 100V\n")
         root.update()
      
    elif value=='200':
         board.analog_write(TV_GEN_CTRL, 18)
         msgbox.insert(INSERT, "Setting voltage to 200V\n")
         root.update()
      
    elif value=='300':
         board.analog_write(TV_GEN_CTRL, 23)
         msgbox.insert(INSERT, "Setting voltage to 300V\n")
         root.update()
      
    elif value=='400':
         board.analog_write(TV_GEN_CTRL, 29)
         msgbox.insert(INSERT, "Setting voltage to 400V\n")
         root.update()
      
    elif value=='500':
         board.analog_write(TV_GEN_CTRL, 38)
         msgbox.insert(INSERT, "Setting voltage to 500V\n")
         root.update()
      
    elif value=='600':
         board.analog_write(TV_GEN_CTRL, 50)
         msgbox.insert(INSERT, "Setting voltage to 600V\n")
         root.update()
      
    elif value=='700':
         board.analog_write(TV_GEN_CTRL, 60)
         msgbox.insert(INSERT, "Setting voltage to 700V\n")
         root.update()
      
    elif value=='800':
         board.analog_write(TV_GEN_CTRL, 70)
         msgbox.insert(INSERT, "Setting voltage to 800V\n")
         root.update()
      
    elif value=='900':
         board.analog_write(TV_GEN_CTRL, 80)
         msgbox.insert(INSERT, "Setting voltage to 900V\n")
         root.update()
    elif value=='1000':
         board.analog_write(TV_GEN_CTRL, 90)
         msgbox.insert(INSERT, "Setting voltage to 1000V\n")
         root.update()

def short():
    msgbox.insert(INSERT, "Short\n")
    board.digital_write(TV_REL_DIR, 1)
    board.digital_write(TV_GEN_DIR, 0)
    board.digital_write(TV_REL_CTRL, 1)
    board.analog_write(TV_GEN_CTRL, 0)
    board.digital_write(SENS_1_REF, 1)
    
    if rig =='SN001':
       board.digital_write(BUTTON_REF, 1)
       board.digital_write(BUTTON_LED_RED, 1)    
    board.sleep(2.0)

def short600V():
    msgbox.insert(INSERT, "Short600V\n") 
    board.digital_write(TV_REL_DIR, 1)
    board.digital_write(TV_GEN_DIR, 0)
    board.digital_write(TV_REL_CTRL, 1)
    board.analog_write(TV_GEN_CTRL, 50)
    board.digital_write(SENS_1_REF, 1)
    
    if rig =='SN001':
       board.digital_write(BUTTON_REF, 1)
       board.digital_write(BUTTON_LED_RED, 1) 
    board.sleep(2.0)  
       
# For these check if rig == 'SN005' or rig == 'SN006':
# def ess_short():
#     if var1.get() == 1:
#        msgbox.insert(INSERT, "ESS_Short ON\n")
#     else:
#        msgbox.insert(INSERT, "ESS_Short OFF\n")
#     root.update()  
    
# def contactors_close():
#     if var2.get() == 1:
#        TV_CON_CTRL=6 (HIGH)
#        msgbox.insert(INSERT, "Contactors_Close ON\n")
#     else:
#        TV_CON_CTRL=6 (LOW)
#        msgbox.insert(INSERT, "Contactors_Close OFF\n")
#     root.update() 

# def obc_insulation():
#     if var3.get() == 1:
#        TV_OBC_CTRL=5 (HIGH)
#        msgbox.insert(INSERT, "OBC_Insulation ON\n")
#     else:
#        TV_OBC_CTRL=5 (LOW)
#        msgbox.insert(INSERT, "OBC_Insulation OFF\n")
#     root.update() 

# def hvil_jb_open():
#     if var4.get() == 1:
#        HVIL_JB_PIN1=4  (HIGH for 1s and back to LOW as normal state)
#        HVIL_JB_PIN2=12 (LOW)
#        msgbox.insert(INSERT, "HVIL_JB_Open ON\n")
#     else:
#        HVIL_JB_PIN1=4 (LOW)
#        HVIL_JB_PIN2=12 (HIGH for 1s and back to LOW as normal state)
#        msgbox.insert(INSERT, "HVIL_JB_Open OFF\n")
#     root.update() 

# def hvil_dc_open():
#     if var5.get() == 1:
#        HVIL_DC_PIN1=7
#        # board.sleep(1.0)
#        HVIL_DC_PIN2=8 (LOW)
#        msgbox.insert(INSERT, "HVIL_DC_Open ON\n")
#     else:
#        HVIL_DC_PIN1=7  (LOW)
#        HVIL_DC_PIN2=8
#        msgbox.insert(INSERT, "HVIL_DC_Open OFF\n")
#     root.update() 

# Gets the value for the chosen rig
def retrieve():
    rig = rig_entry.get()
    if rig == 'SN005' or rig == 'SN006':
       evrig_init()
       s = rig+" initialized\n"
       msgbox.insert(INSERT, s)
       submit_button.config(state=DISABLED)
       rig_entry.config(state=DISABLED)
       maingui()
    elif rig == 'SN001':
         evsim_init()
         s = rig+" initialized\n"
         msgbox.insert(INSERT, s)
         submit_button.config(state=DISABLED)
         rig_entry.config(state=DISABLED)
         maingui()

# The function creates the graphical user interface
def maingui():
    # Create buttons 
    button_discharge = Button(mainframe, text="Discharge", command=discharge)
    button_discharge.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    button_reset = Button(mainframe, text="Reset", command=reset)
    button_reset.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    button_short = Button(mainframe, text="Short", command=short)
    button_short.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    button_short600V = Button(mainframe, text="Short600V", command=short600V)
    button_short600V.grid(row=5, column=0, padx=5, pady=5, sticky=W)     

    # Create scale for setting the voltage
    scala = Scale(mainframe, from_=0, to=1000, orient=HORIZONTAL, label="60V - 1000V", resolution="100", relief=RAISED, showvalue=False, command=set_voltage)
    scala.grid(row=6, column=0, padx=5, pady=5, sticky=W)

    # Create checkbuttons
    chk_button = Checkbutton(mainframe, text="ESS_Short", variable=var1, command=ess_short)
    chk_button.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    chk_button = Checkbutton(mainframe, text="Contactors_Close", variable=var2, command=contactors_close)
    chk_button.grid(row=8, column=0, padx=5, pady=5, sticky=W)
    chk_button = Checkbutton(mainframe, text="OBC_Insulation", variable=var3, command=obc_insulation)
    chk_button.grid(row=9, column=0, padx=5, pady=5, sticky=W)
    chk_button = Checkbutton(mainframe, text="HVIL_JB_Open", variable=var4, command=hvil_jb_open)
    chk_button.grid(row=10, column=0, padx=5, pady=5, sticky=W)
    chk_button = Checkbutton(mainframe, text="HVIL_DC_Open", variable=var5, command=hvil_dc_open)
    chk_button.grid(row=11, column=0, padx=5, pady=5, sticky=W)      
  
root = Tk()
img = PhotoImage(file='favicon.png')
root.iconphoto(False, img)
root.title("AMIBA-ALPHA") 
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
rig_entry = Entry(mainframe, width=13)
rig_entry.grid(row=0, column=0, padx=5, pady=5)
rig_entry.focus()
submit_button = Button(mainframe, text="Submit", command=retrieve)
submit_button.grid(row=1, column=0, padx=5, pady=5)
scrollbar = Scrollbar(mainframe)
scrollbar.grid(row=16, column=1, sticky=NS)
msgbox = Text(mainframe, height=30, width=30, yscrollcommand=scrollbar.set)
msgbox.grid(row=16, column=0, padx=5, pady=5)
scrollbar.config(command=msgbox.yview)

rig = ''
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
root.mainloop()    


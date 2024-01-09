Regarding pins update for Amiba-Alpha (big-rigs) in red:

    SENS_1_PIN=20

    SENS_1_REF=19

    HVIL_DC_PIN1=7

    HVIL_DC_PIN2=8

    HVIL_JB_PIN1=4

    HVIL_JB_PIN2=12

    TV_OBC_CTRL=5

    TV_CON_CTRL=6

    TV_REL_CTRL=11

    TV_REL_DIR=18

    TV_GEN_CTRL=10

    TV_GEN_DIR=9

 

   #  board.set_pin_mode(SENS_1_PIN, Constants.INPUT)

   #  board.set_pin_mode(SENS_1_REF, Constants.OUTPUT)

   #  board.set_pin_mode(HVIL_DC_PIN1, Constants.OUTPUT)

   #  board.set_pin_mode(HVIL_DC_PIN2, Constants.OUTPUT)

   #  board.set_pin_mode(HVIL_JB_PIN1, Constants.OUTPUT)

   #  board.set_pin_mode(HVIL_JB_PIN2, Constants.OUTPUT)

   #  board.set_pin_mode(TV_OBC_CTRL, Constants.OUTPUT)

   #  board.set_pin_mode(TV_CON_CTRL, Constants.OUTPUT)

   #  board.set_pin_mode(TV_REL_CTRL, Constants.OUTPUT)

   #  board.set_pin_mode(TV_REL_DIR, Constants.OUTPUT)

   #  board.set_pin_mode(TV_GEN_CTRL, Constants.PWM)

   #  board.set_pin_mode(TV_GEN_DIR, Constants.OUTPUT)




shortly about expected features:

In case user activates feature HVIL_DC , its expected that system turns this ON
    HVIL_DC_PIN1=7  (HIGH for 1s and back to LOW as normal state)

    HVIL_DC_PIN2=8 (LOW)



In case user deactivates feature HVIL_DC , its expected that system turns this OFF

    HVIL_DC_PIN1=7  (LOW)

    HVIL_DC_PIN2=8 (HIGH for 1s and back to LOW as normal state)



In case user activates feature HVIL_JB , its expected that system turns this ON

    HVIL_JB_PIN1=4  (HIGH for 1s and back to LOW as normal state)
    HVIL_JB_PIN2=12 (LOW)



In case user deactivates feature HVIL_JB , its expected that system turns this OFF


    HVIL_JB_PIN1=4 (LOW)
    HVIL_JB_PIN2=12 (HIGH for 1s and back to LOW as normal state)



In case user activates feature TV_OBC , its expected that system turns this ON
    TV_OBC_CTRL=5 (HIGH)




In case user deactivates feature TV_OBC , its expected that system turns this OFF
    TV_OBC_CTRL=5 (LOW)




In case user activates feature TV_CON , its expected that system turns this ON
    TV_CON_CTRL=6 (HIGH) 

In case user deactivates feature TV_CON , its expected that system turns this OFF
    TV_CON_CTRL=6 (LOW) 

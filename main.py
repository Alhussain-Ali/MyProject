from flask import Flask, render_template, request

# pip install RPi.GPIO

# todo Initialization GPIO PINS
#! ==========================================================================================

# ? ForWard_Pin1 = 18
# ? ForWard_Pin2 = 19


#! BackWard_Pin1 = 20
#! BackWard_Pin2 = 21

# todo Left_Right_Pin1 = 22
# todo Left_Right_Pin2 = 23

#* Vibration_Pin1 = 24
#* Vibration_Pin2 = 25

# ? ForWard_Led1 == 26
# ? ForWard_Led2 == 27

# ? BackWard_Led1 == 28
# ? BackWard_Led2 == 29

# ? Power_Car = 30

#! ==========================================================================================

# GPIO.setmode(GPIO.BCM)

# ? GPIO.setup(ForWard_Pin1, GPIO.OUT)
# ? GPIO.setup(ForWard_Pin2, GPIO.OUT)

# ! GPIO.setup(BackWard_Pin1, GPIO.OUT)
# ! GPIO.setup(BackWard_Pin2, GPIO.OUT)

# todo GPIO.setup(Left_Right_Pin1, GPIO.OUT)
# todo GPIO.setup(Left_Right_Pin2, GPIO.OUT)

# * GPIO.setup(Vibration_Pin1, GPIO.OUT)
# * GPIO.setup(Vibration_Pin2, GPIO.OUT)


# ? GPIO.setup(ForWard_Led1, GPIO.OUT)
# ? GPIO.setup(ForWard_Led2, GPIO.OUT)

# ? GPIO.setup(BackWard_Led1, GPIO.OUT)
# ? GPIO.setup(BackWard_Led2, GPIO.OUT)

# ? GPIO.setup(Power_Car, GPIO.OUT)

#! ==========================================================================================

# todo Pwm_Left_Right_Pin1 = GPIO.PWM(Left_Right_Pin1,100)    // Determine PWM Frequency
# todo Pwm_Left_Right_Pin2 = GPIO.PWM(Left_Right_Pin2,100)    // Determine PWM Frequency

# ? Pwm_ForWard_Pin1 = GPIO.PWM(ForWard_Pin1,100)    // Determine PWM Frequency
# ? Pwm_ForWard_Pin2 = GPIO.PWM(ForWard_Pin2,100)    // Determine PWM Frequency

# ! Pwm_BackWard_Pin1 = GPIO.PWM(BackWard_Pin1,100)    // Determine PWM Frequency
# ! Pwm_BackWard_Pin2 = GPIO.PWM(BackWard_Pin2,100)    // Determine PWM Frequency

# * Pwm_Vibration_Pin1 = GPIO.PWM(Vibration_Pin1,100)    // Determine PWM Frequency
# * Pwm_Vibration_Pin2 = GPIO.PWM(Vibration_Pin2,100)    // Determine PWM Frequency

#! ==========================================================================================

# todo duty_cycle = 50
#!note
# todo If The Value of duty_cycle is 0   --> output is Zero
# todo If The Value of duty_cycle is 100 --> output is Full

app = Flask(__name__)

#! ==========================================================================================
# * Put Initial Value To The Led And Actuators

# ? GPIO.output(ForWard_Led1, GPIO.LOW)
# ? GPIO.output(ForWard_Led2, GPIO.LOW)

# ? GPIO.output(ForWard_Led1, GPIO.LOW)
# ? GPIO.output(BackWard_Led2, GPIO.LOW)

# ? GPIO.output(Power_Car, GPIO.LOW)

    # ? Pwm_ForWard_Pin1.stop()
    # ? Pwm_ForWard_Pin2.stop()

    #! Pwm_BackWard_Pin1.stop()
    #! Pwm_BackWard_Pin2.stop()

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

#! ==========================================================================================

@app.route("/")
def home():
    return render_template("index.html")

slider_value = 0

@app.route("/get_value", methods=["POST"])
def get_value():
    data = request.get_json()
    slider_value = data["value"]
    print("Slider value:", slider_value)  # Show The Speed Value Inside The Terminal
    return "", 204


@app.route("/ForWard")
def sendFront():
    print("ForWard")

    # ? Pwm_ForWard_Pin1.start(slider_value)
    # ? Pwm_ForWard_Pin2.start(0)

    # ! Pwm_BackWard_Pin1.start(0)
    # ! Pwm_BackWard_Pin2.start(slider_value)

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

    return "success"


@app.route("/BackWard")
def sendBack():
    print("BackWard")

    # ? Pwm_ForWard_Pin1.start(slider_value)
    # ? Pwm_ForWard_Pin2.start(0)

    #! Pwm_BackWard_Pin1.start(0)
    #! Pwm_BackWard_Pin2.start(slider_value)

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

    return "success"


@app.route("/Left")
def sendLeft():
    print("Left")

    # ? Pwm_ForWard_Pin1.stop()
    # ? Pwm_ForWard_Pin2.stop()

    #! Pwm_BackWard_Pin1.stop()
    #! Pwm_BackWard_Pin2.stop()


    # todo Pwm_Left_Right_Pin1.start(duty_cycle)
    # todo Pwm_Left_Right_Pin2.stop()
      
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

    return "success"


@app.route("/Right")
def sendRight():
    print("Right")
    
    # ? Pwm_ForWard_Pin1.stop()
    # ? Pwm_ForWard_Pin2.stop()

    #! Pwm_BackWard_Pin1.stop()
    #! Pwm_BackWard_Pin2.stop()

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.start(duty_cycle)
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

    return "success"


@app.route("/Stop")
def sendStop():
    print("Stop")

    # ? Pwm_ForWard_Pin1.stop()
    # ? Pwm_ForWard_Pin2.stop()

    #! Pwm_BackWard_Pin1.stop()
    #! Pwm_BackWard_Pin2.stop()

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.stop()

    return "success"


@app.route("/V_motor")
def V_motor():
    print("V_motor")

    # ? Pwm_ForWard_Pin1.stop()
    # ? Pwm_ForWard_Pin2.stop()

    #! Pwm_BackWard_Pin1.stop()
    #! Pwm_BackWard_Pin2.stop()

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()
    
    # * Pwm_Vibration_Pin1.stop()
    # * Pwm_Vibration_Pin2.start(slider_value)

    return "success"



@app.route("/forwardLed")
def forwardLed():
    print("forwardLed")
    
    # ? GPIO.output(ForWard_Led1, GPIO.HIGH)
    # ? GPIO.output(ForWard_Led2, GPIO.HIGH)
    
    return "success"

@app.route("/backwardLed")
def backwardLed():
    print("backwardLed")
    
    # ? GPIO.output(ForWard_Led1, GPIO.HIGH)
    # ? GPIO.output(BackWard_Led2, GPIO.HIGH)

    return "success"

@app.route("/power")
def power():
    print("power")
    
    # ? GPIO.output(Power_Car, GPIO.HIGH)

    return "success"

if __name__ == "__main__":
    # app.run(debug=True, port=80)
    app.run(host="0.0.0.0", port=9000)


@app.route("/buzzer")
def buzzer():
    print("buzzer")

    return "success"

@app.route("/music")
def music():
    print("music")

    return "success"

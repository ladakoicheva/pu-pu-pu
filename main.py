
lamp_is_on = 230
lamp_is_blinking = 210
lamp_is_off = 100


def lamp(voltage):
    if 220 <= voltage <= 240:
        print('лампа горит')
    elif 190 <= voltage <= 210:
        print('лампа мерцает ')
    elif voltage <= 100:
        print('лампа погасла')
    else:
        print('все пропалооо ужас')


lamp(lamp_is_on)
lamp(lamp_is_blinking)
lamp(lamp_is_off)

import math

def Gen_Onda(x, f, a, duty_porc, offset, tipo_senal):
    t = x / 512
    T = 1 / f
    volt = 0

    if tipo_senal == 'cuadrada':
        if t % T <= duty_porc / (100 * f):
            volt = a / 2
        else:
            volt = -a / 2

    elif tipo_senal == 'sawtooth':
        period = T
        phase = (t % period) / period
        volt = -a / 2 + a * phase

    elif tipo_senal == 'senoidal':
        volt = a * math.sin(2 * math.pi * f * t)

    elif tipo_senal == 'triangular':
        period = T
        phase = (t % period) / period
        if phase < 0.25:
            volt = -a / 2 + 4 * a * phase
        elif phase < 0.75:
            volt = a / 2 - 4 * a * (phase - 0.25)
        else:
            volt = -a / 2 + 4 * a * (phase - 0.75)

    voltaje = volt + offset


    return int(6.4 * voltaje + 64)
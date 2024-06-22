import datetime
import ephem

# Obtener la fecha actual
hoy = datetime.date.today()

# Configurar la observación en Madrid, España
madrid = ephem.Observer()
madrid.lat, madrid.lon = '40.4165', '-3.70256'  # Coordenadas de Madrid

# Obtener la fase lunar
luna = ephem.Moon(madrid)
luna.compute(hoy)

# Determinar la fase lunar y asignar el emoji correspondiente
edad_lunar = luna.phase

if edad_lunar == 0:
    fase = "Luna Nueva"
    emoji = "🌑"
elif 0 < edad_lunar < 7.4:
    fase = "Luna Creciente"
    emoji = "🌒"
elif 7.4 <= edad_lunar < 14.8:
    fase = "Luna Llena"
    emoji = "🌕"
elif 14.8 <= edad_lunar < 22.1:
    fase = "Luna Menguante"
    emoji = "🌗"
else:
    fase = "Luna Nueva"
    emoji = "🌑"

# Mostrar la información
print(f"Fecha: {hoy}")
print(f"Fase Lunar: {fase} {emoji}")

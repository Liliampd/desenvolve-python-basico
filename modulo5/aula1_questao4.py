import datetime

agora = datetime.datetime.now()

data_formatada = f"{agora.day:02}/{agora.month:02}/{agora.year}"
hora_formatada = f"{agora.hour:02}:{agora.minute:02}"

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")

import qrcode

# URL de tu API en localhost
api_url = 'http://127.0.0.1:8000'

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agregar los datos (en este caso, la URL de tu API)
qr.add_data(api_url)
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen del código QR
img.save('codigo_qr_api.png')

print("Se ha generado exitosamente el código QR.")

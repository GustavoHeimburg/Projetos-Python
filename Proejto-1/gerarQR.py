import qrcode
from PIL import Image

#URL do QRCode
data = "https://www.instagram.com/santapedraimobiliaria/"

# Criando o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Gerando a imagem do QR Code
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

logo = Image.open('iamgeone.jpg').convert("RGBA")

qr_width, qr_height = qr_img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

mask = logo.split()[3]

logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

qr_img.paste(logo, logo_position, mask=mask)

qr_img.save('qrcode_personalizado.png')

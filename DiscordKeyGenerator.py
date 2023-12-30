import requests

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
                                                        #añadir aqui el numero de promocion
promo_url = 'https://discord.com/billing/partner-promotions/        /'  # URL a agregar


headers = {
    #añadir url en cbash
    #añadir url en cbash
    #añadir url en cbash
    #añadir url en cbash

}

data = {
    #añadir url en cbash
}

# Cantidad de codigos para generar
num_solicitudes = 100

# Cadena para acumular los tokens
tokens_acumulados = ''

for _ in range(num_solicitudes):
    response = requests.post(url, headers=headers, json=data)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
         # Analizar la respuesta JSON
        json_response = response.json()
        
        # Extraer el token
        token = json_response.get('token', '')

        # Agregar la URL antes de cada token y acumularlo
        tokens_acumulados += f'{promo_url}{token}\n'
    else:
        print(f'Error en la solicitud {_ + 1}: {response.status_code}')

# Guardar todos los tokens en un solo archivo
with open('tokens.txt', 'w') as file:
    file.write(tokens_acumulados)

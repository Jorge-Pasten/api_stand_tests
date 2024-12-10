#Información que se envía en la solicitud
headers = {
    "Content-Type": "application/json"
} #Encabezado de solicitud POST

#Cuerpo de solicitud POST
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

#Diccionario con id de productos
product_ids = {
    "ids": [1, 2, 3]
}
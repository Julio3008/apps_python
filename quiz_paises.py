capitales = {
    "España": "Madrid",
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "Reino Unido": "Londres",
    "Japon": "Tokio",
    "China": "Pekin",
    "India": "Nueva Delhi",
    "Brasil": "Brasilia",
    "Argentina": "Buenos Aires",
}

def quiz_capitales():
    print("Bienvenido al quiz de capitales")
    score = 0
    for pais, capital in capitales.items():
        print(f"\n ¿Cual es la capital de {pais}?")
        user_answer = input("Respuesta: ")

        if user_answer.lower() == capital.lower():
            print("Correcto!, ganastes un punto")
            score += 1
        else:
            print(f"Incorrecto, la capital de {pais} es {capital}")
    print(f"\n Fin del quiz, tu puntuacion final es: {score}/{len(capitales)}")

quiz_capitales()
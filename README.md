# Colección de Aplicaciones Python

Este repositorio contiene una colección de aplicaciones útiles desarrolladas en Python para diferentes propósitos.

## Aplicaciones

### 1. Alarma (alarma.py)

Una aplicación que reproduce un sonido después de un tiempo determinado.

- Permite configurar minutos y segundos para la alarma
- Reproduce un archivo MP3 cuando se cumple el tiempo

### 2. Generador de Códigos QR (generador_codigo.py)

Crea imágenes de códigos QR a partir de URLs.

- Genera códigos QR personalizables
- Guarda el resultado como imagen PNG

### 3. Enviador de Correos (mandarcorreos.py)

Envía correos electrónicos de forma automatizada.

- Configura remitente, destinatario y mensaje
- Utiliza el protocolo SMTP para el envío

### 4. Traductor (traductor.py)

Traduce texto del español al inglés.

- Interfaz simple para ingresar el texto a traducir
- Muestra el resultado de la traducción

### 5. Bot de Ratón (bot_raton.py)

Automatiza movimientos del cursor y clics del ratón.

- Abre un navegador web con una URL específica
- Mueve el cursor a coordenadas predefinidas
- Realiza clics automáticos

### 6. Quiz de Países (quiz_paises.py)

Juego de preguntas sobre países.

- Pone a prueba conocimientos geográficos
- Sistema de puntuación

### 7. Generador de Contraseñas (Generador_password.py)

Crea contraseñas seguras aleatorias.

- Genera contraseñas con caracteres variados
- Útil para mejorar la seguridad de cuentas

### 8. Sistema de Login (login.py)

Implementa un sistema básico de inicio de sesión.

- Verifica credenciales de usuario
- Control de acceso

### 9. Apagado de PC (apagar_pc.py)

Programa el apagado automático del ordenador.

- Permite configurar el tiempo antes del apagado
- Útil para ahorrar energía

### 10. Reconocimiento de Voz (reconocimiento_voz.py)

Convierte voz en texto utilizando el micrófono.

- Captura audio desde el micrófono
- Transcribe el habla a texto

## Requisitos

- Python 3.x
- Bibliotecas específicas para cada aplicación:
  - playsound
  - qrcode
  - PIL (Pillow)
  - smtplib
  - translate
  - pyautogui
  - speech_recognition
  - webbrowser
  - random
  - time
  - os

## Uso

Ejecuta cada aplicación individualmente con Python:

```
python alarma.py
python generador_codigo.py
python mandarcorreos.py
python traductor.py
python bot_raton.py
python quiz_paises.py
python Generador_password.py
python login.py
python apagar_pc.py
python reconocimiento_voz.py
```

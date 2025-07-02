import os
shutdown=input("Quieres apagar el pc? (si/no): ")
if shutdown.lower()=="si":
    os.system("shutdown /s /t 1")
else:
    exit()
#Para realizar esta evidencia, se reutilizó un menú que fue parte de una actividad práctica el semestre anterior,
# en el cual cambiamos sus funciones para que se ajusten a la evidencia actual

while True:
    print(" ")
    print("-"*50)
    print("Servicio de soporte técnico")
    print("-"*50)
    print("[a] Registrar un servicio")
    print("[b] Consultar un servicio")
    print("[f] Consultar los servicios realizados en una fecha específica")
    print("[x] Salir")
    opcion=input("Qué opción deseas: ")
    if (opcion=="x"):
        break
    if (opcion=="a"):
        RegistroServicio()
    if (opcion=="b"):
        ConsultaServicio()
    if (opcion=="f"):
        ServicioFecha()

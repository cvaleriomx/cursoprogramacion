# Diccionario para almacenar los jugadores
jugadores = {}

def agregar_jugador(id_jugador, nombre):
    # Agregar un nuevo jugador al diccionario
    jugadores[id_jugador] = {
        'nombre': nombre,
        'goles': 0,
        'asistencias': 0,
        'tarjetas_amarillas': 0,
        'tarjetas_rojas': 0,
        'partidos_jugados': 0,
        'nacionalidad': "nA",
    }
    print(f"Jugador {nombre} agregado con éxito.")

def actualizar_estadisticas(id_jugador, goles=0, asistencias=0,
                            amarillas=0, rojas=0, partidos=0,nacionalidad="nA"):
    # Actualiza las estadísticas del jugador
    if id_jugador in jugadores:
        jugador = jugadores[id_jugador]
        jugador['goles'] += goles
        jugador['asistencias'] += asistencias
        jugador['tarjetas_amarillas'] += amarillas
        jugador['tarjetas_rojas'] += rojas
        jugador['partidos_jugados'] += partidos
        jugador['nacionalidad'] =nacionalidad 

        print(f"Estadísticas actualizadas para {jugador['nombre']}.")
    else:
        print("Jugador no encontrado.")

def mostrar_jugadores():
    # Muestra todos los jugadores y sus estadísticas
    for id, datos in jugadores.items():
        print(f"ID: {id}, Nombre: {datos['nombre']}, Goles: {datos['goles']}, "
              f"Asistencias: {datos['asistencias']}, Amarillas: {datos['tarjetas_amarillas']}, "
              f"Rojas: {datos['tarjetas_rojas']}, Partidos: {datos['partidos_jugados']}")
        print("==========================================")
# Agregar jugadores
agregar_jugador(1, "Lionel Messi")
agregar_jugador(2, "Cristiano Ronaldo")
agregar_jugador(98, "rodri")
agregar_jugador(70, "xavi")
actualizar_estadisticas(98,nacionalidad="Espanola")
actualizar_estadisticas(70,nacionalidad="Espanola")


# Actualizar estadísticas
actualizar_estadisticas(1, goles=5, asistencias=10, partidos=10)
actualizar_estadisticas(1,3,rojas=2)

actualizar_estadisticas(2, goles=4, amarillas=1, partidos=10)

# Mostrar información de todos los jugadores
mostrar_jugadores()
print(jugadores)

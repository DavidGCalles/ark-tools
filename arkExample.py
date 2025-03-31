from mcrcon import MCRcon
import os

# Configuración de conexión RCON
RCON_HOST = os.getenv("ARK_HOST_IP")
RCON_PORT = os.getenv("ARK_HOST_PORT")
RCON_PASSWORD = os.getenv("ARK_RCON_PASSWORD")

def get_players():
    """
    Obtiene la lista de jugadores en el servidor ARK.
    """
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        print("Conectado al servidor ARK")
        # Enable cheats with the admin password
        mcr.command(f"EnableCheats {RCON_PASSWORD}")
        response = mcr.command("ListPlayers")
        return response
    

print(get_players())
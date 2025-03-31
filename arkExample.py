from mcrcon import MCRcon
import os

# Configuración de conexión RCON
RCON_HOST = os.getenv("ARK_HOST_IP")
RCON_PORT = int(os.getenv("ARK_HOST_PORT"))
RCON_PASSWORD = os.getenv("ARK_RCON_PASSWORD")

def get_players():
    """
    Obtiene la lista de jugadores en el servidor ARK.
    """
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        print("Conectado al servidor ARK: Obteniendo jugadores...")
        # Enable cheats with the admin password
        mcr.command(f"EnableCheats {RCON_PASSWORD}")
        response = mcr.command("ListPlayers")
        split_response = response.split("\n")
        players = []
        for line in split_response:
            try:
                if isinstance(int(line[0]), int):
                    infoPlayer = {
                        "id": line.split(",")[-1].strip(),
                        "name": line.split(".")[1].split(",")[0].strip()
                    }
                    players.append(infoPlayer)
            except:
                pass
        return players

    

print(get_players())
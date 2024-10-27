import requests
import json
from ..errors.customerror import *

def get_player_uuid(player_name: str) -> str:
    """Get the UUID of a Minecraft player by their name
    
    Parameters
    -----------
    player_name: str
        The name of the player to query
    """
    url = f"https://api.mojang.com/users/profiles/minecraft/{player_name}"
    response = requests.get(url)
    if response.status_code == 204:
        return None
    if response.status_code != 200:
        raise IDNotFound(player_name)
    return json.loads(response.text)["id"]

def get_player_info(player_uuid: str, player_time_stamps: int = None) -> dict:
    """Get the information of a Minecraft player by their UUID
    
    Parameters
    -----------
    player_uuid: str
        The UUID of the player to query
    player_time_stamps: int
        The time stamp of the player
    """
    base_url = "https://sessionserver.mojang.com/session/minecraft/profile/"
    if player_time_stamps != None:
        args = f"?at={player_time_stamps}"
    else:
        args = ""
    response = requests.get(f"{base_url}{player_uuid}{args}")
    return json.loads(response.text)
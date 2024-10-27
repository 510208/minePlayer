import logging
from .useravatar import UserAvatar
from .info.info import get_player_uuid, get_player_info

logger = logging.getLogger(__name__)

class MinePlayer():
    """A class to represent a Minecraft player.

    Parameters:
    - username (str): The player's username
    
    Attributes:
    - username (str): The player's username.
    - uuid (str): The player's UUID.
    - info (dict): The player's information.
    - useravatar (UserAvatar): The player's avatar.
    """
    def __init__(self, username: str):
        """Constructs all the necessary attributes for the player object.
        
        Parameters:
        - username (str): The player's username.
        """
        self.username = username
        self.uuid = get_player_uuid(username)
        self.info = get_player_info(self.uuid)
        self.useravatar = UserAvatar(self.uuid)
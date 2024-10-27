class IDNotFound(Exception):
    """
    Raised when the ID of a player is not found
    """
    def __init__(self, message):
        self.message = f"Can't found this player: {message}"
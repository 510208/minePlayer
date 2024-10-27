class UserAvatar():
    def __init__(self, user_uuid: str, api_path: str = "https://crafatar.com"):
        """Get the avatar URL of a Minecraft user by their UUID
        
        Parameters
        -----------
        user_uuid: str
            The UUID of the user to query
        api_path: str
            The path of the API"""
        self.user_uuid = user_uuid
        self.avatar = f"{api_path}/avatars/{user_uuid}"
        self.avatar_overlay = f"{api_path}/avatars/{user_uuid}?overlay"
        self.head_render = f"{api_path}/renders/head/{user_uuid}"
        self.head_render_overlay = f"{api_path}/renders/head/{user_uuid}?overlay"
        self.body_render = f"{api_path}/renders/body/{user_uuid}"
        self.body_render_overlay = f"{api_path}/renders/body/{user_uuid}?overlay"
        self.skin = f"{api_path}/skins/{user_uuid}"
        self.cape = f"{api_path}/capes/{user_uuid}"

    def change_avatar_provider(self, api_path: str):
        """Change the avatar provider
        
        Parameters
        -----------
        api_path: str
            The path of the API"""
        self.avatar = f"{api_path}/avatars/{self.user_uuid}"
        self.avatar_overlay = f"{api_path}/avatars/{self.user_uuid}?overlay"
        self.head_render = f"{api_path}/renders/head/{self.user_uuid}"
        self.head_render_overlay = f"{api_path}/renders/head/{self.user_uuid}?overlay"
        self.body_render = f"{api_path}/renders/body/{self.user_uuid}"
        self.body_render_overlay = f"{api_path}/renders/body/{self.user_uuid}?overlay"
        self.skin = f"{api_path}/skins/{self.user_uuid}"
        self.cape = f"{api_path}/capes/{self.user_uuid}"

"""Thank you to "https://crafatar.com" for providing avatars."""
import mineplayer
import logging

logging.basicConfig(level=logging.INFO)

# Create a new player
logging.info("=== Create a new player. ===")
player = mineplayer.MinePlayer("Sam510208")
logging.info(f"Player {player.username} created.")

# Get the player's UUID
logging.info("=== Get the player's UUID. ===")
uuid = player.uuid
logging.info(f"Player {player.username}'s UUID is {uuid}.")

# Get the player's information
logging.info("=== Get the player's information. ===")
info = player.info
logging.info(f"Player {player.username}'s information is {info}.")

# Get the player's avatar
logging.info("=== Get the player's avatar. ===")
avatar = player.useravatar
player_avatar = avatar.avatar
player_avatar_overlay = avatar.avatar_overlay
head_render = avatar.head_render
head_render_overlay = avatar.head_render_overlay
body_render = avatar.body_render
body_render_overlay = avatar.body_render_overlay
skin = avatar.skin
cape = avatar.cape
logging.info(f"Player {player.username}'s avatar is {player_avatar}.")
logging.info(f"Player {player.username}'s avatar with overlay is {player_avatar_overlay}.")
logging.info(f"Player {player.username}'s head render is {head_render}.")
logging.info(f"Player {player.username}'s head render with overlay is {head_render_overlay}.")
logging.info(f"Player {player.username}'s body render is {body_render}.")
logging.info(f"Player {player.username}'s body render with overlay is {body_render_overlay}.")
logging.info(f"Player {player.username}'s skin is {skin}.")
logging.info(f"Player {player.username}'s cape is {cape}.")

"""
The avatar service is provided by "https://crafatar.com".
"""
logging.info("=== Change the avatar provider. ===")
# Use another avatar provider(https://crafatar.icehost.xyz, Don't let the uel end with "/")
player.useravatar.change_avatar_provider("https://crafatar.icehost.xyz")
avatar = player.useravatar
player_avatar = avatar.avatar
player_avatar_overlay = avatar.avatar_overlay
head_render = avatar.head_render
head_render_overlay = avatar.head_render_overlay
body_render = avatar.body_render
body_render_overlay = avatar.body_render_overlay
skin = avatar.skin
cape = avatar.cape
logging.info(f"Player {player.username}'s avatar is {player_avatar}.")
logging.info(f"Player {player.username}'s avatar with overlay is {player_avatar_overlay}.")
logging.info(f"Player {player.username}'s head render is {head_render}.")
logging.info(f"Player {player.username}'s head render with overlay is {head_render_overlay}.")
logging.info(f"Player {player.username}'s body render is {body_render}.")
logging.info(f"Player {player.username}'s body render with overlay is {body_render_overlay}.")
logging.info(f"Player {player.username}'s skin is {skin}.")
logging.info(f"Player {player.username}'s cape is {cape}.")

# Raise an exception
logging.info("=== Raise an exception. ===")
try:
    player = mineplayer.MinePlayer("ajepajijcoerppevrup38825pao")
except Exception as e:
    logging.error(f"An exception occurred: {e}")
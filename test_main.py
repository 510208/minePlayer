# Import necessary libraries
import pytest
from mineplayer import MinePlayer, UserAvatar


def test_create_player():
    """Test creating a new player object with a valid username."""
    player = MinePlayer("Sam510208")
    assert player.username == "Sam510208"
    assert isinstance(player.uuid, str)  # Check if UUID is a string


def test_player_info():
    """Test retrieving a player's UUID and information."""
    player = MinePlayer("Sam510208")
    assert player.uuid
    assert player.info  # No need to check specific content


def test_player_avatar():
    """Test retrieving different avatar URLs for a player."""
    player = MinePlayer("Sam510208")
    avatar = player.useravatar
    assert avatar.avatar
    assert avatar.avatar_overlay
    assert avatar.head_render
    assert avatar.head_render_overlay
    assert avatar.body_render
    assert avatar.body_render_overlay
    assert avatar.skin
    assert avatar.cape  # No need to check specific URLs


def test_change_avatar_provider():
    """Test changing the avatar provider and updating URLs."""
    player = MinePlayer("Sam510208")
    original_avatar = player.useravatar.avatar
    player.useravatar.change_avatar_provider("https://crafatar.icehost.xyz")
    new_avatar = player.useravatar.avatar
    assert original_avatar != new_avatar  # Check URLs are different


def test_invalid_username():
    """Test handling an invalid username."""
    with pytest.raises(Exception):
        MinePlayer("ajepajijcoerppevrup38825pao")  # Replace with any invalid username

def test_invalid_avatar_provider():
    """Test handling an invalid avatar provider."""
    player = MinePlayer("Sam510208")
    with pytest.raises(Exception):
        player.useravatar.change_avatar_provider("https://crafatar.icehost.xyz")
        # Assert that the avatar URLs are not updated
        assert player.useravatar.avatar == "https://crafatar.icehost.xyz/avatars/Sam510208"
        assert player.useravatar.avatar_overlay == "https://crafatar.icehost.xyz/avatars/Sam510208?overlay"
        assert player.useravatar.head_render == "https://crafatar.icehost.xyz/renders/head/Sam510208"
        assert player.useravatar.head_render_overlay == "https://crafatar.icehost.xyz/renders/head/Sam510208?overlay"
        assert player.useravatar.body_render == "https://crafatar.icehost.xyz/renders/body/Sam510208"
        assert player.useravatar.body_render_overlay == "https://crafatar.icehost.xyz/renders/body/Sam510208?overlay"
        assert player.useravatar.skin == "https://crafatar.icehost.xyz/skins/Sam510208"
        assert player.useravatar.cape == "https://crafatar.icehost.xyz/capes/Sam510208"

    with pytest.raises(Exception):
        # 提供沒有https開頭的URL，檢查是否有加上https://
        player.useravatar.change_avatar_provider("crafatar.icehost.xyz")
        # Assert that the avatar URLs are updated
        assert player.useravatar.avatar == "https://crafatar.icehost.xyz/avatars/Sam510208"
        assert player.useravatar.avatar_overlay == "https://crafatar.icehost.xyz/avatars/Sam510208?overlay"
        assert player.useravatar.head_render == "https://crafatar.icehost.xyz/renders/head/Sam510208"
        assert player.useravatar.head_render_overlay == "https://crafatar.icehost.xyz/renders/head/Sam510208?overlay"
        assert player.useravatar.body_render == "https://crafatar.icehost.xyz/renders/body/Sam510208"
        assert player.useravatar.body_render_overlay == "https://crafatar.icehost.xyz/renders/body/Sam510208?overlay"
        assert player.useravatar.skin == "https://crafatar.icehost.xyz/skins/Sam510208"
        assert player.useravatar.cape == "https://crafatar.icehost.xyz/capes/Sam510208"

# Run the tests
if __name__ == "__main__":
    pytest.main(["--html", "test_result\\index.html"])
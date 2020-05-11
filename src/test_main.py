"""Test for Http function."""


def test_client():
    """Test returns messages shorter than one buffer in length."""
    from client import client
    assert client('running') == 'running'

"""Auth unit tests."""
from angel_cli.core.auth import hash_password, verify_password


def test_hash_and_verify() -> None:
    password = "test-password"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

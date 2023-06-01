from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    assert encrypt_message("teste", 5) == "etset"
    assert encrypt_message("abcde", 2) == "edc_ba"
    assert encrypt_message("abcde", 3) == "cba_ed"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcde", "1")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(12345, 1)

    

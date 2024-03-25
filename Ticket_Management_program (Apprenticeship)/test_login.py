import pytest
from Start_here import main


def login_valid_inputs(prompt):
    responses = {
        ": ": "1",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


def login_invalid_inputs(prompt):
    responses = {
        ": ": "1",
        ": ": "1",
        "Username: ": "A",
        "Password: ": "A",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


def test_login_valid(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Login system")
        monkeypatch.setattr("builtins.input", login_valid_inputs)

        output = main()
        assert output == ""


def test_login_invalid(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Login system")
        monkeypatch.setattr("builtins.input", login_invalid_inputs)

        output = main()
        assert output == ""

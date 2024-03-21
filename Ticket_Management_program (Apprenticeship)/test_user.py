import pytest
from Start_here import main

# ------------
# Test Inputs:
# ------------


def inputs_user_creation_pass(prompt):
    responses = {
        ": ": "2",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Please enter a new username: ": "pyTest_user",
        "Please enter a password for the new user: ": "pyTest_pwd",
        "Please enter your password again: ": "pyTest_pwd",
        ": ": "1",
    }
    return responses.get(prompt, "")


def inputs_user_creation_fail(prompt):
    responses = {
        ": ": "2",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Please enter a new username: ": "Admin",
        "Please enter a password for the new user: ": "Admin",
        "Please enter your password again: ": "pyTest_pwd",
        ": ": "1",
    }
    return responses.get(prompt, "")


def inputs_user_deletion_pass(prompt):
    responses = {
        ": ": "2",
        ": ": "2",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Username:": "pyTest_user",
        ": ": "Y",
        "Do you want to delete another user? (Y/N)": "N",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


def inputs_user_deletion_fail(prompt):
    responses = {
        ": ": "3",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Username:": "TEST_FAIL",
        "Username:": "pyTest_user",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# --------------------
# User Creation tests:
# --------------------


def test_user_creation_pass(monkeypatch):
    with pytest.raises(RecursionError):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", inputs_user_creation_pass)

        output = main()
        assert output == ""
        print("TEST: Passed")


def test_user_creation_fail(monkeypatch):
    with pytest.raises(RecursionError):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", inputs_user_creation_fail)

        output = main()
        assert output == "Press <ENTER> to continue"
        print("TEST: Passed")


# --------------------
# User Deletion tests:
# --------------------


def test_user_deletion_pass(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", inputs_user_deletion_fail)

        output = main()
        assert output == "Press <ENTER> to continue"
        print("TEST: Passed")


def test_user_deletion_fail(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", inputs_user_deletion_fail)

        output = main()
        assert output == "Press <ENTER> to continue"
        print("TEST: Passed")

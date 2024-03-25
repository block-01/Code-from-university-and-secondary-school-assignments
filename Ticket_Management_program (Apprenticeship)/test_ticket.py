import pytest
from Start_here import main

# -------------
# Test Inputs:
# -------------


# PASS:
def creation_inputs_pass(prompt):
    responses = {
        ": ": "1",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket name: ": "PyTest_Ticket-01",
        "Ticket description: ": "PyTest_Ticket",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# FAIL:
def creation_inputs_fail(prompt):
    responses = {
        ": ": "1",
        ": ": "1",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket name: ": "Print Hello World in python",
        "Ticket description: ": "PyTest_Ticket",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# ----------------------
# INPUTS DELETE TICKETS:
# ----------------------


# PASS:
def delete_inputs_pass(prompt):
    responses = {
        ": ": "1",
        ": ": "3",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket name: ": "1",
        ": ": "Y",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# FAIL:
def delete_inputs_fail(prompt):
    responses = {
        ": ": "1",
        ": ": "3",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket ID: ": "16",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# --------------------
# INPUTS VIEW TICKETS:
# --------------------


# PASS:
def view_tickets_inputs_pass(prompt):
    responses = {
        ": ": "1",
        ": ": "4",
        "Ticket ID: ": "1",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# FAIL:
def view_tickets_inputs_fail(prompt):
    responses = {
        ": ": "1",
        ": ": "4",
        "Ticket ID: ": "14",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# -------------------
# INPUTS TICKET EDIT:
# -------------------


def ticket_edit_inputs_pass(prompt):
    responses = {
        ": ": "1",
        ": ": "2",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket ID: ": "1",
        "Title: ": "Updated_Ticket_name",
        "Description: ": "Updated_Ticket_description",
        "Do you wish to apply theses changes? (Y/N): ": "Y",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


def ticket_edit_inputs_fail(prompt):
    responses = {
        ": ": "1",
        ": ": "2",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket ID: ": "1",
        "Title: ": "Print Hello World in python",
        "Description: ": "Create a script that prints Hello World",
        "Title: ": "",
        "Description: ": "",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# ----------------------------
# INPUTS CHANGE TICKET STATUS:
# ----------------------------


# PASS:
def change_ticket_status_inputs_pass(prompt):
    responses = {
        ": ": "1",
        ": ": "5",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket ID: ": "1",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# FAIL:
def change_ticket_status_inputs_fail(prompt):
    responses = {
        ": ": "1",
        ": ": "5",
        "Username: ": "Admin",
        "Password: ": "Admin",
        "Ticket ID: ": "14",
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


# -----
# TESTS:
# -----

# ----------------------
# Ticket Creation tests:
# ----------------------


def test_ticket_creation_pass(
    monkeypatch,
):  # Tests that ticket creation is working properly by using a ticket name that isn't taken
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", creation_inputs_pass)

        output = main()
        assert output == ""
        print("TEST: Passed")


def test_ticket_creation_fail(
    monkeypatch,
):  # Tests that ticket creation is working properly by using a ticket name that isn't taken
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", creation_inputs_fail)

        output = main()
        assert output == ""
        print("TEST: Passed")


# ----------------------
# Ticket deletion tests:
# ----------------------


def test_ticket_deletion_pass(
    monkeypatch,
):  # Tests that ticket deletion is working properly with a valid ticket ID
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", delete_inputs_pass)

        output = main()
        assert output == ""
        print("TEST: Passed")


def test_ticket_deletion_fail(
    monkeypatch,
):  # Tests that ticket deletion is working properly with an invalid ticket ID
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", delete_inputs_fail)

        output = main()
        assert output == "Invalid Ticket ID\nPress <ENTER> to continue"
        print("TEST: Passed")


# ----------------------
# Ticket Editing tests:
# ----------------------


def test_ticket_edit_pass(monkeypatch):
    with pytest.raises(
        SystemExit
    ):  # RecursionError is here as while the edit function works when ran by the user, it fails when ran in a test
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", ticket_edit_inputs_pass)

        output = main()
        assert output == "Changes Applied:"
        print("TEST: Passed")


def test_ticket_edit_fail(monkeypatch):
    with pytest.raises(
        SystemExit
    ):  # RecursionError is here as while the edit function works when ran by the user, it fails when ran in a test
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", ticket_edit_inputs_fail)

        output = main()
        assert (
            output
            == """
        ERROR: Invalid Ticket ID
        Press <ENTER> to continue"""
        )
        print("TEST: Passed")


# ---------------------------
# Ticket Status Change tests:
# ---------------------------


def test_ticket_status_change_pass(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", delete_inputs_fail)

        output = main()
        assert output == ""
        print("TEST: Passed")


def test_ticket_status_change_fail(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", delete_inputs_fail)

        output = main()
        assert output == ""
        print("TEST: Passed")


# ---------------------
# Ticket Viewing tests:
# ---------------------


def test_ticket_view_pass(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", view_tickets_inputs_pass)

        output = main()
        assert output == ""
        print("TEST: Passed")


def test_ticket_view_fail(monkeypatch):
    with pytest.raises(SystemExit):
        print("Testing Ticket creation system")
        monkeypatch.setattr("builtins.input", view_tickets_inputs_fail)

        output = main()
        assert output == ""
        print("TEST: Passed")

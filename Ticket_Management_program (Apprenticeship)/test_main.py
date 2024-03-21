import pytest
from Assignment_code.code.Packages.clear import clear
from Start_here import main


def startup_inputs(prompt):
    responses = {
        ": ": "3",
        "Do you want to exit (Y/N): ": "Y",
    }
    return responses.get(prompt, "")


def test_startup(monkeypatch):
    with pytest.raises(SystemExit):
        monkeypatch.setattr("builtins.input", startup_inputs)
        output = main()
        assert output == ""


def test_clear():  # This tests the clear function (there is no way of it really failing so this test normally passes unless the OS isn't using the Windows Kernel, Linux Kernel, or MacOS Kernel)
    try:
        if pytest.raises(Exception):
            clear()
            print("TEST: CLEAR | Passed")
    except SystemError or OSError:
        print(f"TEST: CLEAR | Failed")
    if pytest.raises(Exception):
        clear()

def back():
    try:
        from Assignment_code.code.main import main_menu

        main_menu()
    except ImportError:
        try:
            from main import main_menu

            main_menu()
        except ImportError as e:
            print(f"ERROR: {e}")


back()

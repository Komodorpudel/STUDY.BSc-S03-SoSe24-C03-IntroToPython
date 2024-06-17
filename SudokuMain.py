import sys

# -----------------------------------------------------------------
    def main():

        # Ask the user for their preferred UI type
        ui_type = input("Which UI would you like to use? (Enter 'gui' or 'terminal'): ").strip().lower()
        
        if ui_type == 'gui':
            from SudokuUI_Graphical import SudokuUI_Graphical
            ui = SudokuUI_Graphical()
        elif ui_type == 'terminal':
            from SudokuUI_Terminal import SudokuUI_Terminal
            ui = SudokuUI_Terminal()
        else:
            print("Invalid input. Exiting...")
            sys.exit(1)

        # Assuming you have a UIController class that handles the interaction
        from SudokuAppController import SudokuAppController
        controller = SudokuAppController(ui)
        controller.run()

# -----------------------------------------------------------------

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------

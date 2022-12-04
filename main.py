from controller import *


def main() -> None:
    """
    Function that starts the app and shows the GUI to the user
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()

if __name__ == '__main__':
        main()

import sys

sys.path.append("./mainWindow.py")
from mainWindow import * 

def main():

    # create the main Window
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("execution du programme")
    main()

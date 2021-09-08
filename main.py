import main_win
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.A_val = None
        self.B_val = None
        self.C_val = None

        self.button.clicked.connect(self.print_answer)

    def print_answer(self):
        self.A_val = float(self.tE_A.toPlainText())
        self.B_val = float(self.tE_B.toPlainText())
        self.C_val = float(self.tE_C.toPlainText())

        if self.A_val == 0:
            if self.B_val == 0:
                if self.C_val != 0:
                    self.tE_Answer.setText("Ошибка", encoding='utf-8')
                else:
                    self.tE_Answer.setText("Любое число", encoding='utf-8')
            else:
                answer = (-self.C_val) / self.B_val
                self.tE_Answer.setText(str(answer))
        else:
            Dis = (self.B_val)**2 - 4*self.A_val*self.C_val
            if Dis > 0:
                x11 = ((-self.B_val) + Dis**(1/2))/(2*self.A_val)
                x22 = ((-self.B_val) - Dis**(1/2))/(2*self.A_val)
                self.tE_Answer.setText(f"x1 = {x11}\rx2 = {x22}")
            elif Dis == 0:
                x = (-self.B_val)/(2*self.A_val)
                self.tE_Answer.setText(f"x = {x}")
            else:
                self.tE_Answer.setText("Действ. \nкорней нет", encoding='utf-8')



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # os.environ["QT_SCALE_FACTOR"] = "1.0"
    #
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

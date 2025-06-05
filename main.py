import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from bmi import Ui_MainWindow
from bmi_logic import BMICalculator


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['სიმაღლე (სმ)', 'წონა (კგ)', 'BMI', 'შეფასება'])
        self.ui.tableView.setModel(self.model)


        self.ui.pushButton.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            height = float(self.ui.lineEdit_height.text())
            weight = float(self.ui.lineEdit_weight.text())

            calculator = BMICalculator(height, weight)
            bmi = calculator.calculate_bmi()
            status = calculator.interpret_bmi(bmi)

            self.ui.label_result.setText(f"BMI: {bmi} ({status})")


            self.add_history(height, weight, bmi, status)

        except ValueError:
            self.ui.label_result.setText("შეიყვანე მხოლოდ რიცხვები ")

    def add_history(self, height, weight, bmi, status):
        row = [
            QStandardItem(str(height)),
            QStandardItem(str(weight)),
            QStandardItem(str(bmi)),
            QStandardItem(status)
        ]
        self.model.appendRow(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.setWindowTitle("BMI კალკულატორი")
    window.show()
    sys.exit(app.exec_())

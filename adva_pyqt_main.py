from Ui_adva_pyqt import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui


class CamShow(QMainWindow, Ui_MainWindow):
    """
    继承 QMainWindow, Ui_MainWindow 类, python是多继承
    """

    def __init__(self, parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        # 信号与槽
        self.OpenFileBtn.clicked.connect(self.loadImage)
        self.actionOpen.triggered.connect(self.loadImage)
        self.actionExit.triggered.connect(self.exit)

    def exit(self):
        sys.exit(app.exec_())

    def loadImage(self):
        print("按钮被按下了")
        # 读取文件
        self.fname, _ = QFileDialog.getOpenFileName(
            self, "选择图片", ".", "图像文件(*.jpg *.png)"
        )
        print(self.fname)

        # 显示到label
        pix = QtGui.QPixmap(self.fname).scaled(
            self.ImageLabel.width(), self.ImageLabel.height()
        )
        self.ImageLabel.setPixmap(pix)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())

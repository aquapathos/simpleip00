# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys,os
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import cv2
import numpy as np

# OpenCV2 の画像から　Qt4 のpixmapを生成する関数
def cv2q4pixmap(cv2img):
    height, width, dim = cv2img.shape
    bytesPerLine = dim * width
    rgbimg = cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
    q4img = QtGui.QImage(rgbimg.data,width,height,bytesPerLine,QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(q4img)
    return pixmap
# ウィンドウの上部エリア
class Pane01(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.initial()

    def initial(self):
        # 512x512の真っ黒のダミー画像を作る
        dummypixmap = cv2q4pixmap(np.zeros((512,512,3),dtype=np.uint8))
        # Label Widget に画像を貼り付ける．Labelを表示すれば画像が表示される
        self.imagePane = QtGui.QLabel(u"パネル",parent=self)
        self.imagePane.setPixmap(dummypixmap)

        # 自動水平レイアウトで 上記Widetを配置したレイアウトをつくる
        self.layout = QtGui.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.imagePane)

# ウィンドウの下部エリア
class Pane02(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.initial()

    def initial(self):
        # ボタンWidgetを一つ作る
        self.fopenButton = QtGui.QPushButton(u"ボタン",parent=self)

        # 自動水平レイアウトで 上記Widetを配置したレイアウトをつくる
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.fopenButton)

def main():
    # 次の3行はおきまり
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    mainPanels = QtGui.QWidget()

    # 自動垂直レイアウトに Pane01,Pane02 のインスタンスを貼り付ける
    layout = QtGui.QVBoxLayout()
    pane01 = Pane01(parent=mainPanels)
    layout.addWidget(pane01)
    pane02 = Pane02(parent=mainPanels)
    layout.addWidget(pane02)

    # メインパネルにレイアウトしたものを貼り付ける
    mainPanels.setLayout(layout)
    # メインパネルをウィンドウ中央エリアに取り付け
    mainWindow.setCentralWidget(mainPanels)

    #　最後に表示してプログラムを実行　この2行はおきまり
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()

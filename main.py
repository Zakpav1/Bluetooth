from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice\

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Bluetoouth")

serial = QSerialPort()
serial.setBaudRate(9600)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comL.addItems(portList)


def open():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)
    ui.textEdit.setText("Можно проверять\n")


def close():
    serial.setPortName(ui.comL.currentText())
    serial.close(QIODevice.ReadWrite)


def read():
    try:
        rx = serial.readLine()
        rxs = str(rx, 'UTF-8').strip()
        data = rxs.split(',')
        ui.textEdit.setText(rxs)
    except Exception:
        ui.textEdit.setText('не работает твоя херня\n')



ui.OpenB.clicked.connect(open)
ui.CheckB.clicked.connect(read)

ui.show()
app.exec()
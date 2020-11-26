from PySide2.QtWidgets import *

app=QApplication()
wd = QWidget()
ws = QTableView()
m = QMainWindow()

l = [1,2,3,4,5,6,7,8,9]
print(tuple(zip(*[iter(l)] * 3))) #((1, 2, 3), (4, 5, 6), (7, 8, 9))

# import sys
# import requests
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtGui import QImage, QPixmap


# url_image = 'https://pics.javhoo.net/2016/02/2ny_a.jpg'#'https://live.staticflickr.com/65535/49251422908_591245c64a_c_d.jpg'

# app = QApplication([])

# image = QImage()
# image.loadFromData(requests.get(url_image).content)

# pixmap5 = image.scaled(250, 250)

# image_label = QLabel()
# image_label.setPixmap(QPixmap(pixmap5))
# image_label.show()

# app.exec_()

from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QVBoxLayout, QTableView, QTableWidgetItem, QItemDelegate
from PyQt5.QtGui import QStandardItem,  QStandardItemModel
from PyQt5.QtCore import QSortFilterProxyModel
import sys
import requests
from PyQt5.QtGui import QImage, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np




class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        return super(PandasModel, self).headerData(section, orientation, role)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if not index.isValid():
            return QtCore.QVariant()
        if index.row() == 0:
            return QtCore.QVariant(self._df.columns.values[index.column()])
        return QtCore.QVariant(str(self._df.iloc[index.row()-1, index.column()]))

    def setData(self, index, value, role):
        if index.row() == 0:
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            self._df.columns.values[index.column()] = value
            self.headerDataChanged.emit(QtCore.Qt.Horizontal, index.column(), index.column())
        else:
            col = self._df.columns[index.column()]
            row = self._df.index[index.row()]
            if isinstance(value, QtCore.QVariant):
                value = value.value()
            if hasattr(value, 'toPyObject'):
                value = value.toPyObject()
            else:
                dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
                self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)+1 

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)


class Second(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('second.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(data, bins= 30)
        self.ax.set_xlabel('Age', fontweight = 'bold')
        self.ax.set_ylabel('Frequency', fontweight = 'bold')
        self.canvas.draw()

    def display(self):
	    self.show()


class Third(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('third.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(data, bins= 30)
        self.ax.set_xlabel('Height', fontweight='bold')
        self.ax.set_ylabel('Frequency', fontweight = 'bold')
        self.canvas.draw()

    def display(self):
	    self.show()


class Fourth(QMainWindow):
    def __init__(self,x,y):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('fourth.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.bar(x = x, height=y)
        self.ax.set_xlabel('Cup_Size',fontweight="bold")
        self.ax.set_ylabel('Count',fontweight="bold")
        self.canvas.draw()

    def display(self):
        self.show()


class Fiveth(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('fiveth.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(data, bins= 30)
        self.ax.set_xlabel('Bust',fontweight="bold")
        self.ax.set_ylabel('Frequency',fontweight="bold")
        self.canvas.draw()

    def display(self):
        self.show()

class Sixth(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('sixth.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(data, bins= 30)
        self.ax.set_xlabel('Waist',fontweight="bold")
        self.ax.set_ylabel('Frequency',fontweight="bold")
        self.canvas.draw()

    def display(self):
        self.show()

class Seventh(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('seventh.ui',self)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
 
        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        
        self.ua.gridLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(data, bins= 30)
        self.ax.set_xlabel('Hips',fontweight="bold")
        self.ax.set_ylabel('Frequency',fontweight="bold")
        self.canvas.draw()

    def display(self):
        self.show()



class Filter(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.w = None
        self.ua = uic.loadUi('table.ui',self)

        self.model = QStandardItemModel(len(data.axes[1]), len(data.axes[0]))
        self.model.setHorizontalHeaderLabels(data.columns)
        self.stat_df = data.sort_index()
        self.model = PandasModel(data)
        self.tableView.setModel(self.model)
        for i in range(self.model.columnCount()):
            ix = self.model.index(-1, i)
            self.tableView.openPersistentEditor(ix)
        stylesheet = "::section{Background-color:rgb(192,192,192);}"
        self.tableView.verticalHeader().setStyleSheet(stylesheet)
        self.tableView.horizontalHeader().setStyleSheet(stylesheet)

        self.radioButton.toggled.connect(self.radio_1)
        self.radioButton_2.toggled.connect(self.radio_2)
        self.radioButton_3.toggled.connect(self.radio_3)
        self.label_3.setText(str(len(data.axes[0])))
        self.label_7.setText(str(len(data.axes[1])))


    def radio_1(self):

        if self.radioButton.isChecked():
            print('Phrase_1')
            filter_proxy_model = QSortFilterProxyModel()
            filter_proxy_model.setSourceModel(self.model)
            filter_proxy_model.setFilterKeyColumn(4)
            self.lineEdit.textChanged.connect(filter_proxy_model.setFilterRegExp)
            self.tableView.setModel(filter_proxy_model)

    def radio_2(self):
        if self.radioButton_2.isChecked():
            print('Phrase_2')
            filter_proxy_model = QSortFilterProxyModel()
            filter_proxy_model.setSourceModel(self.model)
            filter_proxy_model.setFilterKeyColumn(5)
            self.lineEdit_2.textChanged.connect(filter_proxy_model.setFilterRegExp)
            self.tableView.setModel(filter_proxy_model)


    def radio_3(self):
        if self.radioButton_3.isChecked():
            print('Phrase_3')
            filter_proxy_model = QSortFilterProxyModel()
            filter_proxy_model.setSourceModel(self.model)
            filter_proxy_model.setFilterKeyColumn(6)
            self.lineEdit_3.textChanged.connect(filter_proxy_model.setFilterRegExp)
            self.tableView.setModel(filter_proxy_model)
            

    def display(self):
        self.show()



class Jav(QtWidgets.QMainWindow):
    def __init__(self):
        super(Jav,self).__init__()
        self.ui = uic.loadUi('jav.ui',self)
        
        self.actionAge.triggered.connect(self.Age)
        self.actionHeight.triggered.connect(self.Height)
        self.actionCup_size.triggered.connect(self.Cup_Size)
        self.actionBust.triggered.connect(self.Bust)
        self.actionWaist.triggered.connect(self.Waist)
        self.actionHips.triggered.connect(self.Hips)
        self.pushButton.clicked.connect(self.ok)
        self.actionFilter.triggered.connect(self.table)
        self.df = pd.read_csv('actress.csv')
        self.df.replace(np.nan,inplace=True )

        year = []
        for i in self.df['birthday']:
            year.append(int(i[:4]))
        self.df['year'] = year
        self.df['age'] = 2021 - self.df['year']


        new_bust = []
        for j in self.df['bust']:
            new_bust.append(int(j[:-2]))
        self.df['new_bust'] = new_bust

        new_waist = []
        for a in self.df['waist']:
            new_waist.append(int(a[:-2]))
        self.df['new_waist'] = new_waist

        new_hips = []
        for b in self.df['hips']:
            new_hips.append(int(b[:-2]))
        self.df['new_hips'] = new_hips

        new_height = []
        for c in self.df['height']:
            new_height.append(int(c[:3]))
        self.df['new_height'] = new_height


        self.figure = plt.figure(figsize=(1,2), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        self.figure_1 = plt.figure(figsize=(1,2), dpi=100)
        self.canvas_1 = FigureCanvas(self.figure_1)

        self.figure_2 = plt.figure(figsize=(1,2), dpi=100)
        self.canvas_2 = FigureCanvas(self.figure_2)

        sns.set_style('darkgrid')
        style = 'ggplot' 

        plt.style.use(style)
        
        
        self.ui.verticalLayout_2.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.hist(self.df['age'], bins= 30)
        
        self.ui.verticalLayout_3.addWidget(self.canvas_1)
        self.ax = self.figure_1.add_subplot(111)
        self.ax.hist(self.df['new_height'], bins= 30)

        a1 = self.df[self.df['cup_size'] == 'A'].count()[0]
        a2 = self.df[self.df['cup_size'] == 'B'].count()[0]
        a3 = self.df[self.df['cup_size'] == 'C'].count()[0]
        a4 = self.df[self.df['cup_size'] == 'D'].count()[0]
        a5 = self.df[self.df['cup_size'] == 'E'].count()[0]
        a6 = self.df[self.df['cup_size'] == 'F'].count()[0]
        a7 = self.df[self.df['cup_size'] == 'G'].count()[0]
        a8 = self.df[self.df['cup_size'] == 'H'].count()[0]
        a9 = self.df[self.df['cup_size'] == 'I'].count()[0]
        a10 = self.df[self.df['cup_size'] == 'J'].count()[0]
        a11 = self.df[self.df['cup_size'] == 'K'].count()[0]
        a12 = self.df[self.df['cup_size'] == 'L'].count()[0]
        a13 = self.df[self.df['cup_size'] == 'M'].count()[0]
        a14 = self.df[self.df['cup_size'] == 'N'].count()[0]
        a15 = self.df[self.df['cup_size'] == 'O'].count()[0]
        a16 = self.df[self.df['cup_size'] == 'P'].count()[0]
        a17 = self.df[self.df['cup_size'] == 'Q'].count()[0]
       
        
        self.ui.verticalLayout_4.addWidget(self.canvas_2)
        self.ax = self.figure_2.add_subplot(111)
        self.ax.bar(x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'], height=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,
                                                                                         a13,a14,a15,a16,a17])

        data = self.df['age']
        self.second = Second(data)
        self.third = Third(self.df['new_height'])
        self.fourth = Fourth(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'], [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,
                                                                                         a13,a14,a15,a16,a17])
        self.fiveth = Fiveth(self.df['new_bust'])
        self.sixth = Sixth(self.df['new_waist'])
        self.seventh = Seventh(self.df['new_hips'])

        bust = ['max', 'min', '70-80', '80-90', '90-100','>100']
        waist = ['max', 'min', '50-60', '60-70', '70-80', '80-90', '>90']
        hips = ['max', 'min', '70-80', '80-90','90-100','100-110','110-120', '>120']
        
        self.comboBox.addItems(bust)
        self.comboBox_2.addItems(waist)
        self.comboBox_3.addItems(hips)

        self.comboBox.activated[str].connect(self.bus)
        self.comboBox_2.activated[str].connect(self.waist)
        self.comboBox_3.activated[str].connect(self.hip)

        self.output = self.df[['name','birthday','height', 'cup_size', 'new_bust','new_waist', 'new_hips', 'age', 'imgurl']]


    def hip(self,text):
        if text == 'max':
            max_hips = self.output['new_hips'].max()
            self.a = self.output[self.output['new_hips'] ==max_hips]
        if text == 'min':
            min_hips = self.output['new_hips'].min()
            self.a = self.output[self.output['new_hips'] ==min_hips]
        elif text == '70-80':
            self.a = self.output[(self.output['new_hips']>70) & (self.output['new_hips']<80)]
        elif text == '80-90':
            self.a = self.output[(self.output['new_hips']>80) & (self.output['new_hips']<90)]
        elif text == '90-100':
            self.a = self.output[(self.output['new_hips']>90) & (self.output['new_hips']<100)]
        elif text == '100-110':
            self.a = self.output[(self.output['new_hips']>100) & (self.output['new_hips']<110)]
        elif text == '110-120':
            self.a = self.output[(self.output['new_hips']>110) & (self.output['new_hips']<120)]
        elif text == '>120':
            self.a = self.output[(self.output['new_hips']>120)]


        self.model_2 = QStandardItemModel(len(self.a.axes[1]), len(self.a.axes[0]))
        self.model_2.setHorizontalHeaderLabels(self.a.columns)
        self.stat_df = self.a.sort_index()
        self.model_2 = PandasModel(self.a)
        self.tableView.setModel(self.model_2)
        for i in range(self.model_2.columnCount()):
            ix = self.model_2.index(-1, i)
            self.tableView.openPersistentEditor(ix)




    def waist(self,text):
        if text == 'max':
            max_waist = self.output['new_waist'].max()
            self.a = self.output[self.output['new_waist'] ==max_waist]
        elif text == 'min':
            min_waist = self.output['new_waist'].min()
            self.a = self.output[self.output['new_waist'] ==min_waist]
        elif text == '50-60':
            self.a = self.output[(self.output['new_waist']>50) & (self.output['new_waist']<60)]
        elif text == '60-70':
            self.a = self.output[(self.output['new_waist']>60) & (self.output['new_waist']<70)]
        elif text == '70-80':
            self.a = self.output[(self.output['new_waist']>70) & (self.output['new_waist']<80)]
        elif text == '80-90':
            self.a = self.output[(self.output['new_waist']>80) & (self.output['new_waist']<90)]
        elif text == '>90':
            self.a = self.output[(self.output['new_waist']>90)]



        self.model_2 = QStandardItemModel(len(self.a.axes[1]), len(self.a.axes[0]))
        self.model_2.setHorizontalHeaderLabels(self.a.columns)
        self.stat_df = self.a.sort_index()
        self.model_2 = PandasModel(self.a)
        self.tableView.setModel(self.model_2)
        for i in range(self.model_2.columnCount()):
            ix = self.model_2.index(-1, i)
            self.tableView.openPersistentEditor(ix)

    def bus(self,text):
        if text == 'max':
            max_bust = self.output['new_bust'].max()
            self.a = self.output[self.output['new_bust'] == max_bust]
        elif text == 'min':
            min_bust = self.output['new_bust'].min()
            self.a = self.output[self.output['new_bust'] == min_bust]
        elif text == '70-80':
            self.a = self.output[(self.output['new_bust']>70) & (self.output['new_bust']<80)]
        elif text == '80-90':
            self.a = self.output[(self.output['new_bust']>80) & (self.output['new_bust']<90)]
        elif text == '90-100':
            self.a == self.output[(self.output['new_bust']>90) & (self.output['new_bust']<100)]
        elif text == '>100':
            self.a == self.output[(self.output['new_bust']>100)]

            


        self.model_2 = QStandardItemModel(len(self.a.axes[1]), len(self.a.axes[0]))
        self.model_2.setHorizontalHeaderLabels(self.a.columns)
        self.stat_df = self.a.sort_index()
        self.model_2 = PandasModel(self.a)
        self.tableView.setModel(self.model_2)
        for i in range(self.model_2.columnCount()):
            ix = self.model_2.index(-1, i)
            self.tableView.openPersistentEditor(ix)
    
    def ok(self):
        a = self.lineEdit.text()
        self.img = self.output[self.output['name']==a]['imgurl']
        self.img = ''.join(self.img)
        print(self.img)

        self.image = QImage()
        self.image.loadFromData(requests.get(self.img).content)

        pixmap5 = self.image.scaled(200, 200)

        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap(pixmap5)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)

        
        age = self.output[self.output['name'] == a]['age']
        cup_size = self.output[self.output['name'] ==a]['cup_size']
        bust = self.output[self.output['name']==a]['new_bust']
        waist = self.output[self.output['name']==a]['new_waist']
        hips = self.output[self.output['name']==a]['new_hips']
        height = self.output[self.output['name']==a]['height']

        print(age)
        self.label_15.setText(a)
        self.label_16.setText(str(age.to_list()[0]))
        self.label_17.setText(str(cup_size.to_list()[0]))
        self.label_18.setText(str(bust.to_list()[0]))
        self.label_19.setText(str(waist.to_list()[0]))
        self.label_20.setText(str(hips.to_list()[0]))
        self.label_21.setText(str(height.to_list()[0]))

        self.filter = Filter(self.a)

    
    def Age(self):
        self.second.display()

    def Height(self):
    	self.third.display()

    def Cup_Size(self):
        self.fourth.display()

    def Bust(self):
        self.fiveth.display()

    def Waist(self):
        self.sixth.display()

    def Hips(self):
        self.seventh.display()

    def table(self):
        self.filter.display()
        

app = QApplication(sys.argv)
window = Jav()
window.show()
app.exec()
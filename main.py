from starwarsDialog import Ui_Dialog
from starwarscharacterinfo import Ui_MainWindow

import json
import requests
import sys

from PyQt5.QtWidgets import QApplication, QDialog, qApp, QLabel, QGridLayout, QLayout, QPushButton, QMainWindow
from PyQt5.QtCore import Qt


class StarWarApp(QDialog, Ui_Dialog):
    def __init__(self):
        super(StarWarApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("StarWars Characters")
        self.url = {"current":"https://swapi.dev/api/people/",
                    "next":"",
                    "previous":""
                    }
        
        self.pushButton.clicked.connect(self.previous_page)
        self.pushButton_2.clicked.connect(self.next_page)
        self.gridLayoutLP = QGridLayout(self.widget)
        self.gridLayoutLP.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayoutLP.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutLP.setObjectName("gridLayoutLP")
        
        self.name_button = []
        self.first_page()
        # self.show()

    def create_labels(self, data):
        for i in range(len(data)):
            self.label_name = QLabel(data[i]["name"])
            self.label_name.setAlignment(Qt.AlignCenter)
            self.label_name.setMargin(14)
            self.gridLayoutLP.addWidget(self.label_name,i,1)

    def create_buttons(self, data):
        qApp.processEvents()
        self.name_button.clear()
        for i in range(len(data)):  
            name = data[i]["name"]
            self.name_button.append(name)
            self.btn = QPushButton(f"Get {name} Info", self)            
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : self.charater_info_window(text))
            self.gridLayoutLP.addWidget(self.btn,i,2)

    def first_page(self):
        self.data = requests.get(self.url["current"])

        self.create_labels(self.data.json()['results'])
        self.create_buttons(self.data.json()['results'])
        self.label.setText(str(len(self.data.json()["results"])))
        self.url["next"] = self.data.json()["next"]
        self.url["previous"] = self.data.json()["previous"]


    def next_page(self):
        for i in reversed(range(self.gridLayoutLP.count())): 
            self.gridLayoutLP.itemAt(i).widget().deleteLater()

        if self.url["next"] != None:
            qApp.processEvents()
            self.data = requests.get(self.url["next"])
            
            self.create_labels(self.data.json()['results'])
            self.create_buttons(self.data.json()['results'])
            self.label.setText(str(len(self.data.json()["results"])))
            self.url["current"] = self.data.url
            self.url["next"] = self.data.json()["next"]
            self.url["previous"] = self.data.json()["previous"]
        else:
            self.data = requests.get(self.url["current"])
            self.create_labels(self.data.json()['results'])
            self.create_buttons(self.data.json()['results'])
            self.label.setText(str(len(self.data.json()["results"])))

    def previous_page(self):
        qApp.processEvents()
        for i in reversed(range(self.gridLayoutLP.count())): 
            self.gridLayoutLP.itemAt(i).widget().deleteLater()

        if self.url["previous"] == None:
            self.data = requests.get(self.url["current"])
            self.create_labels(self.data.json()['results'])
            self.create_buttons(self.data.json()['results'])
            self.label.setText(str(len(self.data.json()["results"])))
        else:
            self.data = requests.get(self.url["previous"])
    
            self.create_labels(self.data.json()['results'])
            self.create_buttons(self.data.json()['results'])
            self.label.setText(str(len(self.data.json()["results"])))
            self.url["current"] = self.data.url
            self.url["next"] = self.data.json()["next"]
            self.url["previous"] = self.data.json()["previous"]

    def charater_info_window(self, b):
        name_index = self.name_button.index(b[4:-5])
       
        self.charaterwindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.charaterwindow)
        self.charaterwindow.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui.name_label_header(b[4:-5])
        self.ui.label_height.setText(self.data.json()['results'][name_index]['height'])
        self.ui.label_mass.setText(self.data.json()['results'][name_index]['mass'])
        self.ui.label_haircolor.setText(self.data.json()['results'][name_index]['hair_color'])
        self.ui.label_skincolor.setText(self.data.json()['results'][name_index]['skin_color'])
        self.ui.label_eyecolor.setText(self.data.json()['results'][name_index]['eye_color'])
        self.ui.label_birthyear.setText(self.data.json()['results'][name_index]['birth_year'])
        self.ui.label_gender.setText(self.data.json()['results'][name_index]['gender'])
        homeworld_url = self.data.json()['results'][name_index]['homeworld']
        home_world = requests.get(homeworld_url)
        
        self.ui.label_name.setText(home_world.json()['name'])
        self.ui.label_rotationperiod.setText(home_world.json()['rotation_period'])
        self.ui.label_orbitalperiod.setText(home_world.json()['orbital_period'])
        self.ui.label_diameter.setText(home_world.json()['diameter'])
        self.ui.label_climate.setText(home_world.json()['climate'])
        self.ui.label_gravity.setText(home_world.json()['gravity'])
        self.ui.label_terrain.setText(home_world.json()['terrain'])
        self.ui.label_surfacewater.setText(home_world.json()['surface_water'])
        self.ui.label_population.setText(home_world.json()['population'])
        self.charaterwindow.show()
        
        

app = QApplication(sys.argv)
window = StarWarApp()
window.repaint()
window.show()
app.exec()
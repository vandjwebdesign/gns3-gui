# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_preferences_page.ui'
#
# Created: Thu May 28 11:58:27 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_ServerPreferencesPageWidget(object):

    def setupUi(self, ServerPreferencesPageWidget):
        ServerPreferencesPageWidget.setObjectName("ServerPreferencesPageWidget")
        ServerPreferencesPageWidget.resize(549, 536)
        self.verticalLayout = QtWidgets.QVBoxLayout(ServerPreferencesPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(ServerPreferencesPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiLocalTabWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalServerAutoStartCheckBox.sizePolicy().hasHeightForWidth())
        self.uiLocalServerAutoStartCheckBox.setSizePolicy(sizePolicy)
        self.uiLocalServerAutoStartCheckBox.setMinimumSize(QtCore.QSize(0, 40))
        self.uiLocalServerAutoStartCheckBox.setChecked(True)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.verticalLayout_2.addWidget(self.uiLocalServerAutoStartCheckBox)
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGeneralSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiGeneralSettingsGroupBox.setSizePolicy(sizePolicy)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout.addWidget(self.uiLocalServerPathLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.uiUbridgePathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLabel.setObjectName("uiUbridgePathLabel")
        self.gridLayout.addWidget(self.uiUbridgePathLabel, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiUbridgePathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLineEdit.setObjectName("uiUbridgePathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiUbridgePathLineEdit)
        self.uiUbridgeToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiUbridgeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiUbridgeToolButton.setObjectName("uiUbridgeToolButton")
        self.horizontalLayout_5.addWidget(self.uiUbridgeToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout.addWidget(self.uiLocalServerHostLabel, 4, 0, 1, 1)
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout.addWidget(self.uiLocalServerHostComboBox, 5, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout.addWidget(self.uiLocalServerPortLabel, 6, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 8000)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout.addWidget(self.uiLocalServerPortSpinBox, 7, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 8, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.uiGeneralSettingsGroupBox)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.uiConsolePortRangeGroupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.horizontalLayout_7.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.horizontalLayout_7.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem = QtWidgets.QSpacerItem(363, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiUDPPortRangeGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_8.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_8.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(363, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.uiUDPPortRangeGroupBox)
        spacerItem2 = QtWidgets.QSpacerItem(390, 193, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.uiTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiRemoteTabWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        self.uiRemoteServersTreeWidget.setColumnCount(4)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(0, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Port")
        self.verticalLayout_3.addWidget(self.uiRemoteServersTreeWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.uiRemoteServerProtocolLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerProtocolLabel.setObjectName("uiRemoteServerProtocolLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerProtocolLabel)
        self.uiRemoteServerProtocolComboBox = QtWidgets.QComboBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerProtocolComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerProtocolComboBox.setObjectName("uiRemoteServerProtocolComboBox")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.uiRemoteServerProtocolComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerProtocolComboBox)
        self.uiRemoteServerHostLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerHostLabel.setObjectName("uiRemoteServerHostLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerHostLabel)
        self.uiRemoteServerPortLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLineEdit.setObjectName("uiRemoteServerPortLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerPortLineEdit)
        self.uiRemoteServerPortLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerPortLabel.setObjectName("uiRemoteServerPortLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerPortLabel)
        self.uiRemoteServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerPortSpinBox.setSuffix(" TCP")
        self.uiRemoteServerPortSpinBox.setMaximum(65535)
        self.uiRemoteServerPortSpinBox.setProperty("value", 8000)
        self.uiRemoteServerPortSpinBox.setObjectName("uiRemoteServerPortSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerPortSpinBox)
        self.uiRemoteServerSSHPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerSSHPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerSSHPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteServerSSHPortSpinBox.setMaximum(65535)
        self.uiRemoteServerSSHPortSpinBox.setProperty("value", 22)
        self.uiRemoteServerSSHPortSpinBox.setObjectName("uiRemoteServerSSHPortSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerSSHPortSpinBox)
        self.uiRemoteServerSSHPortLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerSSHPortLabel.setObjectName("uiRemoteServerSSHPortLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerSSHPortLabel)
        self.uiRemoteServerUserLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerUserLabel.setObjectName("uiRemoteServerUserLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerUserLabel)
        self.uiRemoteServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServerUserLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteServerUserLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteServerUserLineEdit.setObjectName("uiRemoteServerUserLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerUserLineEdit)
        self.uiRemoteServerSSHKeyLabel = QtWidgets.QLabel(self.uiRemoteTabWidget)
        self.uiRemoteServerSSHKeyLabel.setObjectName("uiRemoteServerSSHKeyLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.uiRemoteServerSSHKeyLabel)
        self.uiRemoteServerSSHKeyHorizontalLayout = QtWidgets.QHBoxLayout()
        self.uiRemoteServerSSHKeyHorizontalLayout.setObjectName("uiRemoteServerSSHKeyHorizontalLayout")
        self.uiRemoteServerSSHKeyLineEdit = QtWidgets.QLineEdit(self.uiRemoteTabWidget)
        self.uiRemoteServerSSHKeyLineEdit.setObjectName("uiRemoteServerSSHKeyLineEdit")
        self.uiRemoteServerSSHKeyHorizontalLayout.addWidget(self.uiRemoteServerSSHKeyLineEdit)
        self.uiRemoteServerSSHKeyPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiRemoteServerSSHKeyPushButton.setObjectName("uiRemoteServerSSHKeyPushButton")
        self.uiRemoteServerSSHKeyHorizontalLayout.addWidget(self.uiRemoteServerSSHKeyPushButton)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.uiRemoteServerSSHKeyHorizontalLayout)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(390, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.uiTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.verticalLayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ServerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ServerPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ServerPreferencesPageWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiTabWidget, self.uiLocalServerAutoStartCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerToolButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiLocalServerHostComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiLocalServerPathLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiRemoteServersTreeWidget)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiRemoteServerProtocolComboBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerProtocolComboBox, self.uiRemoteServerPortLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortLineEdit, self.uiRemoteServerPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerPortSpinBox, self.uiRemoteServerUserLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerUserLineEdit, self.uiRemoteServerSSHPortSpinBox)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerSSHPortSpinBox, self.uiRemoteServerSSHKeyLineEdit)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerSSHKeyLineEdit, self.uiRemoteServerSSHKeyPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiRemoteServerSSHKeyPushButton, self.uiDeleteRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiDeleteRemoteServerPushButton, self.uiAddRemoteServerPushButton)
        ServerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiRestoreDefaultsPushButton)

    def retranslateUi(self, ServerPreferencesPageWidget):
        _translate = gns3.qt.translate
        ServerPreferencesPageWidget.setWindowTitle(_translate("ServerPreferencesPageWidget", "Server"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ServerPreferencesPageWidget", "Enable local server"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "General settings"))
        self.uiLocalServerPathLabel.setText(_translate("ServerPreferencesPageWidget", "Server path:"))
        self.uiLocalServerToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiUbridgePathLabel.setText(_translate("ServerPreferencesPageWidget", "Ubridge path:"))
        self.uiUbridgeToolButton.setText(_translate("ServerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ServerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "Console port range"))
        self.uiConsolePortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ServerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ServerPreferencesPageWidget", "to"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiLocalTabWidget), _translate("ServerPreferencesPageWidget", "Local server"))
        self.uiRemoteServersTreeWidget.headerItem().setText(3, _translate("ServerPreferencesPageWidget", "User"))
        self.uiRemoteServerProtocolLabel.setText(_translate("ServerPreferencesPageWidget", "Protocol:"))
        self.uiRemoteServerProtocolComboBox.setProperty("currentText", _translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(0, _translate("ServerPreferencesPageWidget", "HTTP"))
        self.uiRemoteServerProtocolComboBox.setItemText(1, _translate("ServerPreferencesPageWidget", "SSH"))
        self.uiRemoteServerHostLabel.setText(_translate("ServerPreferencesPageWidget", "Host:"))
        self.uiRemoteServerPortLineEdit.setText(_translate("ServerPreferencesPageWidget", "192.168.56.101"))
        self.uiRemoteServerPortLabel.setText(_translate("ServerPreferencesPageWidget", "Port:"))
        self.uiRemoteServerSSHPortSpinBox.setSuffix(_translate("ServerPreferencesPageWidget", " TCP"))
        self.uiRemoteServerSSHPortLabel.setText(_translate("ServerPreferencesPageWidget", "SSH port:"))
        self.uiRemoteServerUserLabel.setText(_translate("ServerPreferencesPageWidget", "User:"))
        self.uiRemoteServerSSHKeyLabel.setText(_translate("ServerPreferencesPageWidget", "SSH key:"))
        self.uiRemoteServerSSHKeyPushButton.setText(_translate("ServerPreferencesPageWidget", "Browse"))
        self.uiAddRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Add"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ServerPreferencesPageWidget", "&Delete"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ServerPreferencesPageWidget", "Remote servers"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ServerPreferencesPageWidget", "Restore defaults"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/general_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneralPreferencesPageWidget(object):
    def setupUi(self, GeneralPreferencesPageWidget):
        GeneralPreferencesPageWidget.setObjectName("GeneralPreferencesPageWidget")
        GeneralPreferencesPageWidget.resize(517, 577)
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneralPreferencesPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiMiscTabWidget = QtWidgets.QTabWidget(GeneralPreferencesPageWidget)
        self.uiMiscTabWidget.setObjectName("uiMiscTabWidget")
        self.uiGeneralTab = QtWidgets.QWidget()
        self.uiGeneralTab.setObjectName("uiGeneralTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uiGeneralTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiLocalPathsGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiLocalPathsGroupBox.setObjectName("uiLocalPathsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiLocalPathsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiProjectsPathLabel = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.uiProjectsPathLabel.setObjectName("uiProjectsPathLabel")
        self.gridLayout_2.addWidget(self.uiProjectsPathLabel, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiProjectsPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiProjectsPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiProjectsPathLineEdit.setSizePolicy(sizePolicy)
        self.uiProjectsPathLineEdit.setObjectName("uiProjectsPathLineEdit")
        self.horizontalLayout_2.addWidget(self.uiProjectsPathLineEdit)
        self.uiProjectsPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiProjectsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiProjectsPathToolButton.setObjectName("uiProjectsPathToolButton")
        self.horizontalLayout_2.addWidget(self.uiProjectsPathToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.uiImagesPathLabel = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.uiImagesPathLabel.setObjectName("uiImagesPathLabel")
        self.gridLayout_2.addWidget(self.uiImagesPathLabel, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiImagesPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiImagesPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiImagesPathLineEdit.setSizePolicy(sizePolicy)
        self.uiImagesPathLineEdit.setObjectName("uiImagesPathLineEdit")
        self.horizontalLayout_4.addWidget(self.uiImagesPathLineEdit)
        self.uiImagesPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiImagesPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiImagesPathToolButton.setObjectName("uiImagesPathToolButton")
        self.horizontalLayout_4.addWidget(self.uiImagesPathToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.uiConfigsPathLabel = QtWidgets.QLabel(self.uiLocalPathsGroupBox)
        self.uiConfigsPathLabel.setObjectName("uiConfigsPathLabel")
        self.gridLayout_2.addWidget(self.uiConfigsPathLabel, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiConfigsPathLineEdit = QtWidgets.QLineEdit(self.uiLocalPathsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiConfigsPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiConfigsPathLineEdit.setSizePolicy(sizePolicy)
        self.uiConfigsPathLineEdit.setObjectName("uiConfigsPathLineEdit")
        self.horizontalLayout_7.addWidget(self.uiConfigsPathLineEdit)
        self.uiConfigsPathToolButton = QtWidgets.QToolButton(self.uiLocalPathsGroupBox)
        self.uiConfigsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiConfigsPathToolButton.setObjectName("uiConfigsPathToolButton")
        self.horizontalLayout_7.addWidget(self.uiConfigsPathToolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.uiLocalPathsGroupBox)
        self.uiStyleGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiStyleGroupBox.setObjectName("uiStyleGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiStyleGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiStyleComboBox = QtWidgets.QComboBox(self.uiStyleGroupBox)
        self.uiStyleComboBox.setObjectName("uiStyleComboBox")
        self.verticalLayout_4.addWidget(self.uiStyleComboBox)
        self.verticalLayout_5.addWidget(self.uiStyleGroupBox)
        self.uiConfigurationFileGroupBox = QtWidgets.QGroupBox(self.uiGeneralTab)
        self.uiConfigurationFileGroupBox.setObjectName("uiConfigurationFileGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiConfigurationFileGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiImportConfigurationFilePushButton = QtWidgets.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiImportConfigurationFilePushButton.setObjectName("uiImportConfigurationFilePushButton")
        self.horizontalLayout.addWidget(self.uiImportConfigurationFilePushButton)
        self.uiExportConfigurationFilePushButton = QtWidgets.QPushButton(self.uiConfigurationFileGroupBox)
        self.uiExportConfigurationFilePushButton.setObjectName("uiExportConfigurationFilePushButton")
        self.horizontalLayout.addWidget(self.uiExportConfigurationFilePushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.uiConfigurationFileLabel = QtWidgets.QLabel(self.uiConfigurationFileGroupBox)
        self.uiConfigurationFileLabel.setObjectName("uiConfigurationFileLabel")
        self.gridLayout.addWidget(self.uiConfigurationFileLabel, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.uiConfigurationFileGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.uiMiscTabWidget.addTab(self.uiGeneralTab, "")
        self.uiConsoleTab = QtWidgets.QWidget()
        self.uiConsoleTab.setObjectName("uiConsoleTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiConsoleTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiTelnetConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiConsoleTab)
        self.uiTelnetConsoleSettingsGroupBox.setObjectName("uiTelnetConsoleSettingsGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiTelnetConsoleSettingsGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiTelnetConsolePreconfiguredCommandLabel = QtWidgets.QLabel(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsolePreconfiguredCommandLabel.setObjectName("uiTelnetConsolePreconfiguredCommandLabel")
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandLabel, 0, 0, 1, 1)
        self.uiTelnetConsolePreconfiguredCommandComboBox = QtWidgets.QComboBox(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsolePreconfiguredCommandComboBox.setObjectName("uiTelnetConsolePreconfiguredCommandComboBox")
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandComboBox, 1, 0, 1, 1)
        self.uiTelnetConsoleCommandLabel = QtWidgets.QLabel(self.uiTelnetConsoleSettingsGroupBox)
        self.uiTelnetConsoleCommandLabel.setObjectName("uiTelnetConsoleCommandLabel")
        self.gridLayout_4.addWidget(self.uiTelnetConsoleCommandLabel, 3, 0, 1, 1)
        self.uiTelnetConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiTelnetConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTelnetConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiTelnetConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiTelnetConsoleCommandLineEdit.setObjectName("uiTelnetConsoleCommandLineEdit")
        self.gridLayout_4.addWidget(self.uiTelnetConsoleCommandLineEdit, 4, 0, 1, 2)
        self.uiTelnetConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiTelnetConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTelnetConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiTelnetConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiTelnetConsolePreconfiguredCommandPushButton.setObjectName("uiTelnetConsolePreconfiguredCommandPushButton")
        self.gridLayout_4.addWidget(self.uiTelnetConsolePreconfiguredCommandPushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiTelnetConsoleSettingsGroupBox)
        self.uiSerialConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiConsoleTab)
        self.uiSerialConsoleSettingsGroupBox.setObjectName("uiSerialConsoleSettingsGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiSerialConsoleSettingsGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiSerialConsoleCommandLabel = QtWidgets.QLabel(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsoleCommandLabel.setObjectName("uiSerialConsoleCommandLabel")
        self.gridLayout_5.addWidget(self.uiSerialConsoleCommandLabel, 3, 0, 1, 1)
        self.uiSerialConsolePreconfiguredCommandLabel = QtWidgets.QLabel(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsolePreconfiguredCommandLabel.setObjectName("uiSerialConsolePreconfiguredCommandLabel")
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandLabel, 0, 0, 1, 1)
        self.uiSerialConsolePreconfiguredCommandComboBox = QtWidgets.QComboBox(self.uiSerialConsoleSettingsGroupBox)
        self.uiSerialConsolePreconfiguredCommandComboBox.setObjectName("uiSerialConsolePreconfiguredCommandComboBox")
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandComboBox, 1, 0, 1, 1)
        self.uiSerialConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiSerialConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSerialConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiSerialConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiSerialConsoleCommandLineEdit.setObjectName("uiSerialConsoleCommandLineEdit")
        self.gridLayout_5.addWidget(self.uiSerialConsoleCommandLineEdit, 4, 0, 1, 2)
        self.uiSerialConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiSerialConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSerialConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiSerialConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiSerialConsolePreconfiguredCommandPushButton.setObjectName("uiSerialConsolePreconfiguredCommandPushButton")
        self.gridLayout_5.addWidget(self.uiSerialConsolePreconfiguredCommandPushButton, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.uiSerialConsoleSettingsGroupBox)
        self.uiConsoleMiscGroupBox = QtWidgets.QGroupBox(self.uiConsoleTab)
        self.uiConsoleMiscGroupBox.setObjectName("uiConsoleMiscGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiConsoleMiscGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiCloseConsoleWindowsOnDeleteCheckBox = QtWidgets.QCheckBox(self.uiConsoleMiscGroupBox)
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setObjectName("uiCloseConsoleWindowsOnDeleteCheckBox")
        self.gridLayout_7.addWidget(self.uiCloseConsoleWindowsOnDeleteCheckBox, 0, 0, 1, 1)
        self.uiBringConsoleWindowToFrontCheckBox = QtWidgets.QCheckBox(self.uiConsoleMiscGroupBox)
        self.uiBringConsoleWindowToFrontCheckBox.setObjectName("uiBringConsoleWindowToFrontCheckBox")
        self.gridLayout_7.addWidget(self.uiBringConsoleWindowToFrontCheckBox, 1, 0, 1, 1)
        self.uiSlowConsoleAllLabel = QtWidgets.QLabel(self.uiConsoleMiscGroupBox)
        self.uiSlowConsoleAllLabel.setObjectName("uiSlowConsoleAllLabel")
        self.gridLayout_7.addWidget(self.uiSlowConsoleAllLabel, 2, 0, 1, 1)
        self.uiDelayConsoleAllSpinBox = QtWidgets.QSpinBox(self.uiConsoleMiscGroupBox)
        self.uiDelayConsoleAllSpinBox.setMaximum(10000)
        self.uiDelayConsoleAllSpinBox.setProperty("value", 500)
        self.uiDelayConsoleAllSpinBox.setObjectName("uiDelayConsoleAllSpinBox")
        self.gridLayout_7.addWidget(self.uiDelayConsoleAllSpinBox, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.uiConsoleMiscGroupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.uiMiscTabWidget.addTab(self.uiConsoleTab, "")
        self.uiVNCTab = QtWidgets.QWidget()
        self.uiVNCTab.setObjectName("uiVNCTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.uiVNCTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uiVNCConsoleSettingsGroupBox = QtWidgets.QGroupBox(self.uiVNCTab)
        self.uiVNCConsoleSettingsGroupBox.setObjectName("uiVNCConsoleSettingsGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.uiVNCConsoleSettingsGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.uiVNCConsolePreconfiguredCommandLabel = QtWidgets.QLabel(self.uiVNCConsoleSettingsGroupBox)
        self.uiVNCConsolePreconfiguredCommandLabel.setObjectName("uiVNCConsolePreconfiguredCommandLabel")
        self.gridLayout_6.addWidget(self.uiVNCConsolePreconfiguredCommandLabel, 0, 0, 1, 1)
        self.uiVNCConsolePreconfiguredCommandComboBox = QtWidgets.QComboBox(self.uiVNCConsoleSettingsGroupBox)
        self.uiVNCConsolePreconfiguredCommandComboBox.setObjectName("uiVNCConsolePreconfiguredCommandComboBox")
        self.gridLayout_6.addWidget(self.uiVNCConsolePreconfiguredCommandComboBox, 1, 0, 1, 1)
        self.uiVNCConsoleCommandLabel = QtWidgets.QLabel(self.uiVNCConsoleSettingsGroupBox)
        self.uiVNCConsoleCommandLabel.setObjectName("uiVNCConsoleCommandLabel")
        self.gridLayout_6.addWidget(self.uiVNCConsoleCommandLabel, 3, 0, 1, 1)
        self.uiVNCConsoleCommandLineEdit = QtWidgets.QLineEdit(self.uiVNCConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVNCConsoleCommandLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVNCConsoleCommandLineEdit.setSizePolicy(sizePolicy)
        self.uiVNCConsoleCommandLineEdit.setObjectName("uiVNCConsoleCommandLineEdit")
        self.gridLayout_6.addWidget(self.uiVNCConsoleCommandLineEdit, 4, 0, 1, 2)
        self.uiVNCConsolePreconfiguredCommandPushButton = QtWidgets.QPushButton(self.uiVNCConsoleSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVNCConsolePreconfiguredCommandPushButton.sizePolicy().hasHeightForWidth())
        self.uiVNCConsolePreconfiguredCommandPushButton.setSizePolicy(sizePolicy)
        self.uiVNCConsolePreconfiguredCommandPushButton.setObjectName("uiVNCConsolePreconfiguredCommandPushButton")
        self.gridLayout_6.addWidget(self.uiVNCConsolePreconfiguredCommandPushButton, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.uiVNCConsoleSettingsGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 294, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.uiMiscTabWidget.addTab(self.uiVNCTab, "")
        self.uiSceneTab = QtWidgets.QWidget()
        self.uiSceneTab.setObjectName("uiSceneTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiSceneTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiSceneWidthLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.gridLayout_8.addWidget(self.uiSceneWidthLabel, 0, 0, 1, 1)
        self.uiSceneHeightLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.gridLayout_8.addWidget(self.uiSceneHeightLabel, 2, 0, 1, 1)
        self.uiRectangleSelectedItemCheckBox = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiRectangleSelectedItemCheckBox.setChecked(True)
        self.uiRectangleSelectedItemCheckBox.setObjectName("uiRectangleSelectedItemCheckBox")
        self.gridLayout_8.addWidget(self.uiRectangleSelectedItemCheckBox, 4, 0, 1, 2)
        self.uiDrawLinkStatusPointsCheckBox = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiDrawLinkStatusPointsCheckBox.setChecked(True)
        self.uiDrawLinkStatusPointsCheckBox.setObjectName("uiDrawLinkStatusPointsCheckBox")
        self.gridLayout_8.addWidget(self.uiDrawLinkStatusPointsCheckBox, 5, 0, 1, 1)
        self.uiLinkManualModeCheckBox = QtWidgets.QCheckBox(self.uiSceneTab)
        self.uiLinkManualModeCheckBox.setChecked(True)
        self.uiLinkManualModeCheckBox.setObjectName("uiLinkManualModeCheckBox")
        self.gridLayout_8.addWidget(self.uiLinkManualModeCheckBox, 6, 0, 1, 2)
        self.uiLabelPreviewLabel = QtWidgets.QLabel(self.uiSceneTab)
        self.uiLabelPreviewLabel.setObjectName("uiLabelPreviewLabel")
        self.gridLayout_8.addWidget(self.uiLabelPreviewLabel, 7, 0, 1, 1)
        self.uiDefaultLabelStylePlainTextEdit = QtWidgets.QPlainTextEdit(self.uiSceneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDefaultLabelStylePlainTextEdit.sizePolicy().hasHeightForWidth())
        self.uiDefaultLabelStylePlainTextEdit.setSizePolicy(sizePolicy)
        self.uiDefaultLabelStylePlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.uiDefaultLabelStylePlainTextEdit.setReadOnly(True)
        self.uiDefaultLabelStylePlainTextEdit.setObjectName("uiDefaultLabelStylePlainTextEdit")
        self.gridLayout_8.addWidget(self.uiDefaultLabelStylePlainTextEdit, 8, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiDefaultLabelFontPushButton = QtWidgets.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelFontPushButton.setObjectName("uiDefaultLabelFontPushButton")
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelFontPushButton)
        self.uiDefaultLabelColorPushButton = QtWidgets.QPushButton(self.uiSceneTab)
        self.uiDefaultLabelColorPushButton.setObjectName("uiDefaultLabelColorPushButton")
        self.horizontalLayout_5.addWidget(self.uiDefaultLabelColorPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 9, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 201, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem5, 10, 1, 1, 1)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(self.uiSceneTab)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setSingleStep(100)
        self.uiSceneHeightSpinBox.setProperty("value", 1000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.gridLayout_8.addWidget(self.uiSceneHeightSpinBox, 3, 0, 1, 2)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(self.uiSceneTab)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setSingleStep(100)
        self.uiSceneWidthSpinBox.setProperty("value", 2000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.gridLayout_8.addWidget(self.uiSceneWidthSpinBox, 1, 0, 1, 2)
        self.uiMiscTabWidget.addTab(self.uiSceneTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiLaunchNewProjectDialogCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiLaunchNewProjectDialogCheckBox.setChecked(True)
        self.uiLaunchNewProjectDialogCheckBox.setObjectName("uiLaunchNewProjectDialogCheckBox")
        self.verticalLayout_2.addWidget(self.uiLaunchNewProjectDialogCheckBox)
        self.uiAutoScreenshotCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiAutoScreenshotCheckBox.setChecked(True)
        self.uiAutoScreenshotCheckBox.setObjectName("uiAutoScreenshotCheckBox")
        self.verticalLayout_2.addWidget(self.uiAutoScreenshotCheckBox)
        self.uiCheckForUpdateCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiCheckForUpdateCheckBox.setChecked(True)
        self.uiCheckForUpdateCheckBox.setObjectName("uiCheckForUpdateCheckBox")
        self.verticalLayout_2.addWidget(self.uiCheckForUpdateCheckBox)
        self.uiCrashReportCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiCrashReportCheckBox.setChecked(True)
        self.uiCrashReportCheckBox.setObjectName("uiCrashReportCheckBox")
        self.verticalLayout_2.addWidget(self.uiCrashReportCheckBox)
        self.uiExperimentalFeaturesCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiExperimentalFeaturesCheckBox.setObjectName("uiExperimentalFeaturesCheckBox")
        self.verticalLayout_2.addWidget(self.uiExperimentalFeaturesCheckBox)
        self.uiSlowStartAllLabel = QtWidgets.QLabel(self.tab)
        self.uiSlowStartAllLabel.setObjectName("uiSlowStartAllLabel")
        self.verticalLayout_2.addWidget(self.uiSlowStartAllLabel)
        self.uiSlowStartAllSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiSlowStartAllSpinBox.setMinimum(0)
        self.uiSlowStartAllSpinBox.setMaximum(10000)
        self.uiSlowStartAllSpinBox.setProperty("value", 0)
        self.uiSlowStartAllSpinBox.setObjectName("uiSlowStartAllSpinBox")
        self.verticalLayout_2.addWidget(self.uiSlowStartAllSpinBox)
        spacerItem6 = QtWidgets.QSpacerItem(20, 318, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.uiMiscTabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.uiMiscTabWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(324, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(GeneralPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_6.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(GeneralPreferencesPageWidget)
        self.uiMiscTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GeneralPreferencesPageWidget)

    def retranslateUi(self, GeneralPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        GeneralPreferencesPageWidget.setWindowTitle(_translate("GeneralPreferencesPageWidget", "General"))
        self.uiLocalPathsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Local paths"))
        self.uiProjectsPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My projects:"))
        self.uiProjectsPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your GNS3 projects are stored"))
        self.uiProjectsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.uiImagesPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My binary images:"))
        self.uiImagesPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your binary images (e.g. IOS) are stored"))
        self.uiImagesPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.uiConfigsPathLabel.setText(_translate("GeneralPreferencesPageWidget", "My configs:"))
        self.uiConfigsPathLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "Directory where your binary images (e.g. IOS) are stored"))
        self.uiConfigsPathToolButton.setText(_translate("GeneralPreferencesPageWidget", "&Browse..."))
        self.uiStyleGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Style"))
        self.uiConfigurationFileGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Configuration file"))
        self.uiImportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Import"))
        self.uiExportConfigurationFilePushButton.setText(_translate("GeneralPreferencesPageWidget", "&Export"))
        self.uiConfigurationFileLabel.setText(_translate("GeneralPreferencesPageWidget", "Unknown location"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiGeneralTab), _translate("GeneralPreferencesPageWidget", "General"))
        self.uiTelnetConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Console settings for Telnet connections"))
        self.uiTelnetConsolePreconfiguredCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Preconfigured commands:"))
        self.uiTelnetConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command:"))
        self.uiTelnetConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%h = device server </p><p>%p = device port</p><p>%d = device hostname</p></body></html>"))
        self.uiTelnetConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Set"))
        self.uiSerialConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Console settings for local serial connections"))
        self.uiSerialConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command:"))
        self.uiSerialConsolePreconfiguredCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Preconfigured commands:"))
        self.uiSerialConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%d = device hostname</p><p>%s = device pipe file</p></body></html>"))
        self.uiSerialConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Set"))
        self.uiConsoleMiscGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Miscellaneous"))
        self.uiCloseConsoleWindowsOnDeleteCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Close any connected console window when deleting a node"))
        self.uiBringConsoleWindowToFrontCheckBox.setToolTip(_translate("GeneralPreferencesPageWidget", "<html>This option will attempt to bring existing opened console window to front, instead of opening a new window.<br>If no existing opened console window exists, it will start a new  console window.</html>"))
        self.uiBringConsoleWindowToFrontCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Bring console window to front (experimental feature)"))
        self.uiSlowConsoleAllLabel.setText(_translate("GeneralPreferencesPageWidget", "Delay between each console launch when consoling to all devices:"))
        self.uiDelayConsoleAllSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " ms"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiConsoleTab), _translate("GeneralPreferencesPageWidget", "Console applications"))
        self.uiVNCConsoleSettingsGroupBox.setTitle(_translate("GeneralPreferencesPageWidget", "Settings for VNC connections"))
        self.uiVNCConsolePreconfiguredCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Preconfigured commands:"))
        self.uiVNCConsoleCommandLabel.setText(_translate("GeneralPreferencesPageWidget", "Console application command:"))
        self.uiVNCConsoleCommandLineEdit.setToolTip(_translate("GeneralPreferencesPageWidget", "<html><head/><body><p>Command line replacements:</p><p>%h = device server </p><p>%p = device port</p><p>%d = device hostname</p></body></html>"))
        self.uiVNCConsolePreconfiguredCommandPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Set"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiVNCTab), _translate("GeneralPreferencesPageWidget", "VNC"))
        self.uiSceneWidthLabel.setText(_translate("GeneralPreferencesPageWidget", "Default width:"))
        self.uiSceneHeightLabel.setText(_translate("GeneralPreferencesPageWidget", "Default height:"))
        self.uiRectangleSelectedItemCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw a rectangle when an item is selected"))
        self.uiDrawLinkStatusPointsCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Draw link status points"))
        self.uiLinkManualModeCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Always use manual mode when adding links"))
        self.uiLabelPreviewLabel.setText(_translate("GeneralPreferencesPageWidget", "Default label style:"))
        self.uiDefaultLabelStylePlainTextEdit.setPlainText(_translate("GeneralPreferencesPageWidget", "AaBbYyZz"))
        self.uiDefaultLabelFontPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default font"))
        self.uiDefaultLabelColorPushButton.setText(_translate("GeneralPreferencesPageWidget", "&Select default color"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " pixels"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.uiSceneTab), _translate("GeneralPreferencesPageWidget", "Topology view"))
        self.uiLaunchNewProjectDialogCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Launch the new project dialog on startup"))
        self.uiAutoScreenshotCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Automatically take a screenshot when saving a project"))
        self.uiCheckForUpdateCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Automatically check for update"))
        self.uiCrashReportCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Automatically send crash reports"))
        self.uiExperimentalFeaturesCheckBox.setText(_translate("GeneralPreferencesPageWidget", "Enable experimental features (Dangerous, require restart)"))
        self.uiSlowStartAllLabel.setText(_translate("GeneralPreferencesPageWidget", "Delay between each device start when starting all devices:"))
        self.uiSlowStartAllSpinBox.setSuffix(_translate("GeneralPreferencesPageWidget", " seconds"))
        self.uiMiscTabWidget.setTabText(self.uiMiscTabWidget.indexOf(self.tab), _translate("GeneralPreferencesPageWidget", "Miscellaneous"))
        self.uiRestoreDefaultsPushButton.setText(_translate("GeneralPreferencesPageWidget", "Restore defaults"))


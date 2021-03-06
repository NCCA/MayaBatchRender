# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatchRenderUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.setEnabled(True)
        mainDialog.resize(799, 484)
        self.gridLayout = QtWidgets.QGridLayout(mainDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.m_fileName = QtWidgets.QLineEdit(mainDialog)
        self.m_fileName.setEnabled(False)
        self.m_fileName.setObjectName("m_fileName")
        self.gridLayout.addWidget(self.m_fileName, 0, 0, 1, 1)
        self.m_chooseFile = QtWidgets.QPushButton(mainDialog)
        self.m_chooseFile.setEnabled(True)
        self.m_chooseFile.setObjectName("m_chooseFile")
        self.gridLayout.addWidget(self.m_chooseFile, 0, 1, 1, 1)
        self.s_renderControlGroupBox = QtWidgets.QGroupBox(mainDialog)
        self.s_renderControlGroupBox.setEnabled(True)
        self.s_renderControlGroupBox.setObjectName("s_renderControlGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.s_renderControlGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.s_gridLayoutGroupBox = QtWidgets.QGridLayout()
        self.s_gridLayoutGroupBox.setObjectName("s_gridLayoutGroupBox")
        self.m_startFrame = QtWidgets.QSpinBox(self.s_renderControlGroupBox)
        self.m_startFrame.setEnabled(True)
        self.m_startFrame.setMaximum(99999)
        self.m_startFrame.setObjectName("m_startFrame")
        self.s_gridLayoutGroupBox.addWidget(self.m_startFrame, 0, 1, 1, 1)
        self.s_byFrame = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_byFrame.setEnabled(True)
        self.s_byFrame.setObjectName("s_byFrame")
        self.s_gridLayoutGroupBox.addWidget(self.s_byFrame, 0, 4, 1, 1)
        self.s_endFrame = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_endFrame.setEnabled(True)
        self.s_endFrame.setObjectName("s_endFrame")
        self.s_gridLayoutGroupBox.addWidget(self.s_endFrame, 0, 2, 1, 1)
        self.m_endFrame = QtWidgets.QSpinBox(self.s_renderControlGroupBox)
        self.m_endFrame.setEnabled(True)
        self.m_endFrame.setMaximum(999999)
        self.m_endFrame.setProperty("value", 1)
        self.m_endFrame.setObjectName("m_endFrame")
        self.s_gridLayoutGroupBox.addWidget(self.m_endFrame, 0, 3, 1, 1)
        self.s_startFrame = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_startFrame.setEnabled(True)
        self.s_startFrame.setObjectName("s_startFrame")
        self.s_gridLayoutGroupBox.addWidget(self.s_startFrame, 0, 0, 1, 1)
        self.s_renderLabel = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_renderLabel.setEnabled(True)
        self.s_renderLabel.setObjectName("s_renderLabel")
        self.s_gridLayoutGroupBox.addWidget(self.s_renderLabel, 1, 0, 1, 1)
        self.m_byFrame = QtWidgets.QSpinBox(self.s_renderControlGroupBox)
        self.m_byFrame.setEnabled(True)
        self.m_byFrame.setMaximum(200)
        self.m_byFrame.setProperty("value", 1)
        self.m_byFrame.setObjectName("m_byFrame")
        self.s_gridLayoutGroupBox.addWidget(self.m_byFrame, 0, 5, 1, 1)
        self.s_pad = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_pad.setEnabled(True)
        self.s_pad.setObjectName("s_pad")
        self.s_gridLayoutGroupBox.addWidget(self.s_pad, 0, 6, 1, 1)
        self.m_pad = QtWidgets.QSpinBox(self.s_renderControlGroupBox)
        self.m_pad.setEnabled(True)
        self.m_pad.setMaximum(10)
        self.m_pad.setObjectName("m_pad")
        self.s_gridLayoutGroupBox.addWidget(self.m_pad, 0, 7, 1, 1)
        self.m_renderer = QtWidgets.QComboBox(self.s_renderControlGroupBox)
        self.m_renderer.setEnabled(True)
        self.m_renderer.setObjectName("m_renderer")
        self.m_renderer.addItem("")
        self.m_renderer.addItem("")
        self.m_renderer.addItem("")
        self.m_renderer.addItem("")
        self.m_renderer.addItem("")
        self.s_gridLayoutGroupBox.addWidget(self.m_renderer, 1, 1, 1, 2)
        self.s_filename = QtWidgets.QLabel(self.s_renderControlGroupBox)
        self.s_filename.setEnabled(True)
        self.s_filename.setObjectName("s_filename")
        self.s_gridLayoutGroupBox.addWidget(self.s_filename, 1, 3, 1, 1)
        self.m_outputFileName = QtWidgets.QLineEdit(self.s_renderControlGroupBox)
        self.m_outputFileName.setEnabled(True)
        self.m_outputFileName.setObjectName("m_outputFileName")
        self.s_gridLayoutGroupBox.addWidget(self.m_outputFileName, 1, 4, 1, 3)
        self.m_extension = QtWidgets.QComboBox(self.s_renderControlGroupBox)
        self.m_extension.setEnabled(True)
        self.m_extension.setObjectName("m_extension")
        self.m_extension.addItem("")
        self.m_extension.setItemText(0, "")
        self.m_extension.addItem("")
        self.m_extension.addItem("")
        self.m_extension.addItem("")
        self.s_gridLayoutGroupBox.addWidget(self.m_extension, 1, 7, 1, 1)
        self.m_outputWindow = QtWidgets.QTextEdit(self.s_renderControlGroupBox)
        self.m_outputWindow.setEnabled(True)
        self.m_outputWindow.setReadOnly(True)
        self.m_outputWindow.setObjectName("m_outputWindow")
        self.s_gridLayoutGroupBox.addWidget(self.m_outputWindow, 2, 0, 1, 8)
        self.gridLayout_3.addLayout(self.s_gridLayoutGroupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.s_renderControlGroupBox, 4, 0, 1, 2)
        self.m_chooseProject = QtWidgets.QPushButton(mainDialog)
        self.m_chooseProject.setEnabled(True)
        self.m_chooseProject.setObjectName("m_chooseProject")
        self.gridLayout.addWidget(self.m_chooseProject, 1, 1, 1, 1)
        self.m_projectDir = QtWidgets.QLineEdit(mainDialog)
        self.m_projectDir.setEnabled(False)
        self.m_projectDir.setObjectName("m_projectDir")
        self.gridLayout.addWidget(self.m_projectDir, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.m_batchRender = QtWidgets.QPushButton(mainDialog)
        self.m_batchRender.setEnabled(True)
        self.m_batchRender.setObjectName("m_batchRender")
        self.gridLayout.addWidget(self.m_batchRender, 7, 1, 1, 1)
        self.m_outputDir = QtWidgets.QLineEdit(mainDialog)
        self.m_outputDir.setEnabled(False)
        self.m_outputDir.setObjectName("m_outputDir")
        self.gridLayout.addWidget(self.m_outputDir, 2, 0, 1, 1)
        self.m_chooseOutputDir = QtWidgets.QPushButton(mainDialog)
        self.m_chooseOutputDir.setEnabled(True)
        self.m_chooseOutputDir.setObjectName("m_chooseOutputDir")
        self.gridLayout.addWidget(self.m_chooseOutputDir, 2, 1, 1, 1)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Maya Batch Render GUI"))
        self.m_chooseFile.setText(_translate("mainDialog", "Choose File"))
        self.s_renderControlGroupBox.setTitle(_translate("mainDialog", "Render Controls"))
        self.s_byFrame.setText(_translate("mainDialog", "by Frame"))
        self.s_endFrame.setText(_translate("mainDialog", "End Frame"))
        self.s_startFrame.setText(_translate("mainDialog", "Start Frame"))
        self.s_renderLabel.setText(_translate("mainDialog", "Renderer"))
        self.s_pad.setText(_translate("mainDialog", "Pad"))
        self.m_renderer.setItemText(0, _translate("mainDialog", "default"))
        self.m_renderer.setItemText(1, _translate("mainDialog", "Use Render Globals"))
        self.m_renderer.setItemText(2, _translate("mainDialog", "V-Ray"))
        self.m_renderer.setItemText(3, _translate("mainDialog", "Renderman"))
        self.m_renderer.setItemText(4, _translate("mainDialog", "Arnold"))
        self.s_filename.setText(_translate("mainDialog", "Output filename"))
        self.m_extension.setItemText(1, _translate("mainDialog", "tiff"))
        self.m_extension.setItemText(2, _translate("mainDialog", "exr"))
        self.m_extension.setItemText(3, _translate("mainDialog", "iff"))
        self.m_chooseProject.setText(_translate("mainDialog", "Choose Proj"))
        self.m_batchRender.setText(_translate("mainDialog", "Batch Render"))
        self.m_chooseOutputDir.setText(_translate("mainDialog", "Choose Output Dir"))

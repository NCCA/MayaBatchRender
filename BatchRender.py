#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from BatchRenderUI import Ui_mainDialog

import os,shutil
import fileinput

class BatchRender(Ui_mainDialog):
	def __init__(self, _mayaPath=None):

		# @brief the name of the maya file to render
		self.m_mayaFile=""
		# @brief the name of the maya project directory
		self.m_mayaProject=""
		# @brief the optional name of the output directory
		self.m_outputDir=""
		# @brief the main ui object which contains our controls
		self.m_ui=Ui_mainDialog()
		# @brief we will use this to thread our render output
		self.m_process=QtCore.QProcess()
		# @brief a flag to indicate if we are rendering or not
		self.m_rendering=False
		# @brief the batch render command constructed from the maya path
		self.m_batchRender="%sbin/Render " %(_mayaPath)
		# now we call the setup UI to populate our gui
		self.m_ui.setupUi(MainDialog)

		print self.m_batchRender

		# here we connect the controls on the UI to the methods in the class

		QtCore.QObject.connect(self.m_ui.m_chooseFile, QtCore.SIGNAL("clicked()"), self.chooseFile)
		QtCore.QObject.connect(self.m_ui.m_chooseProject, QtCore.SIGNAL("clicked()"), self.chooseProject)
		QtCore.QObject.connect(self.m_ui.m_chooseOutputDir, QtCore.SIGNAL("clicked()"), self.chooseOutput)
		QtCore.QObject.connect(self.m_ui.m_batchRender, QtCore.SIGNAL("clicked()"), self.doRender)
		QtCore.QObject.connect(self.m_process, QtCore.SIGNAL("readyReadStandardOutput()"), self.updateDebugOutput)
		QtCore.QObject.connect(self.m_process, QtCore.SIGNAL("readyReadStandardError()"), self.updateDebugOutput)
		QtCore.QObject.connect(self.m_process, QtCore.SIGNAL("started()"), self.updateDebugOutput)
		QtCore.QObject.connect(self.m_process, QtCore.SIGNAL("error()"), self.error)
		QtCore.QObject.connect(self.m_process, QtCore.SIGNAL("finished()"), self.finished)

	def error(self) :
		self.errorDialog("error from process")
	def finished(self) :
		self.m_ui.m_batchRender.setText("Batch Render");

	# a method to popup a file dialog and get the filename
	def chooseFile(self) :
		# pop up a dialog to get the maya file
		self.m_mayaFile=QtGui.QFileDialog.getOpenFileName(None,"Select Maya Scene",".","*")
		# now set the dialog text field
		self.m_ui.m_fileName.setText(self.m_mayaFile)


# a method to popup a file dialog and get the project directory
	def chooseProject(self) :
		# pop up a dialog to get the maya file
		self.m_mayaProject=QtGui.QFileDialog.getExistingDirectory(None,"Choose Project Directory")
		# now set the dialog text field
		self.m_ui.m_projectDir.setText(self.m_mayaProject)

# a method to popup a file dialog and get the project directory
	def chooseOutput(self) :
		# pop up a dialog to get the maya file
		self.m_outputDir=QtGui.QFileDialog.getExistingDirectory(None,"Choose Output Directory")
		# now set the dialog text field
		self.m_ui.m_outputDir.setText(self.m_outputDir)

	def errorDialog(self,_text) :
		QtGui.QMessageBox.about(None,"Warning", _text)



	def doRender(self) :
		if self.m_rendering == True :
			self.m_ui.m_batchRender.setText("Batch Render");
			# stop the batch render process
			self.m_process.kill()
			# clear the output window
			self.m_ui.m_outputWindow.clear()
			self.m_rendering = False
		else :
			""" first we are going to check that we have the correct settings """
			if self.m_mayaFile =="" :
				self.errorDialog("no maya file set")
				return
			if self.m_mayaProject=="" :
				self.errorDialog("no Project directory set")
				return
			if self.m_ui.m_startFrame.value() >= self.m_ui.m_endFrame.value() :
				self.errorDialog("start Frame <= end Frame")
				return
			else :
				print "Doing render"
				self.m_ui.m_batchRender.setText("stop Batch Render");
				# first we need to build up the render string
				renderString=self.m_batchRender
				frameRange="-fnc name.#.ext -s %d -e %d -b %d -pad %d " %(self.m_ui.m_startFrame.value(),
																									 self.m_ui.m_endFrame.value(),
																									 self.m_ui.m_byFrame.value(),
																									 self.m_ui.m_pad.value())
				outputDir=""
				if self.m_ui.m_outputDir.text() != "" :
					outputDir="-rd %s/ " %(self.m_ui.m_outputDir.text())
				outputName=""
				if self.m_ui.m_outputFileName.text() !="" :
					outputName="-im %s "%(self.m_ui.m_outputFileName.text())

				extension=""
				if self.m_ui.m_extension.currentIndex()!=0 :
					extension=" -of %s " %(self.m_ui.m_extension.currentText())

				sceneData="-proj %s %s" %(self.m_mayaProject,self.m_mayaFile)

				Renderers={0:"default",1:"mr",2:"file",3:"hw",4:"rman",5:"sw"}
				rendererString="-renderer %s " %(Renderers.get(self.m_ui.m_renderer.currentIndex()))

				arguments=frameRange+outputName+extension+rendererString+outputDir+sceneData;
				commandString=renderString+arguments
				self.m_ui.m_outputWindow.setText(commandString)
				self.m_process.start(commandString)
				self.m_rendering = True



	def updateDebugOutput(self) :

		data=self.m_process.readAllStandardOutput()
		s=QtCore.QString(data);
		self.m_ui.m_outputWindow.append(s)

		data=self.m_process.readAllStandardError()
		s=QtCore.QString(data);
		self.m_ui.m_outputWindow.append(s)




def QuitApp() :
	sys.exit()


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)

	ResourcePath=os.environ.get("MAYA_LOCATION")

	MainDialog = QtGui.QDialog()
	ui = BatchRender(ResourcePath)

#see if the ResourcePath is set and quite if not
	if ResourcePath == None :
		msgBox=QtGui.QMessageBox()
		msgBox.setText("The environment variable MAYA_LOCATION not set ")
		msgBox.show()
		sys.exit(app.exec_())

	else :

		MainDialog.show()
		sys.exit(app.exec_())

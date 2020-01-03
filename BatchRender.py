#!/usr/bin/env python
#from __future__ import print_function
from PyQt5.QtWidgets import (QApplication,QDialog,QMessageBox,QFileDialog)
from  PyQt5.QtCore import *

from BatchRenderUI import Ui_mainDialog

import os,shutil
import fileinput

class BatchRender(Ui_mainDialog):
	def __init__(self, _mayaPath=None):
		# @brief the name of the maya file to render
		self.m_mayaFile=''
		# @brief the name of the maya project directory
		self.m_mayaProject=''
		# @brief the optional name of the output directory
		self.m_outputDir=''
		# @brief the main ui object which contains our controls
		self.m_ui=Ui_mainDialog()
		# @brief we will use this to thread our render output
		self.m_process=QProcess()
		# @brief a flag to indicate if we are rendering or not
		self.m_rendering=False
		# @brief the batch render command constructed from the maya path
		self.m_batchRender='%s/bin/Render ' %(_mayaPath)
		# now we call the setup UI to populate our gui
		self.m_ui.setupUi(MainDialog)
		print self.m_batchRender
		# here we connect the controls on the UI to the methods in the class
		self.m_ui.m_chooseFile.clicked.connect(self.chooseFile)
		self.m_ui.m_chooseProject.clicked.connect(self.chooseProject)
		self.m_ui.m_chooseOutputDir.clicked.connect(self.chooseOutput)
		self.m_ui.m_batchRender.clicked.connect(self.doRender)
		self.m_process.readyReadStandardOutput.connect(self.updateDebugOutput)
		self.m_process.readyReadStandardError.connect(self.updateDebugOutput)
		self.m_process.started.connect(self.updateDebugOutput)
		self.m_process.error.connect(self.error)
		self.m_process.finished.connect(self.finished)
		self.loadEnvironment()

	def loadEnvironment(self) :
		environment=QProcessEnvironment().systemEnvironment()
		
		with open('Environment.txt') as env :
			lines=env.read().splitlines()
			for line in lines :
				line=line.split(' ')
				print('{} {}'.format(line,len(line)))
				if len(line) >1 :
					print('Env Set {} {}'.format(line[0],line[1]))
					environment.insert(line[0],line[1])
		print(environment.toStringList())
		self.m_process.setProcessEnvironment(environment)	

	def error(self) :
		self.errorDialog('error from process')
	def finished(self) :
		self.m_ui.m_batchRender.setText('Batch Render')

	# a method to popup a file dialog and get the filename
	def chooseFile(self) :
		# pop up a dialog to get the maya file
		self.m_mayaFile,_filter=QFileDialog.getOpenFileName(None,'Select Maya Scene','.','Maya Files(*.ma *.mb)')
		# now set the dialog text field
		if len(self.m_mayaFile) !=0 :
			self.m_ui.m_fileName.setText(self.m_mayaFile)
			print('Maya file set to {}'.format(self.m_mayaFile))


# a method to popup a file dialog and get the project directory
	def chooseProject(self) :
		# pop up a dialog to get the maya file
		self.m_mayaProject=QFileDialog.getExistingDirectory(None,'Choose Project Directory')
		# now set the dialog text field
		if len(self.m_mayaProject) !=0 :
			self.m_ui.m_projectDir.setText(self.m_mayaProject)

# a method to popup a file dialog and get the project directory
	def chooseOutput(self) :
		# pop up a dialog to get the maya file
		self.m_outputDir=QFileDialog.getExistingDirectory(None,'Choose Output Directory')
		# now set the dialog text field
		if len(self.m_outputDir) !=0 :
			self.m_ui.m_outputDir.setText(self.m_outputDir)

	def errorDialog(self,_text) :
		QMessageBox.about(None,'Warning', _text)



	def doRender(self) :
		if self.m_rendering == True :
			self.m_ui.m_batchRender.setText('Batch Render')
			# stop the batch render process
			self.m_process.kill()
			# clear the output window
			self.m_ui.m_outputWindow.clear()
			self.m_rendering = False
		else :
			''' first we are going to check that we have the correct settings '''
			if self.m_mayaFile =='' :
				self.errorDialog('no maya file set')
				return
			if self.m_mayaProject=='' :
				self.errorDialog('no Project directory set')
				return
			if self.m_ui.m_startFrame.value() >= self.m_ui.m_endFrame.value() :
				self.errorDialog('start Frame <= end Frame')
				return
			else :
				print 'Doing render'
				self.m_ui.m_batchRender.setText('stop Batch Render')
				# first we need to build up the render string
				renderString=self.m_batchRender
				frameRange='-of name.#.ext -s %d -e %d -b %d -pad %d ' %(self.m_ui.m_startFrame.value(),
																									 self.m_ui.m_endFrame.value(),
																									 self.m_ui.m_byFrame.value(),
																									 self.m_ui.m_pad.value())
				outputDir=''
				if self.m_ui.m_outputDir.text() != '' :
					outputDir='-rd %s/ ' %(self.m_ui.m_outputDir.text())
				outputName=''
				if self.m_ui.m_outputFileName.text() !='' :
					outputName='-im %s '%(self.m_ui.m_outputFileName.text())

				extension=''
				if self.m_ui.m_extension.currentIndex()!=0 :
					extension=' -of %s ' %(self.m_ui.m_extension.currentText())

				sceneData='-proj %s %s' %(self.m_mayaProject,self.m_mayaFile)

				Renderers={0:'default',1:'file',2:'vray',3:'rman',4:'arnold'}
				rendererString='-renderer %s ' %(Renderers.get(self.m_ui.m_renderer.currentIndex()))

				arguments=frameRange+outputName+extension+rendererString+outputDir+sceneData
				commandString=renderString+arguments
				self.m_ui.m_outputWindow.setText(commandString)
				self.m_process.start(commandString)
				self.m_rendering = True



	def updateDebugOutput(self) :

		data=self.m_process.readAllStandardOutput()
		self.m_ui.m_outputWindow.append(data.data().decode('utf8'))

		data=self.m_process.readAllStandardError()
		self.m_ui.m_outputWindow.append(data.data().decode('utf8'))




def QuitApp() :
	sys.exit()


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)

	ResourcePath=os.environ.get('MAYA_LOCATION')

	MainDialog = QDialog()
	ui = BatchRender(ResourcePath)

#see if the ResourcePath is set and quite if not
	if ResourcePath == None :
		msgBox=QMessageBox()
		msgBox.setText('The environment variable MAYA_LOCATION not set ')
		msgBox.show()
		sys.exit(app.exec_())

	else :

		MainDialog.show()
		sys.exit(app.exec_())

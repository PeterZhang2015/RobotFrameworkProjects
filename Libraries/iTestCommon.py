from SpirentSLC import SLC
from SpirentSLC.Execution import *

import re
import io
import logging
import collections
from time import sleep, time
from datetime import datetime

global session
global sessionMap
global sessionIndex
global index

class iTestCommon(object):

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def connectItest(self, host='localhost:9005'):
		self.slc = SLC.init(host)

	def openProject(self, project='my_project'):
		self.project = self.slc.open(project)

	def startSession(self, name, alias=None):
		global session
		open_command = "self.project." + name + ".open()"
		if (alias is None):
			alias = name
		session = eval(open_command)
		self.sessionIndex[self.index] = alias
		self.sessionMap[alias] = session
		self.session = session
		self.index += 1

	def switchSession(self, index_or_alias):
		global session
		global index
		if self._representsInt(index_or_alias):
			i = int(index_or_alias)
			if (i <= 0 or i >= self.index):
				raise Exception('Invalid index: ' + str(index_or_alias))
			index_or_alias = self.sessionIndex[i]
		try:
			session = self.sessionMap[index_or_alias]
			self.session = session
		except Exception:
			raise Exception('Invalid alias: ' + str(index_or_alias))

	def closeSession(self):
		global session
		session.close()

	def closeAllSessions(self):
		global sessionMap
		global sessionIndex
		global index
		for key, ss in self.sessionMap.items():
			ss.close()
		self.sessionMap = {}
		self.sessionIndex = {}
		self.index = 1

	def _formResponse(self, response):
		if response.json != None:
			return response.json
		else:
			responseDictionary = {'text' : response.text.strip()}
			responseQueryList = eval(response.queries())
			for key in responseQueryList:
				responseDictionary[re.sub('[()]','',key)] = eval('response.' + key)
			return responseDictionary

	def __init__(self):
		self._description = 'common library'
		self.sessionMap = {}
		self.sessionIndex = {}
		self.index = 1
		
	def _getSession(self):
		global session
		return session

	def _representsInt(self, s):
		try: 
			int(s)
			return True
		except ValueError:
			return False

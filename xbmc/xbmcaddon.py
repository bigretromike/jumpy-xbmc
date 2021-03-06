import os, os.path, sys
import xbmcinit

# xbmc/interfaces/python/xbmcmodule/PythonAddon.cpp
# (with a little help from xbmcswift)

class Addon:

	def __init__(self, id=None):
		xid = xbmcinit.read_addon(id)
		if xid is not None:
			self._id = xid
		elif id is not None:
			self._id = id
			_info[self._id] = {}
			_settings[self._id] = {}
			_strings[self._id] = {}
		else:
			self._id = _settings[u'_mainid']
		self.info = _info[self._id]
		self.settings = _settings[self._id]
		self.strings = _strings[self._id]

	def getLocalizedString(self, id):
		"""Returns an addon's localized 'unicode string'."""
		key = str(id)
		if key in self.strings:
			return self.strings[key]
		print '%s not found in addon strings.' % key
		return u''

	def getSetting(self, id):
		"""Returns the value of a setting as a unicode string."""
		if id in self.settings:
			return self.settings[id]
		if id in _settings['xbmc']:
			return _settings['xbmc'][id]
		return ''

	def setSetting(self, id, value):
		"""Sets a script setting."""
		print "*** setSetting *** %s=%s" % (id, value)
		self.settings[id] = value
		xbmcinit.changed.add(self._id)

	# sometimes called with an arg, e.g veehd
	def openSettings(self, arg=None):
		"""Opens this scripts self.settings dialog."""
		print "*** openSettings ***"

	def getAddonInfo(self, id):
		"""Returns the value of an addon property as a string."""
		properties = ['author', 'changelog', 'description', 'disclaimer',
			'fanart', 'icon', 'id', 'name', 'path', 'profile', 'stars', 'summary',
			'type', 'version']
		key = id.lower()
		assert key in properties, '%s is not a valid property.' % id
		return self.info[key] if key in self.info else ''



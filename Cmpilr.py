import sublime, sublime_plugin
import os.path
from urlparse import urlparse
from httplib import HTTPConnection
from httplib import HTTPSConnection
import re

class Cmpilr(sublime_plugin.EventListener):

	def __init__(self):
		settings = sublime.load_settings('Cmpilr.sublime-settings')
		self.cmpilr_url = settings.get("cmpilr_url")
		self.compilers = settings.get("compilers")
		self.force_overwrite = settings.get("force_overwrite")

	def on_post_save(self,view):
		file_name = str(view.file_name())
		from_ext = os.path.splitext(file_name)[1][1:]

		if not from_ext in self.compilers.keys(): return

		to_ext = self.compilers[from_ext]
		f = open(file_name)
		source = f.read()
		f.close()
		if len(source) == 0:
			return
		(status,compiled) = self.compile(source, from_ext)
		if status != 200:
			sublime.error_message("Compile Failed!!\n\n" + compiled)
			return
		compiled_file_path = re.sub(r'\.{0}$'.format(from_ext), '.' + to_ext, file_name)
		print(file_name)
		print("\n")
		print(compiled_file_path)
		if not self.force_overwrite and os.path.exists(compiled_file_path) and not sublime.ok_cancel_dialog("overwirte? " + compiled_file_path):
			print "cancel overwrite"
			return

		self.write(compiled_file_path, compiled)
		print 'compiled!!'

	def compile(self, source, extension):
		urlparts = urlparse(str(self.cmpilr_url) + '/' + extension + '/')
		conn = HTTPSConnection(urlparts.netloc, urlparts.port or 443) if urlparts.scheme == 'https' else HTTPConnection(urlparts.netloc, urlparts.port or 80)
		conn.request('POST', urlparts.path, source, { 'Content-Type' : 'application/octet-stream'})
		resp = conn.getresponse()
		return (resp.status, resp.read())

	def write(cls, file, data):
		with open(file, "w") as f:
			f.write(data)

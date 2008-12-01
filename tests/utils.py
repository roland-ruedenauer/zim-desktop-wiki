# -*- coding: utf8 -*-

# Copyright 2008 Jaap Karssenberg <pardus@cpan.org>

from tests import TestCase

from zim.fs import Buffer
from zim.utils import *

class testUtils(TestCase):

	def testSplitWords(self):
		string = r'''"foo bar", "\"foooo bar\"" dusss ja'''
		list = ['foo bar', ',', '"foooo bar"', 'dusss', 'ja']
		result = split_quoted_strings(string)
		self.assertEquals(result, list)
		list = ['"foo bar"', ',', r'"\"foooo bar\""', 'dusss', 'ja']
		result = split_quoted_strings(string, unescape=False)
		self.assertEquals(result, list)

	def testRe(self):
		string = 'foo bar baz';
		re = Re('f(oo)\s*(bar)')
		if re.match(string):
			self.assertEquals(len(re), 3)
			self.assertEquals(re[0], 'foo bar')
			self.assertEquals(re[1], 'oo')
			self.assertEquals(re[2], 'bar')
		else:
			assert False, 'fail'

	def testListDict(self):
		keys = ['foo', 'bar', 'baz']
		mydict = ListDict()
		for k in keys:
			mydict[k] = 'dusss'
		mykeys = [k for k, v in mydict.items()]
		self.assertEquals(mykeys, keys)

	def testConfigList(self):
		input = u'''\
foo	bar
	dusss ja
# comments get taken out
some\ space he\ re # even here
'''
		output = u'''\
foo\tbar
dusss\tja
some\ space\the\ re
'''
		keys = ['foo', 'dusss', 'some space']
		mydict = ConfigList()
		mydict.read(Buffer(input))
		mykeys = [k for k, v in mydict.items()]
		self.assertEquals(mykeys, keys)
		result = Buffer()
		mydict.write(result)
		self.assertEquals(result.getvalue(), output)
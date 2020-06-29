import re
import json
import unittest
from collections import namedtuple
from io import StringIO
from typing import Optional, Union, re as re_t, Iterator
from unittest.result import TestResult

from ndjson_testrunner import JSONTestRunner


StructuredResult = namedtuple('StructuredResult', 'type id desc msg')


class TestsToBeTested(unittest.TestCase):
	"""Those tests are not there to pass, but to create all kinds of output"""
	def test_success(self):
		pass

	def test_failure(self):
		self.assertFalse(True)

	def test_error(self):
		raise Exception('Something went wrong')

	def test_subtest_success(self):
		with self.subTest('a succeeding subtest'):
			pass

	def test_subtest_failure(self):
		with self.subTest('a failing subtest'):
			self.test_failure()

		with self.subTest('an erroring subtest'):
			self.test_error()


class TestRunner(unittest.TestCase):
	def setUp(self):
		self.capture = StringIO()
		self.runner = JSONTestRunner(self.capture)

	def run_test(self, name: str, subtests=False) -> Union[dict, Iterator[dict]]:
		self.runner.run(unittest.defaultTestLoader.loadTestsFromName('tests.TestsToBeTested.{}'.format(name)))
		v = self.capture.getvalue()
		self.assertTrue(v, 'no JSON received')
		if subtests:
			return map(json.loads, v.strip().split('\n'))
		else:
			self.assertNotIn('\n', v.strip(), 'expected 1 ndjson record')
			return json.loads(v)

	def check_test(self, test: Union[str, dict], typ: str, id_: str, desc: Optional[str], msg_re: Union[str, re_t.Pattern]):
		if isinstance(test, str):
			test = self.run_test(test)
		self.assertSetEqual(set(test.keys()), {'type', 'id', 'desc', 'msg'})
		result = StructuredResult(**test)
		self.assertEqual(result.type, typ)
		self.assertEqual(result.id, id_)
		self.assertEqual(result.desc, desc)
		if result.msg is not None:
			self.assertRegex(result.msg, re.compile(msg_re, re.DOTALL))
		return result

	def test_success(self):
		"""Test a normal succeeding tests"""
		self.check_test(
			'test_success', 'success',
			'tests.TestsToBeTested.test_success',
			None, None)

	def test_failure(self):
		"""Test a normal failing tests"""
		self.check_test(
			'test_failure', 'failure',
			'tests.TestsToBeTested.test_failure',
			None,
			r'^Traceback.*in test_failure.*AssertionError: True is not false\n$')

	def test_error(self):
		self.check_test(
			'test_error', 'error',
			'tests.TestsToBeTested.test_error',
			None,
			r'^Traceback.*in test_error.*Exception: Something went wrong\n$')

	def test_subtest_success(self):
		"""Test if subtests result in the whole thing to pass"""
		succ_sub, succ_total = self.run_test('test_subtest_success', subtests=True)
		self.check_test(
			succ_sub, 'success',
			'tests.TestsToBeTested.test_subtest_success [a succeeding subtest]',
			None, None)
		self.check_test(
			succ_total, 'success',
			'tests.TestsToBeTested.test_subtest_success',
			None, None)

	def test_subtest_failure(self):
		"""Test if all subtests run"""
		fail, error = self.run_test('test_subtest_failure', subtests=True)
		self.check_test(
			fail, 'failure',
			'tests.TestsToBeTested.test_subtest_failure [a failing subtest]',
			None,
			r'^Traceback.*in test_subtest_failure.*AssertionError: True is not false\n$')
		self.check_test(
			error, 'error',
			'tests.TestsToBeTested.test_subtest_failure [an erroring subtest]',
			None,
			r'^Traceback.*in test_error.*Exception: Something went wrong\n$')


def load_tests(loader: unittest.TestLoader, standard_tests: unittest.TestSuite, pattern: Optional[str]):
	return unittest.TestSuite(loader.loadTestsFromTestCase(TestRunner))

if __name__ == '__main__':
	unittest.main()

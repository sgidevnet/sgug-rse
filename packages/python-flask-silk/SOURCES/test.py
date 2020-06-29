import unittest
from flask import Flask, Module
from flaskext.silk import Silk


class ApplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.silk = Silk(self.app)

    def test_icon(self):
        rv = self.app.test_client().get("/icons/page_white.png")
        assert 294 == len(rv.data), "could not found an icon file."


class ModuleTestCase(unittest.TestCase):

    def test_urlprefix(self):
        app = Flask(__name__)
        mod = Module(__name__ + ".foo", url_prefix="/foo")
        silk = Silk(mod)
        app.register_module(mod)
        rv = app.test_client().get("/foo/icons/page_white.png")
        assert 294 == len(rv.data), "could not found an icon file."

    def test_subdomain(self):
        app = Flask(__name__)
        app.config["SERVER_NAME"] = "example.org"
        mod = Module(__name__ + ".foo", subdomain="foo")
        silk = Silk(mod)
        app.register_module(mod)
        rv = app.test_client().get("/icons/page_white.png",
                                   "http://foo.example.org/")
        assert 294 == len(rv.data), "could not found an icon file."


import unittest
from warnings import catch_warnings, filterwarnings
from contextlib import contextmanager
from uuid import uuid4

from outdated import check_outdated, utils, OutdatedCacheFailedWarning, warn_if_outdated, OutdatedPackageWarning, \
    OutdatedCheckFailedWarning
from outdated.utils import constantly


@contextmanager
def mock(old, new):
    name = old.__name__
    setattr(utils, name, new)
    try:
        yield
    finally:
        setattr(utils, name, old)


def fail(*_, **__):
    raise ValueError('Error message here')


def disable_cache():
    return mock(utils.cache_is_valid, constantly(False))


def fresh_cache():
    return mock(utils.get_cache_filename, constantly(uuid4().hex))


def fail_cache():
    return mock(utils.get_cache_filename, fail)


def fail_get_url():
    return mock(utils.get_url, fail)


class OutdatedTests(unittest.TestCase):
    version = '1.0.4'
    package = 'ask-so'

    @contextmanager
    def assert_warns(self, category, message):
        message += '\nSet the environment variable OUTDATED_IGNORE=1 to disable these warnings.'
        with catch_warnings(record=True) as w:
            filterwarnings("ignore", "^Not importing directory .+ missing __init__$", ImportWarning)
            yield
            failure_message = "Warnings found: %s" % [x.message for x in w]
            self.assertEqual(len(w), 1, failure_message)
            self.assertEqual(w[0].category, category, failure_message)
            self.assertEqual(str(w[0].message), message, failure_message)

    def test_basic(self):
        with disable_cache():
            self.example_check()

            self.assertEqual(check_outdated(self.package, '1.0'),
                             (True, self.version))

            self.assertEqual(check_outdated(self.package, self.version),
                             (False, self.version))

            self.assertEqual(check_outdated(self.package, self.version + '.0'),
                             (False, self.version))

    def test_caching(self):
        with fresh_cache():
            self.example_check()
            with fail_get_url():
                self.example_check()

    def test_cache_failure(self):
        with fail_cache():
            with self.assert_warns(
                    OutdatedCacheFailedWarning,
                    ('Failed to use cache while checking for outdated package.\n'
                     'Set the environment variable OUTDATED_RAISE_EXCEPTION=1 for a full traceback.')):
                self.example_check()
                self.example_check()

    def example_check(self):
        self.assertEqual(check_outdated(self.package, '0.1'),
                         (True, self.version))

    def test_warn_if_outdated(self):
        with catch_warnings(record=True) as w:
            warn_if_outdated(self.package, self.version, raise_exceptions=True, background=False)
            self.assertEqual(len(w), 0)

        with self.assert_warns(OutdatedPackageWarning,
                               ('The package ask-so is out of date. '
                                'Your version is 0.1, the latest is 1.0.4.')):
            warn_if_outdated(self.package, '0.1', raise_exceptions=True, background=False)

        with disable_cache():
            with fail_get_url():
                with self.assert_warns(
                        OutdatedCheckFailedWarning,
                        ('Failed to check for latest version of package.\n'
                         'Set the environment variable OUTDATED_RAISE_EXCEPTION=1 for a full traceback.')):
                    warn_if_outdated(self.package, '0.1', background=False)

                with self.assertRaises(ValueError):
                    warn_if_outdated(self.package, '0.1', raise_exceptions=True, background=False)

        warn_if_outdated(self.package, self.version)

    def test_stale_cache_new_package(self):
        with fresh_cache():
            self.example_check()  # caches the older latest version

            with self.assertRaises(ValueError):
                check_outdated(self.package, '5.0')

            # Suppose that a new version comes out and has just been installed:
            # the cache must be refreshed
            with mock(utils.get_url, constantly('{"info": {"version": "5.0"}}')):
                self.assertEqual(check_outdated(self.package, '5.0'),
                                 (False, '5.0'))


if __name__ == '__main__':
    unittest.main()

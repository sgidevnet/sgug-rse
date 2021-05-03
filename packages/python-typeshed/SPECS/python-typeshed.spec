%global checkout 8f47637

Name:           python-typeshed
# There are no actual releases of typeshed so we are making one up
Version:        0.1
Release:        0.20170617git%{?dist}
Summary:        Static type information for python modules

License:        ASL 2.0
URL:            https://github.com/python/typeshed
# git archive --prefix=typeshed-0.1-7c706e1/ 7c706e1 | gzip -c9 >typeshed-0.1-7c706e1.tar.gz
Source0:        typeshed-%{version}-%{checkout}.tar.gz

BuildArch:      noarch

%description
Typeshed models function types for the Python standard library
and Python builtins, as well as third party packages.

This data can e.g. be used for static analysis, type checking or type inference.

This package stores the typedata in /usr/share/typeshed

%prep
%autosetup -n typeshed-%{version}-%{checkout}

%build
# All stub files, nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/typeshed
for dir in stdlib third_party ; do
    cp -r $dir %{buildroot}/%{_datadir}/typeshed/$dir
done

%files
%doc README.md
%license LICENSE
%{_datadir}/typeshed

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20170617git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20170616git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20170615git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20170614git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20170613git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.1-0.20170612git
- Latest upstream.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20161223git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 CAI Qian <caiqian@redhat.com> - 0.1.0-20161222
- Update to the latest upstream 7c706e1

* Mon Jul 18 2016 David Shea - 0.1.0-20160713
- Add http_client to six.moves, add missing functions to urllib2 fix some types in gettext
- Fix types.MappingProxyType
- Fix heapq.merge signature for Python >= 3.5
- Add full class definitions for Process, Queue, and Lock
- Make Empty a subclass of Exception
- add types to logging
- make xml.etree.ElementTree.Element a Sequence
- Improve socket py2
- Improve http
- Add logging.WARN; TextIO -> IO[str]
- Fix log() signatures; change msg: str to msg: Text.
- Changed all regular expression findall() to return list[Any].
- Allow use of kwargs in MutableMapping.update
- add types to socketserver for py2
- fix sys.exc_info return type
- Fix argument type for datetime.now.
- re methods' pattern-parameters don't affect the return value anymore
- fleshing out some more stubs for sqlalchemy
- Fix argument type for configparser.write
- Add TYPE_CHECKING = True
- Fix email typing errors
- First cut at stubs for pymssql.
- Make os.name `str` in python 3.
- changed format_exception to use BaseException as value
- Added os.sync, os.truncate and os.fwalk for Python version >= 3.3
- Use "..." for attribute values, instead of None, [], {}
- csv module: make reader() and writer() return types private and non-abstract
- add stub for stdlib abc.ABC in python 3.4+
- a few more stubs for sqlalchemy
- Fix names of several stat constants
- difflib functions return Iterators, not Iterables
- Add stub for statvfs and type for fstatvfs (2.7)
- Use unicode rather than str for os env functions
- adding type-specific assertEqual cases
- Add stubs for importlib.__init__
- Use actual base type
- Annotate **kwargs with dictionary value type only
- stdlib: StringIO - Add len attribute
- Fix bad syntax in two stubs.
- Implement stubs for importlib.abc and update types.ModuleType
- Add stubs for importlib.machinery
- Add tarfile.open
- Add stubs for importlib.util
- fix return type for traceback.format_exception
- Make the 'symmetric' argument to SQLAlchemy's between optional.
- Add exec to Python 2 builtins
- Set a default value for output in CalledProcessError.__init__
- ModuleType has a __file__ attribute.
- Fix some stubs in urllib.parse
- email.header: Make decode_header also accept str.
- Added JSONEncoder and JSONDecoder to stdlib/2.7/json.pyi
- os: Add buffering to fdopen.
- Add stubs for dis and opcode
- Attempt to reduce cyclical dependencies between types and importlib.
- Add types to stub for warnings module.
- Fix signatures of call, check_call and check_output in subprocess
- Correct type of formatter_class arg to ArgParse()
- improve unittest
- First pass at dateutil
- Add stdlib/2.7/traceback._print
- Update set methods to take multiple iterables
- Add cmp to list.sort in python 2.7
- __builtin__: Fix bytearray on python 2
- add bytearray.insert
- add some types to os
- merge py2 and py3 argparse
- Two small changes to help the mypy test suite pass
- Fix some issues for dateutil and argparse
- subprocess: Fix return type of check_output.
- Add stub for boto.exception
- add default arguments to traceback.format_exception
- add ChainMap class to collections module
- More fixes for argparse.
- builtins: Remove Exception.message.
- Mypy stub fixes for strict optional mode

* Mon Jun 13 2016 David Shea - 0.1.0-20160603git
- Added type annotations and small fixes
- Add stub version of Type[C]
- Don't use basestring in tempfile stub
- Added stdlib/2.7/getopt.pyi, updated 3/getopt.pyi
- Fix setsockopt signature.
- specifiy Callable in sys.call_tracing
- more closely fit to html.parser documentation
- Improve email.*
- add types to sys.getrefcount
- complete urllib
- add types to socket.socket.send{,all}
- complete socketserver
- complete ssl
- Initial stubs for tkinter
- Support for 'from six.moves import http_cookies'
- Correct return value of round in Python 2.
- Fixes a few tzinfo method's return type
- Update calendar.pyi `timegm` to accept arbitrary length tuples

* Fri May 20 2016 David Shea - 0.1-0.20160520git
- add AST.__init__ annotation
- Change datetime.datetime.astimezone tz argument type from timezone to tzinfo
- A couple new definitions, some more unicode for 2.7
- Fix html.escape signature
- Add types for gettext
- Fix type of getsockopt
- type `errors` in codecs.EncodedFile
- Add __version__ to requests
- Use __delete__, not __del__, in class property.
- getpass return str
- Make property a type
- Almost all re functions take a compiled pattern.
- Add note about not using basestring in tempfile
- Accept more unicode in 2.7 tempfile stubs
- Add some missing "type" attributes
- fix integration of io with mypy
- Add apply() and coerce() to 2.7 builtins.
- Add __future__.generator_stop for Python 3.5
- Fix subprocess stubs
- improve io
- Add os.replace()
- enable string arguments for start, end, and span methods of Match object

* Tue May 17 2016 David Shea - 0.1-0.20160505git
- Fix and greatly expand stubs for sqlalchemy.
- Expand the sqlalchemy stubs related to the Column model.
- Type Check webbrowser py3 module
- Add missing exec*, EX_* stubs for python 2 and fix py3 types.
- Add py2 webbrowser type checking
- Fix urlunparse stubs for 2.7 to correctly support a list/iterator argument
- Improvements to builtins min/max
- Add missing definition of compile() for 2.7.
- Add abc.abstractproperty (Python 3)
- Fix incorrect sys.exit() type.
- Additional type information for asyncio
- Fix type for reduce
- Remove invalid Python 3 syntax
- Fix asyncio.coroutine signature
- Stub for calendar module
- Stub for shelve
- Remove contents of problematic asyncio __all__s
- Fixed 2.7 stubs for traceback
- Specify attribute types of SyntaxError
- Define three argument type() overload (Python 3)
- reduce use of @overload in socket stubs
- Update stub for zlib
- Update stub for gc
- Add stub for multiprocessing.cpu_count()
- Stubs for pdb (only the most useful functions).
- Add missing import of List from typing.
- Fix traceback.pyi right.
- Fix typos: termina[ta]te()
- Make tests version-aware.
- Type check xml.etree module
- Improve Python 2.7 inspect stub
- sqlite3 stub for 2.7  and 3
- Fix Python 2.7 inspect stub (currentframe + frame type)
- Improve Python 3 inspect stub
- Add tornado.locks module
- Make all function annotations accessible from builtins complete
- Allow adding custom argparse.Actions in add_argument
- Bandaid for sqlalchemy.
- Stubs for setuptools' pkg_resources package
- Ignore Emacs backup files
- Complete getpass stubs
- Add stubs for configparser
- Complete pickle stubs
- Complete pickle and cPickle stubs for Python 2
- remove superfluous type comment in urllib.pyi
- Better stub for contextlib.contextmanager.
- add stdlib/2.7/heapq.pyi
- Use IO[bytes] instead of BytesIO in the pickle stub.
- Improve Python 3 fcntl stub
- Add version keyword arg to argparse.ArgumentParser.add_argument
- Fix signature for reduce in some files.
- Hopeful fix for fcntl stubs
- fileinput first version
- Update dbapi2.pyi to allow `execute` without binding params
- add `__dict__` attribute to class instance
- Add note about obtaining consent of package owner for third-party stubs.
- Implement itertools.chain.from_iterable().
- Added stubs for 2.7 Selenium WebElement
- Add missing return type for __init__()
- Add 2.7/optparse.pyi
- change ='' to :str=... in httplib
- Move warnings.pyi into 2and3/.
- Enable typing.DefaultDict as an alias for collections.defaultdict
- Precision surgery to take out sqlalchemy test failures
- Fix select stub for 2.7
- Various updates to stdlib modules
- py3: traceback.pyi: added format_stack
- Add a very basic bz2 stub
- Simple stub for tornado.testing
- Break cycle between typing and collections.
- Update dict(...) to accept keyword arguments
- Add Text to typing.pyi
- Support keyword arguments for dict() (Python 2)
- 2.7 stub updates
- Add stdlib/3/tokenize.pyi
- Change logging signatures to allow unicode
- Fix type error in 2.7 stubs
- Fixes to urllib2 stubs
- Make Queue generic in Python 2, similar to Python 3
- dateutil stubs
- Fix Py2 hashlib.new arg type
- Add stubs for typed_ast
- Add type.__call__.
- Add missing 3.3+ and 3.5+ math functions
- stdlib/2.7./codecs.pyi: added missing __enter__() and __exit__()
- Fixes to os.environ
- Use overloading rather than Union for MutableMapping.update
- Add abc.ABCMeta.register method
- json.dump{s,}' indent parameter also supports str
- pprint stream type
- Finish Python 3 hashlib stub
- Added bisect.pyi and ConfigParser.pyi
- Add Python 3 ast module; update Python 2.7 ast module; fixup typed_ast
- Fix 2.7 bisect stubs (lo/hi have defaults).
- Misc stub fixes

* Mon Feb 22 2016 David Shea - 0.1-0.20160222git
- Better approach to testing.
- Fix and greatly expand stubs for sqlalchemy.
- Expand the sqlalchemy stubs related to the Column model.
- Type Check webbrowser py3 module
- Add missing exec*, EX_* stubs for python 2 and fix py3 types.
- Add py2 webbrowser type checking
- Fix urlunparse stubs for 2.7 to correctly support a list/iterator argument
- Improvements to builtins min/max
- Try using "pip install -U ..." to install mypy
- Add missing definition of compile() for 2.7.
- Add abc.abstractproperty (Python 3)
- Fix incorrect sys.exit() type.
- Additional type information for asyncio

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20160129git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 David Shea <dshea@redhat.com> - 0.1-0.20160128git
- Add timer class to threading.pyi
- Assorted stub updates
- Some fixes to threading
- Add Iterable base class to csv.DictReader.
- Replace some unicode argument defaults with ...
- Use NamedTuple for inspect.ArgSpec and .FullArgSpec.
- Make Future stub resemble reality better.
- Make asyncio more Generator friendly
- Fix default parameter syntax.
- Fix os.environ improperly classified as not mutable for python 2.
- Implement fromhex and maketrans method
- Add missing re module constants for 2.7.
- Add message attribute to class BaseException.
- Fix several python 2 library stub errors.
- Fix class file so it can be used as "with file(...) as f: f.read() # etc.
- Fix min()/max() overloading with key= parameter.
- Fix stubs for concurrent.futures
- Fix type for py2 traceback.format_exc and add to python 3.
- Add stubs for traceback.format_exception.
- Port stub for os.walk from python 3 to 2 and cleanup comment.
- Fix datetime.timedelta() argument types to be floats.
- Add a Travis CI configuration.
- Add stdlib/2.7 to Travis CI tests.
- Test 2and3, 3.3, 3.4.
- Add stubs for some of the most heavily used parts of six.moves
- Revert "Fix min()/max() overloading with key= parameter.
- Fix signature for 2.7/binascii.crc32().
- Fix constructor signatures to 2.7/cPickle.{Pickler,Unpickler}.
- Copy frozenset stubs from 3/builtins.pyi into 2.7/__builtin__.pyi.
- Add 2.7 stubs for dict.fromkeys().
- Fix ast.parse(). The 2nd and 3rd arg are optional.
- Expand stubs for simplejson, unittest, email
- Comment out references to modules without stubs introduced by accident.
- Add html module stubs.
- Add various annotations to complete more of six.moves.

* Fri Jan 15 2016 David Shea <dshea@redhat.com> - 0.1-0.20160115git
- 2.7 does not have lru_cache()
- Add keyword args to stdlib's json.pyi
- Add Generator to 2.7/typing.pyi.
- Make Reversible covariant.
- Fix Reversible.__reversed__() return type.
- Add flush keyword arg to print()
- Move contents of builtins/* to stdlib/*. This simplifies finding stubs.
- Remove outdated things from README.
- Make deque inherit from MutableMapping (with difficulty).

* Mon Jan 11 2016 David Shea <dshea@redhat.com> - 0.1-0.20160111git
- Fix types for timetuple and utctimetuple
- Fix Python 3 six.moves
- Have ast.pyi re-export symbols from _ast.pyi.
- Unify 2.7 and 3 stubs for functools.
- Enhance type information for lru_cache

* Thu Jan  7 2016 David Shea <dshea@redhat.com> - 0.1-0.20160107git.1
- typing: update 2 to match 3 on Sequence and Container
- builtins: Reversible is redundant when Sequence is already present
- Add __version__ to _ast.pyi.
- add Python 2 stubs for ast, tokenize
- Improve Python 2 stub for abc; _weakrefset stub.
- Update shlex.pyi
- Update random.pyi
- Add abstractproperty.__new__ so it can be used.
- Add object.__new__ so it can be called.
- Update 2.7 built-in set to be the same as PY3 set.
- Swap max() and min() overloads so max(x, y) and min(x, y) work as expected.
- Improve 2.7 stub for tempfile.
- Simplify SystemRandom now it subclasses Random, for 2.7 and 3.
- Add object.__setattr__ for 2.7.
- Simplify PY3 len() spec, no Union with tuple needed.
- Some updates now typing.Container is defined.
- Add cStringIO, cPickle to six.moves. Add six.moves for PY3.

* Fri Dec 18 2015 David Shea <dshea@redhat.com> - 0.1-0.20151217git.1
- Rebuild with the correct prefix in the source archive

* Fri Dec 18 2015 David Shea <dshea@redhat.com> - 0.1-0.20151217git
- Share operator stubs in 2and3
- Make attrgetter, itemgetter and methodcaller in operator usable

* Tue Dec 15 2015 David Shea <dshea@redhat.com> - 0.1-0.20151205git
- Initial package

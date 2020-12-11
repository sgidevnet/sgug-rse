%global srcname Werkzeug

Name:           python-werkzeug
Version:        0.14.1
Release:        10%{?dist}
Summary:        The Swiss Army knife of Python web development 

License:        BSD
URL:            http://werkzeug.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/W/Werkzeug/%{srcname}-%{version}.tar.gz
# Pypi version of werkzeug is missing _themes folder needed to build werkzeug sphinx docs
# See https://github.com/mitsuhiko/werkzeug/issues/761
Source1:        werkzeug-sphinx-theme.tar.gz

# https://github.com/pallets/werkzeug/pull/1293
# skip all tests that use xprocess when it's not installed (like here,
# as it's not packaged for Fedora...)
Patch0:         1293.patch

# Use sys.executable in tests
Patch1:         https://github.com/pallets/werkzeug/pull/1455.patch

# Python 3.8 support in tests
# https://github.com/pallets/werkzeug/commit/e060800e8e6e0c611f9439d746bd4da99a314b79
Patch2:         python38.patch

BuildArch:      noarch

%global _description\
Werkzeug\
========\
\
Werkzeug started as simple collection of various utilities for WSGI\
applications and has become one of the most advanced WSGI utility\
modules.  It includes a powerful debugger, full featured request and\
response objects, HTTP utilities to handle entity tags, cache control\
headers, HTTP dates, cookie handling, file uploads, a powerful URL\
routing system and a bunch of community contributed addon modules.\
\
Werkzeug is unicode aware and doesn't enforce a specific template\
engine, database adapter or anything else.  It doesn't even enforce\
a specific way of handling requests and leaves all that up to the\
developer. It's most useful for end user applications which should work\
on as many server environments as possible (such as blogs, wikis,\
bulletin boards, etc.).\


%description %_description

%package -n python2-werkzeug
Summary: %summary

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests
BuildRequires:  python2-pytest
BuildRequires:  python2-hypothesis
BuildRequires:  python2-requests

# Don't remove before Fedora 33:
Obsoletes:      python2-werkzeug-doc < 0.14.1-8

%{?python_provide:%python_provide python2-werkzeug}

%description -n python2-werkzeug %_description

%package -n python3-werkzeug
Summary:        %summary

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-greenlet
BuildRequires:  python3-redis
BuildRequires:  python3-memcached

%{?python_provide:%python_provide python3-werkzeug}

%description -n python3-werkzeug %_description


%package -n python3-werkzeug-doc
Summary:        Documentation for python3-werkzeug

BuildRequires:  python3-sphinx

Requires:       python3-werkzeug = %{version}-%{release}
%{?python_provide:%python_provide python3-werkzeug-doc}

%description -n python3-werkzeug-doc
Documentation and examples for python3-werkzeug.


%prep
%autosetup -p1 -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE
%{__sed} -i '1d' tests/multipart/test_collect.py
tar -xf %{SOURCE1}

rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py2_build
find examples/ -name '*.py' -executable | xargs chmod -x
find examples/ -name '*.png' -executable | xargs chmod -x

pushd %{py3dir}
%py3_build
find examples/ -name '*.py' -executable | xargs chmod -x
find examples/ -name '*.png' -executable | xargs chmod -x
pushd docs
# Add a symlink to the dir with the Python module so that __version__ can be
# obtained therefrom.
ln -s ../werkzeug werkzeug
make SPHINXBUILD=sphinx-build-3 html
popd
popd
mv %{py3dir}/docs ./docs3


%install
%py2_install
%{__rm} -rf docs/_build/html/.buildinfo
%{__rm} -rf examples/cupoftee/db.pyc

pushd %{py3dir}
%py3_install
%{__rm} -rf docs/_build/html/.buildinfo
%{__rm} -rf examples/cupoftee/db.pyc
popd

%check
# PYTHONPATH=./ is usually unnecessary with pytest, but it is needed here
# for testing werkzeug's reloader.
PYTHONPATH=./ %{__python2} -m pytest

pushd %{py3dir}
PYTHONPATH=./ %{__python3} -m pytest
popd

%files -n python2-werkzeug
%license LICENSE
%doc AUTHORS PKG-INFO CHANGES.rst
%{python2_sitelib}/*

%files -n python3-werkzeug
%license LICENSE
%doc AUTHORS PKG-INFO CHANGES.rst
%{python3_sitelib}/*

%files -n python3-werkzeug-doc
%doc docs3/_build/html examples


%changelog
* Mon Jul 29 2019 Petr Viktorin <pviktori@redhat.com> - 0.14.1-10
- Remove non-essential Python 2 test dependencies
  https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal#Removing_Requirements
- Use system Python interpreter in tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-8
- Remove python2-werkzeug-doc
  https://fedoraproject.org/wiki/Changes/Sphinx2

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14.1-7
- Backport fix to tests using 'python' command

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-5
- Make sure we ship Python 3 docs in the Python 3 docs package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-2
- Don't BR watchdog, it is not needed

* Wed May 09 2018 Adam Williamson <awilliam@redhat.com> - 0.14.1-1
- Update to 0.14.1 (needed by httpbin)
- Run tests during build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.11.10-8
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.10-7
- Python 2 binary package renamed to python2-werkzeug
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.11.10-4
- Rebuild for Python 3.6

* Tue Dec 13 2016 Tomas Orsava <torsava@redhat.com> - 0.11.10-3
- Fixed the building of documentation

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.10-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 28 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.11.10-1
- Upstream 0.11.19
- Fix unicode issues with python3

* Thu Apr 14 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.11.6-1
- Upstream 0.11.6 (upstream #822)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 0.10.4-3
- Rebuilt for Python3.5 rebuild
- Add werkzeug sphinx theme as a Source1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Ricky Elrod <relrod@redhat.com> - 0.10.4-1
- Upstream 0.10.4.

* Fri Jul 18 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.6-1
- Upstream 0.9.6
- Fixes RHBZ #1105819

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 26 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.4-1
- Upstream 0.9.4

* Thu Jul 25 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.3-1
- Upstream 0.9.3

* Tue Jul 23 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.2-1
- Upstream 0.9.2 release.

* Sat Jun 15 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.1-1
- upstream 0.9.1
- add python3 flavor

* Fri Jun 14 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9-1
- Upstream 0.9.0 release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb  5 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.3-1
- upstream 0.8.3 (fixes XSS security issues)

* Wed Jan 25 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.2-1
- upstream 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.2-1
- Updating because upstream release of Werkzeug 0.6.2

* Fri Mar 05 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6-1
- Updating because upstream release of Werkzeug 0.6

* Tue Aug 25 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.5.1-1
- Initial package

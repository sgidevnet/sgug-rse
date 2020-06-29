%global srcname zope.testrunner
%global pkgname zope-testrunner

# We have source files with intentional syntax errors, in order to test.
# Do not fail the build just because some file is not valid python.
%undefine _python_bytecompile_errors_terminate_build

Name:           python-%{pkgname}
Version:        5.1
Release:        4%{?dist}
Summary:        Zope testrunner script

License:        ZPLv2.1
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/zopefoundation/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fix a test failure due to whitespace differences
Patch0:         %{name}-whitespace.patch

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(python-subunit)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-programoutput)
BuildRequires:  python3dist(testtools)
BuildRequires:  python3dist(zope.exceptions)
BuildRequires:  python3dist(zope.interface)
BuildRequires:  python3dist(zope.testing)

%description
This package provides a flexible test runner with layer support.

%package     -n python3-%{pkgname}
Summary:        Zope testrunner script

%{?python_provide:%python_provide python3-%{pkgname}}

# This can be removed when Fedora 30 reaches EOL
Obsoletes:      python2-%{pkgname} < 5.0-4
Provides:       python2-%{pkgname} = %{version}-%{release}

%description -n python3-%{pkgname}
This package provides a flexible test runner with layer support.

%prep
%autosetup -n %{srcname}-%{version} -p0

# Update the sphinx HTML theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Fix the way python is invoked
sed -i 's/python -m/python3 -m/' docs/cli.rst

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

# Replace a deprecated directive
sed -i "s/autodoc_default_flags.*/autodoc_default_options = {'members': True, 'show-inheritance': True}/" docs/conf.py

%build
%py3_build

rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

# Not really RST: https://github.com/zopefoundation/zope.testrunner/issues/100
cp -p COPYRIGHT.rst COPYRIGHT

%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
help2man -s 1 -o %{buildroot}%{_mandir}/man1/zope-testrunner.1 \
  -N -n "Zope testrunner script" %{buildroot}%{_bindir}/zope-testrunner

# The Sphinx documentation cannot be built with an uninstalled zope.testrunner
# because python finds the installed zope package, which doesn't contain
# testrunner.  We fake out python by copying the entire installed tree to a
# local directory and adding this package inside the zope directory.
mkdir lib
cp -a %{_prefix}/lib/python%{python3_version} lib
if [ -d %{_prefix}/lib64/python%{python3_version} ]; then
  mkdir lib64
  cp -a %{_prefix}/lib64/python%{python3_version} lib64
fi
mkdir include
cp -a %{_includedir}/python%{python3_version}* include
cp -a %{buildroot}%{python3_sitelib}/zope* \
      lib/python%{python3_version}/site-packages
export PYTHONHOME=$PWD:$PWD
sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html
rm -fr include lib lib64
rm -f docs/_build/html/.buildinfo
unset PYTHONHOME

%check
# The tests don't work with an uninstalled zope.testrunner because python
# finds the installed zope package, which doesn't contain testrunner.  We fake
# out python by copying the entire installed tree to a local directory and
# adding this package inside the zope directory.
mkdir lib
cp -a %{_prefix}/lib/python%{python3_version} lib
if [ -d %{_prefix}/lib64/python%{python3_version} ]; then
  mkdir lib64
  cp -a %{_prefix}/lib64/python%{python3_version} lib64
fi
mkdir include
cp -a %{_includedir}/python%{python3_version}* include
cp -a %{buildroot}%{python3_sitelib}/zope* \
      lib/python%{python3_version}/site-packages
export PYTHONHOME=$PWD:$PWD
%{__python3} setup.py test
rm -fr include lib lib64
unset PYTHONHOME

%files -n python3-%{pkgname}
%doc CHANGES.html README.html docs/_build/html
%license COPYRIGHT LICENSE.md
%{_bindir}/zope-testrunner
%{_mandir}/man1/zope-testrunner.1*
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/zope/testrunner/
%exclude %{python3_sitelib}/zope/testrunner/tests

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1-4
- Rebuilt for Python 3.9

* Sun Mar  1 2020 Jerry James <loganjerry@gmail.com> - 5.1-3
- Add -whitespace patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Jerry James <loganjerry@gmail.com> - 5.1-1
- New upstream version
- Fix cross-reference links in the documentation

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 5.0-4
- Drop the python2 subpackage (bz 1752151)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 4.9.2-1
- New upstream version

* Mon Nov 26 2018 Lumír Balhar <lbalhar@redhat.com> - 4.9-2
- Fix issue with automatic dependencies and executables' names

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 4.9-1
- New upstream version
- Do not ship the tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Jerry James <loganjerry@gmail.com> - 4.8.1-1
- New upstream version

* Sat Nov 11 2017 Jerry James <loganjerry@gmail.com> - 4.8.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Jerry James <loganjerry@gmail.com> - 4.7.0-1
- New upstream version
- subunit is no longer a dependency
- Enable python 3 tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version
- Drop upstreamed test patch

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.5.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 21 2016 Jerry James <loganjerry@gmail.com> - 4.5.1-2
- Fix spurious build failures due to use of _libdir in a noarch package

* Mon Jun 20 2016 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- New upstream version

* Wed Jun  8 2016 Jerry James <loganjerry@gmail.com> - 4.5.0-3
- Do not test with detox; it downloads files at build time

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 4.5.0-2
- Fix directory ownership
- Add man page

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- Initial RPM

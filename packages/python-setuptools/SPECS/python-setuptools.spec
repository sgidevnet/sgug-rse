%global srcname setuptools

#  WARNING  When bootstrapping, disable tests as well,
#           because tests need pip.
%bcond_without bootstrap
%bcond_with tests

%bcond_without python2

%if %{without bootstrap}
%global python_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%if %{with python2}
%global python2_record %{python2_sitelib}/%{srcname}-%{version}.dist-info/RECORD
%endif
%global python3_record %{python3_sitelib}/%{srcname}-%{version}.dist-info/RECORD
%endif
%global python_wheeldir %{_datadir}/python-wheels

Name:           python-setuptools
# When updating, update the bundled libraries versions bellow!
Version:        41.6.0
Release:        2%{?dist}
Summary:        Easily build and distribute Python packages
# setuptools is MIT
# packaging is BSD or ASL 2.0
# pyparsing is MIT
# six is MIT
License:        MIT and (BSD or ASL 2.0)
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{srcname} %{version} zip}

# In Fedora, sudo setup.py install installs to /usr/local/lib/pythonX.Y/site-packages
# But pythonX doesn't own that dir, that would be against FHS
# We need to create it if it doesn't exist
# https://bugzilla.redhat.com/show_bug.cgi?id=1576924
Patch0:         create-site-packages.patch

BuildArch:      noarch

BuildRequires:  gcc
%if %{with python2}
BuildRequires:  python2-devel
%if %{without bootstrap}
BuildRequires:  python2-pip
BuildRequires:  python2-wheel
%endif # without bootstrap
%if %{with tests}
BuildRequires:  python2-futures
BuildRequires:  python2-pip
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
%endif # with tests
%endif # with python2

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-pytest-fixture-config
BuildRequires:  python3-pytest-virtualenv
%endif # with tests
%if %{without bootstrap}
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
BuildRequires:  python3-rpm-generators
%endif # without bootstrap

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

# Virtual provides for the packages bundled by setuptools.
# You can find the versions in setuptools/setuptools/_vendor/vendored.txt
%global bundled() %{expand:
Provides: bundled(python%{1}dist(packaging)) = 16.8
Provides: bundled(python%{1}dist(pyparsing)) = 2.2.1
Provides: bundled(python%{1}dist(six)) = 1.10.0
}

%if %{with python2}
%package -n python2-setuptools
Summary:        Easily build and distribute Python packages
%{?python_provide:%python_provide python2-setuptools}
%{bundled 2}

%description -n python2-setuptools
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

%endif # with python2


%package -n python3-setuptools
Summary:        Easily build and distribute Python 3 packages
Conflicts:      python-setuptools < %{version}-%{release}
%{?python_provide:%python_provide python3-setuptools}
%{bundled 3}

%description -n python3-setuptools
Setuptools is a collection of enhancements to the Python 3 distutils that allow
you to more easily build and distribute Python 3 packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

%if %{without bootstrap}
%package wheel
Summary:        The setuptools wheel
%{bundled 2}
%{bundled 3}

%description wheel
A Python wheel of setuptools to use with venv.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -r %{srcname}.egg-info

# Strip shbang
find setuptools pkg_resources -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# These tests require internet connection
rm setuptools/tests/test_integration.py 
# Spurious executable perm https://github.com/pypa/setuptools/pull/1441
chmod -x README.rst

%build
# Warning, different bootstrap meaning here, has nothing to do with our bcond
# This bootstraps .egg-info directory needed to build setuptools
%{__python3} bootstrap.py

%if %{without bootstrap}
%py3_build_wheel
%else
%if %{with python2}
%py2_build
%endif # with python2

%py3_build
%endif


%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want /usr/bin/pip to be
# the python3 version).
%if %{with python2}
%if %{without bootstrap}
%py2_install_wheel %{python_wheelname}

# Remove /usr/bin/easy_install from the record as later on we delete the file
sed -i '/\/usr\/bin\/easy_install,/d' %{buildroot}%{python2_record}
%else
%py2_install
%endif

# TODO: we have to remove this by hand now, but it'd be nice if we wouldn't have to
# (pip install wheel doesn't overwrite)
rm %{buildroot}%{_bindir}/easy_install

rm -rf %{buildroot}%{python2_sitelib}/setuptools/tests
%if %{without bootstrap}
sed -i '/^setuptools\/tests\//d' %{buildroot}%{python2_record}
%endif

find %{buildroot}%{python2_sitelib} -name '*.exe' | xargs rm -f
%endif # with python2


%if %{without bootstrap}
%py3_install_wheel %{python_wheelname}
%else
%py3_install
%endif

rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests
%if %{without bootstrap}
sed -i '/^setuptools\/tests\//d' %{buildroot}%{python3_record}
%endif

find %{buildroot}%{python3_sitelib} -name '*.exe' | xargs rm -f

# Don't ship these
rm -r docs/{Makefile,conf.py,_*}

%if %{without bootstrap}
mkdir -p %{buildroot}%{python_wheeldir}
install -p dist/%{python_wheelname} -t %{buildroot}%{python_wheeldir}
%endif


%if %{with tests}
%check
%if %{with python2}
# see https://github.com/pypa/setuptools/issues/1170 for PYTHONDONTWRITEBYTECODE
# several tests are xfailed with POSIX locale, so we set C.utf-8 (not needed on py3)
# test_virtualenv is ignored to break dependency on python2-pytest-virtualenv
LANG=C.utf-8 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$(pwd) pytest-%{python2_version} \
    --ignore setuptools/tests/test_virtualenv.py \
    --deselect=setuptools/tests/test_setuptools.py::TestDepends::testRequire
%endif # with python2

# --ignore=pavement.py: No python3-paver in Fedora (the test is only collected on py3)
#   pavement.py is only used by upstream to do releases and vendoring, we don't ship it
# --deselect=setuptools/tests/test_setuptools.py::TestDepends::testRequire
#   Test failure reported upstream: https://github.com/pypa/setuptools/issues/1896
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$(pwd) pytest-%{python3_version} \
    --ignore=pavement.py \
    --deselect=setuptools/tests/test_setuptools.py::TestDepends::testRequire
%endif # with tests


%if %{with python2}
%files -n python2-setuptools
%license LICENSE
%doc docs/* CHANGES.rst README.rst
%{python2_sitelib}/*
%{_bindir}/easy_install-2.*
%endif # with python2

%files -n python3-setuptools
%license LICENSE
%doc docs/* CHANGES.rst README.rst
%{python3_sitelib}/easy_install.py
%{python3_sitelib}/pkg_resources/
%{python3_sitelib}/setuptools*/
%{python3_sitelib}/__pycache__/*
%{_bindir}/easy_install
%{_bindir}/easy_install-3.*

%if %{without bootstrap}
%files wheel
%license LICENSE
# we own the dir for simplicity
%dir %{python_wheeldir}/
%{python_wheeldir}/%{python_wheelname}
%endif


%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 41.6.0-2
- Support building with python2 too

* Mon Nov 04 2019 Tomas Orsava <torsava@redhat.com> - 41.6.0-1
- Upgrade to 41.6.0 (#1758945).
- https://setuptools.readthedocs.io/en/latest/history.html#v41-6-0
- Disabled a failing upstream test: https://github.com/pypa/setuptools/issues/1896

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 41.2.0-1
- Upgrade to 41.2.0 (#1742718).
- https://setuptools.readthedocs.io/en/latest/history.html#v41-2-0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 41.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Miro Hrončok <mhroncok@redhat.com> - 41.0.1-3
- Make /usr/bin/easy_install Python 3
- Drop obsoleted Obsoletes

* Fri Jun 21 2019 Petr Viktorin <pviktori@redhat.com> - 41.0.1-2
- Remove optional test dependencies for Python 2
- Skip test_virtualenv on Python 2

* Thu Apr 25 2019 Miro Hrončok <mhroncok@redhat.com> - 41.0.1-1
- Update to 41.0.1 (#1695846)
- https://github.com/pypa/setuptools/blob/v41.0.1/CHANGES.rst

* Tue Feb 05 2019 Miro Hrončok <mhroncok@redhat.com> - 40.8.0-1
- Update to 40.8.0 (#1672756)
- https://github.com/pypa/setuptools/blob/v40.8.0/CHANGES.rst

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 40.7.3-1
- Hotfix update to 40.7.3 (#1672084)
- https://github.com/pypa/setuptools/blob/v40.7.3/CHANGES.rst

* Sat Feb 02 2019 Miro Hrončok <mhroncok@redhat.com> - 40.7.2-1
- Hotfix update to 40.7.2 (#1671608)
- https://github.com/pypa/setuptools/blob/v40.7.2/CHANGES.rst

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Miro Hrončok <mhroncok@redhat.com> - 40.7.1-1
- Hotfix update to 40.7.1 (#1670243)
- https://github.com/pypa/setuptools/blob/v40.7.1/CHANGES.rst

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 40.7.0-1
- Update to 40.7.0 (#1669876)
- https://github.com/pypa/setuptools/blob/v40.7.0/CHANGES.rst

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 40.4.3-1
- Update to 40.4.3 to fix dire DeprecationWarnings (#1627071)
- List vendored libraries
- https://github.com/pypa/setuptools/blob/v40.4.3/CHANGES.rst

* Wed Sep 19 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 40.4.1-1
- Update to 40.4.1 (#1599307).
- https://github.com/pypa/setuptools/blob/v40.4.1/CHANGES.rst

* Wed Aug 15 2018 Petr Viktorin <pviktori@redhat.com> - 39.2.0-7
- Add a subpackage with wheels
- Remove the python3 bcond
- Remove macros for RHEL 6

* Thu Jul 19 2018 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-6
- Create /usr/local/lib/pythonX.Y when needed (#1576924)

%global srcname setuptools

#  WARNING  When bootstrapping, disable tests as well,
#           because tests need pip.
%bcond_without bootstrap
%bcond_with tests

%bcond_with python2

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
Release:        1%{?dist}
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

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 39.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-4
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-3
- Bootstrap for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-2
- Bootstrap for Python 3.7

* Wed May 23 2018 Charalampos Stratakis <cstratak@redhat.com> - 39.2.0-1
- update to 39.2.0 Fixes bug #1572889

* Tue Mar 20 2018 Charalampos Stratakis <cstratak@redhat.com> - 39.0.1-1
- update to 39.0.1 Fixes bug #1531527

* Wed Mar 14 2018 Tomas Orsava <torsava@redhat.com> - 38.4.0-4
- Skip test_virtualenv due to broken executable detection

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 38.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 38.4.0-2
- Update conditional

* Tue Jan 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 38.4.0-1
- update to 38.4.0 Fixes bug #1531527

* Tue Jan 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 38.2.5-1
- update to 38.2.5 Fixes bug #1528968

* Tue Nov 21 2017 Miro Hrončok <mhroncok@redhat.com> - 37.0.0-1
- Update to 37.0.0 (fixes #1474126)
- Removed not needed pip3 patch (upstream included different version of fix)

* Tue Nov 21 2017 Miro Hrončok <mhroncok@redhat.com> - 36.5.0-1
- Update to 36.5.0 (related to #1474126)

* Thu Nov 09 2017 Tomas Orsava <torsava@redhat.com> - 36.2.0-8
- Remove the platform-python subpackage

* Sun Aug 20 2017 Tomas Orsava <torsava@redhat.com> - 36.2.0-7
- Re-enable tests to finish bootstrapping the platform-python stack
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Wed Aug 09 2017 Tomas Orsava <torsava@redhat.com> - 36.2.0-6
- Add the platform-python subpackage
- Disable tests so platform-python stack can be bootstrapped
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Wed Aug 09 2017 Tomas Orsava <torsava@redhat.com> - 36.2.0-5
- Add Patch 0 that fixes a test suite failure on Python 3 in absence of
  the Python 2 version of pip
- Move docs to their proper place

* Wed Aug 09 2017 Tomas Orsava <torsava@redhat.com> - 36.2.0-4
- Switch macros to bcond's and make Python 2 optional to facilitate building
  the Python 2 and Python 3 modules.

* Tue Aug 08 2017 Michal Cyprian <mcyprian@redhat.com> - 36.2.0-3
- Revert "Add --executable option to easy_install command"
  This enhancement is currently not needed and it can possibly
  collide with `pip --editable`option

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 36.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 36.2.0-1
- update to 36.2.0. Fixes bug #1470908

* Thu Jun 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 36.0.1-1
- update to 36.0.1. Fixes bug #1458093

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 35.0.2-1
- update to 35.0.2. Fixes bug #1446622

* Sun Apr 23 2017 Kevin Fenzi <kevin@scrye.com> - 35.0.1-1
- Update to 35.0.1. Fixes bug #1440388

* Sat Mar 25 2017 Kevin Fenzi <kevin@scrye.com> - 34.3.2-1
- Update to 34.3.2. Fixes bug #1428818

* Sat Feb 25 2017 Kevin Fenzi <kevin@scrye.com> - 34.3.0-1
- Update to 34.3.0. Fixes bug #1426463

* Fri Feb 17 2017 Michal Cyprian <mcyprian@redhat.com> - 34.2.0-2
- Add --executable option to easy_install command

* Thu Feb 16 2017 Charalampos Stratakis <cstratak@redhat.com> - 34.2.0-1
- Update to 34.2.0. Fixes bug #1421676

* Sat Feb 04 2017 Kevin Fenzi <kevin@scrye.com> - 34.1.1-1
- Update to 34.1.1. Fixes bug #1412268
- Fix License tag. Fixes bug #1412268
- Add Requires for fomerly bundled projects: six, packaging appdirs

* Tue Jan 03 2017 Michal Cyprian <mcyprian@redhat.com> - 32.3.1-2
- Use python macros in build and install sections

* Thu Dec 29 2016 Kevin Fenzi <kevin@scrye.com> - 32.3.1-1
- Update to 32.3.1. Fixes bug #1409091

* Wed Dec 28 2016 Kevin Fenzi <kevin@scrye.com> - 32.3.0-1
- Update to 32.3.0. Fixes bug #1408564

* Fri Dec 23 2016 Kevin Fenzi <kevin@scrye.com> - 32.2.0-1
- Update to 32.2.0. Fixes bug #1400310

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 30.4.0-2
- Enable tests

* Sun Dec 11 2016 Kevin Fenzi <kevin@scrye.com> - 30.4.0-1
- Update to 30.4.0. Fixes bug #1400310

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 28.8.0-3
- Rebuild for Python 3.6 with wheel
- Disable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 28.8.0-2
- Rebuild for Python 3.6 without wheel

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 28.8.0-1
- Update to 28.8.1. Fixes bug #1392722

* Mon Oct 31 2016 Kevin Fenzi <kevin@scrye.com> - 28.7.1-1
- Update to 28.7.1. Fixes bug #1389917

* Tue Oct 25 2016 Kevin Fenzi <kevin@scrye.com> - 28.6.1-1
- Update to 28.6.1. Fixes bug #1387071

* Tue Oct 18 2016 Kevin Fenzi <kevin@scrye.com> - 28.6.0-1
- Update to 28.6.0. Fixes bug #1385655

* Sat Oct 08 2016 Kevin Fenzi <kevin@scrye.com> - 28.3.0-1
- Update to 28.3.0. Fixes bug #1382971

* Sun Oct 02 2016 Kevin Fenzi <kevin@scrye.com> - 28.2.0-1
- Update to 28.2.0. Fixes bug #1381099

* Sun Oct 02 2016 Kevin Fenzi <kevin@scrye.com> - 28.1.0-1
- Update to 28.1.0. Fixes bug #1381066

* Wed Sep 28 2016 Kevin Fenzi <kevin@scrye.com> - 28.0.0-1
- Update to 28.0.0. Fixes bug #1380073

* Sun Sep 25 2016 Kevin Fenzi <kevin@scrye.com> - 27.3.0-1
- Update to 27.3.0. Fixes bug #1378067

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 27.2.0-1
- Update to 27.2.0. Fixes bug #1376298

* Sat Sep 10 2016 Kevin Fenzi <kevin@scrye.com> - 27.1.2-1
- Update to 27.1.2. Fixes bug #1370777

* Sat Aug 27 2016 Kevin Fenzi <kevin@scrye.com> - 26.0.0-1
- Update to 26.0.0. Fixes bug #1370777

* Wed Aug 10 2016 Kevin Fenzi <kevin@scrye.com> - 25.1.6-1
- Update to 25.1.6. Fixes bug #1362325

* Fri Jul 29 2016 Kevin Fenzi <kevin@scrye.com> - 25.1.1-1
- Update to 25.1.1. Fixes bug #1361465

* Thu Jul 28 2016 Kevin Fenzi <kevin@scrye.com> - 25.1.0-1
- Update to 25.1.0

* Sat Jul 23 2016 Kevin Fenzi <kevin@scrye.com> - 25.0.0-1
- Update to 25.0.0

* Fri Jul 22 2016 Kevin Fenzi <kevin@scrye.com> - 24.2.0-1
- Update to 24.2.0. Fixes bug #1352734

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Kevin Fenzi <kevin@scrye.com> - 24.0.1-1
- Update to 24.0.1. Fixes bug #1352532

* Wed Jun 15 2016 Kevin Fenzi <kevin@scrye.com> - 23.0.0-1
- Update to 23.0.0. Fixes bug #1346542

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 22.0.5-1
- Update to 22.0.5. Fixes bug #1342706

* Thu Jun 02 2016 Kevin Fenzi <kevin@scrye.com> - 20.0.0-1
- Upgrade to 22.0.0

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sun May 29 2016 Kevin Fenzi <kevin@scrye.com> - 21.2.2-1
- Update to 21.2.2. Fixes bug #1332357

* Thu Apr 28 2016 Kevin Fenzi <kevin@scrye.com> - 20.10.1-1
- Update to 20.10.1. Fixes bug #1330375

* Sat Apr 16 2016 Kevin Fenzi <kevin@scrye.com> - 20.9.0-1
- Update to 20.9.0. Fixes bug #1327827

* Fri Apr 15 2016 Kevin Fenzi <kevin@scrye.com> - 20.8.1-1
- Update to 20.8.1. Fixes bug #1325910

* Thu Mar 31 2016 Kevin Fenzi <kevin@scrye.com> - 20.6.7-1
- Update to 20.6.7. Fixes bug #1322836

* Wed Mar 30 2016 Kevin Fenzi <kevin@scrye.com> - 20.4-1
- Update to 20.4. Fixes bug #1319366

* Wed Mar 16 2016 Kevin Fenzi <kevin@scrye.com> - 20.3-1
- Update to 20.3. Fixes bug #1311967

* Sat Feb 27 2016 Kevin Fenzi <kevin@scrye.com> - 20.2.2-1
- Update to 20.2.2. Fixes bug #1311967

* Sat Feb 13 2016 Kevin Fenzi <kevin@scrye.com> - 20.1.1-1
- Update to 20.1.1. Fixes bug #130719

* Fri Feb 12 2016 Kevin Fenzi <kevin@scrye.com> - 20.1-1
- Update to 20.1. Fixes bug #1307000

* Mon Feb 08 2016 Kevin Fenzi <kevin@scrye.com> - 20.0-1
- Update to 20.0. Fixes bug #1305394

* Sat Feb 06 2016 Kevin Fenzi <kevin@scrye.com> - 19.7-1
- Update to 19.7. Fixes bug #1304563

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 19.6.2-2
- Fix python3 package file ownership

* Sun Jan 31 2016 Kevin Fenzi <kevin@scrye.com> - 19.6.2-1
- Update to 19.6.2. Fixes bug #1303397

* Mon Jan 25 2016 Kevin Fenzi <kevin@scrye.com> - 19.6-1
- Update to 19.6.

* Mon Jan 25 2016 Kevin Fenzi <kevin@scrye.com> - 19.5-1
- Update to 19.5. Fixes bug #1301313

* Mon Jan 18 2016 Kevin Fenzi <kevin@scrye.com> - 19.4-1
- Update to 19.4. Fixes bug #1299288

* Tue Jan 12 2016 Orion Poplawski <orion@cora.nwra.com> - 19.2-2
- Cleanup spec from python3-setuptools review

* Fri Jan 08 2016 Kevin Fenzi <kevin@scrye.com> - 19.2-1
- Update to 19.2. Fixes bug #1296755

* Fri Dec 18 2015 Kevin Fenzi <kevin@scrye.com> - 19.1.1-1
- Update to 19.1.1. Fixes bug #1292658

* Tue Dec 15 2015 Kevin Fenzi <kevin@scrye.com> - 18.8.1-1
- Update to 18.8.1. Fixes bug #1291678

* Sat Dec 12 2015 Kevin Fenzi <kevin@scrye.com> - 18.8-1
- Update to 18.8. Fixes bug #1290942

* Fri Dec 04 2015 Kevin Fenzi <kevin@scrye.com> - 18.7.1-1
- Update to 18.7.1. Fixes bug #1287372

* Wed Nov 25 2015 Kevin Fenzi <kevin@scrye.com> - 18.6.1-1
- Update to 18.6.1. Fixes bug #1270578

* Sun Nov 15 2015 Thomas Spura <tomspur@fedoraproject.org> - 18.5-3
- Try to disable zip_safe bug #1271776
- Add python2 subpackage

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 18.5-2
- Add patch so it is possible to set test_args variable

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 18.5-1
- Update to 18.5. Fixes bug #1270578

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.coM> - 18.4-1
- Update to 18.4. Fixes bug #1270578
- Build with wheel and check phase

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 18.3.2-2
- Python3.5 rebuild: rebuild without wheel and check phase

* Tue Sep 22 2015 Kevin Fenzi <kevin@scrye.com> 18.3.2-1
- Update to 18.3.2. Fixes bug #1264902

* Mon Sep 07 2015 Kevin Fenzi <kevin@scrye.com> 18.3.1-1
- Update to 18.3.1. Fixes bug #1256188

* Wed Aug 05 2015 Kevin Fenzi <kevin@scrye.com> 18.1-1
- Update to 18.1. Fixes bug #1249436

* Mon Jun 29 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 18.0.1-2
- Explicitely provide python2-setuptools

* Thu Jun 25 2015 Kevin Fenzi <kevin@scrye.com> 18.0.1-1
- Update to 18.0.1

* Sat Jun 20 2015 Kevin Fenzi <kevin@scrye.com> 17.1.1-3
- Drop no longer needed Requires/BuildRequires on python-backports-ssl_match_hostname
- Fixes bug #1231325

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Kevin Fenzi <kevin@scrye.com> 17.1.1-1
- Update to 17.1.1. Fixes bug 1229507

* Sun Jun 07 2015 Kevin Fenzi <kevin@scrye.com> 17.1-1
- Update to 17.1. Fixes bug 1229066

* Sat May 30 2015 Kevin Fenzi <kevin@scrye.com> 17.0-1
- Update to 17

* Mon May 18 2015 Kevin Fenzi <kevin@scrye.com> 16.0-1
- Update to 16

* Mon Apr 27 2015 Ralph Bean <rbean@redhat.com> - 15.2-1
- new version

* Sat Apr 04 2015 Ralph Bean <rbean@redhat.com> - 15.0-1
- new version

* Sun Mar 22 2015 Ralph Bean <rbean@redhat.com> - 14.3.1-1
- new version

* Sat Mar 21 2015 Ralph Bean <rbean@redhat.com> - 14.3.1-1
- new version

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 14.3-1
- new version

* Sun Mar 15 2015 Ralph Bean <rbean@redhat.com> - 14.2-1
- new version

* Sun Mar 15 2015 Ralph Bean <rbean@redhat.com> - 14.1.1-1
- new version

* Fri Mar 06 2015 Ralph Bean <rbean@redhat.com> - 13.0.2-1
- new version

* Thu Mar 05 2015 Ralph Bean <rbean@redhat.com> - 12.4-1
- new version

* Fri Feb 27 2015 Ralph Bean <rbean@redhat.com> - 12.3-1
- new version

* Tue Jan 20 2015 Kevin Fenzi <kevin@scrye.com> 12.0.3-1
- Update to 12.0.3

* Fri Jan 09 2015 Slavek Kabrda <bkabrda@redhat.com> - 11.3.1-2
- Huge spec cleanup
- Make spec buildable on all Fedoras and RHEL 6 and 7
- Make tests actually run

* Wed Jan 07 2015 Kevin Fenzi <kevin@scrye.com> 11.3.1-1
- Update to 11.3.1. Fixes bugs: #1179393 and #1178817

* Sun Jan 04 2015 Kevin Fenzi <kevin@scrye.com> 11.0-1
- Update to 11.0. Fixes bug #1178421

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 8.2.1-1
- Update to 8.2.1. Fixes bug #1175229

* Thu Oct 23 2014 Ralph Bean <rbean@redhat.com> - 7.0-1
- Latest upstream.  Fixes bug #1154590.

* Mon Oct 13 2014 Ralph Bean <rbean@redhat.com> - 6.1-1
- Latest upstream.  Fixes bug #1152130.

* Sat Oct 11 2014 Ralph Bean <rbean@redhat.com> - 6.0.2-2
- Modernized python2 macros.
- Inlined locale environment variables in the %%check section.
- Remove bundled egg-info and .exes.

* Fri Oct 03 2014 Kevin Fenzi <kevin@scrye.com> 6.0.2-1
- Update to 6.0.2

* Sat Sep 27 2014 Kevin Fenzi <kevin@scrye.com> 6.0.1-1
- Update to 6.0.1. Fixes bug #1044444

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-8
- Remove the python-setuptools-devel Virtual Provides as per this Fedora 21
  Change: http://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-7
- And another bug in sdist

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-6
- Fix a bug in the sdist command

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.0-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Tomas Radej <tradej@redhat.com> - 2.0-3
- Rebuilt for tag f21-python

* Wed Apr 23 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.0-2
- Add a switch to build setuptools as wheel

* Mon Dec  9 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0-1
- Update to new upstream release with a few things removed from the API:
  Changelog: https://pypi.python.org/pypi/setuptools#id139

* Mon Nov 18 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4-1
- Update to 1.4 that gives easy_install pypi credential handling

* Thu Nov  7 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-1
- Minor upstream update to reign in overzealous warnings

* Mon Nov  4 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3-1
- Upstream update that pulls in our security patches

* Mon Oct 28 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.7-1
- Update to newer upstream release that has our patch to the unittests
- Fix for http://bugs.python.org/issue17997#msg194950 which affects us since
  setuptools copies that code. Changed to use
  python-backports-ssl_match_hostname so that future issues can be fixed in
  that package.

* Sat Oct 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.6-1
- Update to newer upstream release.  Some minor incompatibilities listed but
  they should affect few, if any consumers.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.6-1
- Upstream update -- just fixes python-2.4 compat

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5
  - package_index can handle hashes other than md5
  - Fix security vulnerability in SSL certificate validation
  - https://bugzilla.redhat.com/show_bug.cgi?id=963260

* Fri Jul  5 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8-1
- Update to upstream 0.8  release.  Codebase now runs on anything from
  python-2.4 to python-3.3 without having to be translated by 2to3.

* Wed Jul  3 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7 upstream release

* Mon Jun 10 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.2-2
- Update to the setuptools-0.7 branch that merges distribute and setuptools

* Thu Apr 11 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.36-1
- Update to upstream 0.6.36.  Many bugfixes

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 0.6.28-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.6.28-2
- remove rhel logic from with_python3 conditional

* Mon Jul 23 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.28-1
- New upstream release:
  - python-3.3 fixes
  - honor umask when setuptools is used to install other modules

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.27-2
- Fix easy_install.py having a python3 shebang in the python2 package

* Thu Jun  7 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.27-1
- Upstream bugfix

* Tue May 15 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.24-2
- Upstream bugfix

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.24-1
- Upstream bugfix
- Compile the win32 launcher binary using mingw

* Sun Aug 21 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.21-1
- Upstream bugfix release

* Thu Jul 14 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.19-1
- Upstream bugfix release

* Tue Feb 22 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.14-7
- Switch to patch that I got in to upstream

* Tue Feb 22 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.14-6
- Fix build on python-3.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6.14-4
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Tue Aug 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.14-3
- Update description to mention this is distribute

* Thu Jul 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6.14-2
- bump for building against python 2.7

* Thu Jul 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.6.14-1
- update to new version
- all patches are upsteam

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.13-7
- generalize path of easy_install-2.6 and -3.1 to -2.* and -3.*

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.13-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 3 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.13-5
- Upstream patch for compatibility problem with setuptools
- Minor spec cleanups
- Provide python-distribute for those who see an import distribute and need
  to get the proper package.

* Thu Jun 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.13-4
- Fix race condition in unittests under the python-2.6.x on F-14.

* Thu Jun 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.13-3
- Fix few more buildroot macros

* Thu Jun 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.13-2
- Include data that's needed for running tests

* Thu Jun 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.13-1
- Update to upstream 0.6.13
- Minor specfile formatting fixes

* Thu Feb 04 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.10-3
- First build with python3 support enabled.
  
* Fri Jan 29 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.10-2
- Really disable the python3 portion

* Fri Jan 29 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.10-1
- Update the python3 portions but disable for now.
- Update to 0.6.10
- Remove %%pre scriptlet as the file has a different name than the old
  package's directory

* Tue Jan 26 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.9-4
- Fix install to make /usr/bin/easy_install the py2 version
- Don't need python3-tools since the library is now in the python3 package
- Few other changes to cleanup style

* Fri Jan 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.9-2
- add python3 subpackage

* Mon Dec 14 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.9-1
- New upstream bugfix release.

* Sun Dec 13 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.8-2
- Test rebuild

* Mon Nov 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8.
- Fix directory => file transition when updating from setuptools-0.6c9.

* Tue Nov 3 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.7-2
- Fix duplicate inclusion of files.
- Only Obsolete old versions of python-setuptools-devel

* Tue Nov 3 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.7-1
- Move easy_install back into the main package as the needed files have been
  moved from python-devel to the main python package.
- Update to 0.6.7 bugfix.

* Fri Oct 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.6-1
- Upstream bugfix release.

* Mon Oct 12 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.4-1
- First build from the distribute codebase -- distribute-0.6.4.
- Remove svn patch as upstream has chosen to go with an easier change for now.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6c9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.6c9-4
- Apply SVN-1.6 versioning patch (rhbz #511021)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6c9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

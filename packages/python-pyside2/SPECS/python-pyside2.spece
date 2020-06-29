%global pypi_name pyside2
%global camel_name PySide2
%global qt5ver 5.14

# Clang doesn't handle some gcc specific flags.
%global _optflags %optflags
%global optflags %(echo %optflags | sed 's| -fstack-clash-protection||')
%global optflags %(echo %optflags | sed 's| -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1||')
%global optflags %(echo %optflags | sed 's| -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1||')
%global _hardening_ldflags %(echo %_hardening_ldflags | sed 's| -specs=/usr/lib/rpm/redhat/redhat-hardened-ld||')


Name:           python-%{pypi_name}
Epoch:          1
Version:        5.15.0
Release:        1%{?dist}
Summary:        Python bindings for the Qt 5 cross-platform application and UI framework

License:        BSD and GPLv2 and GPLv3 and LGPLv3
URL:            https://wiki.qt.io/Qt_for_Python

Source0:        https://download.qt.io/official_releases/QtForPython/%{pypi_name}/%{camel_name}-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz

# PySide2 tools are "reinstalled" for pip installs but breaks distro builds.
Patch0:         pyside2-tools-obsolete.patch
# Don't abort the build on Python 3.8/3.9
Patch1:         python_ver_classifier.patch

%if 0%{?rhel} == 7
BuildRequires:  cmake3
BuildRequires:  llvm-toolset-7-clang-devel llvm-toolset-7-llvm-devel
%else
BuildRequires:  cmake
%endif
BuildRequires:  gcc graphviz
BuildRequires:  clang-devel llvm-devel
BuildRequires:  /usr/bin/pathfix.py
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
# Shiboken2
BuildRequires:  cmake(Qt5Core) >= %{qt5ver}
BuildRequires:  cmake(Qt5Gui) >= %{qt5ver}
BuildRequires:  cmake(Qt5Xml) >= %{qt5ver}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5ver}
BuildRequires:  cmake(Qt5WebKit) >= %{qt5ver}
# Needed for Cmake UI Config
BuildRequires:  cmake(Qt5UiTools) >= %{qt5ver}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5ver}
# PySide2
BuildRequires:  qt5-qtbase-private-devel >= %{qt5ver}
BuildRequires:  cmake(Qt5Charts) >= %{qt5ver}
BuildRequires:  cmake(Qt5DataVisualization) >= %{qt5ver}
BuildRequires:  cmake(Qt5Multimedia) >= %{qt5ver}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5ver}
BuildRequires:  cmake(Qt5RemoteObjects) >= %{qt5ver}
BuildRequires:  cmake(Qt5Script) >= %{qt5ver}
BuildRequires:  cmake(Qt5Scxml) >= %{qt5ver}
BuildRequires:  cmake(Qt5Sensors) >= %{qt5ver}
BuildRequires:  cmake(Qt5SerialPort) >= %{qt5ver}
BuildRequires:  cmake(Qt5Svg) >= %{qt5ver}
BuildRequires:  cmake(Qt5TextToSpeech) >= %{qt5ver}
BuildRequires:  cmake(Qt5XmlPatterns) >= %{qt5ver}
%ifnarch ppc64le s390x
BuildRequires:  cmake(Qt5WebEngine) >= %{qt5ver}
%endif
BuildRequires:  cmake(Qt5WebSockets) >= %{qt5ver}
BuildRequires:  cmake(Qt53DCore) >= %{qt5ver}
BuildRequires:  cmake(Qt5Designer) >= %{qt5ver}
BuildRequires:  cmake(Qt5Help) >= %{qt5ver}
BuildRequires:  cmake(Qt5UiPlugin) >= %{qt5ver}


%description
PySide2 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 5.13+ framework.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n     python3-%{pypi_name}
Provides:       python3-%{camel_name} = %{version}-%{release}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%{?python_provide:%python_provide python3-%{camel_name}}

%description -n python3-%{pypi_name}
PySide2 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 5.13+ framework.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.


%package -n     python3-%{pypi_name}-devel
Requires:       pyside2-tools
Requires:       shiboken2
Summary:        Development files related to %{name}
%{?python_provide:%python_provide python3-%{pypi_name}-devel}
%{?python_provide:%python_provide python3-%{camel_name}-devel}

%description -n python3-%{pypi_name}-devel
%{summary}.


%package -n pyside2-tools
Summary:        PySide2 tools for the Qt 5 framework

%description -n pyside2-tools
PySide2 provides Python bindings for the Qt5 cross-platform application
and UI framework.

This package ships the following accompanying tools:
 * pyside2-rcc - PySide2 resource compiler
 * pyside2-uic - Python User Interface Compiler for PySide2
 * pyside2-lupdate - update Qt Linguist translation files for PySide2

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.


%package -n shiboken2
Summary:        Python / C++ bindings generator for %camel_name

%description -n shiboken2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python3-shiboken2
Summary:        Python / C++ bindings libraries for %camel_name

%description -n python3-shiboken2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python3-shiboken2-devel
Summary:        Python / C++ bindings helper module for %camel_name
Requires:       shiboken2
Requires:       python3-shiboken2

%description -n python3-shiboken2-devel
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.


%prep
%autosetup -p1 -n pyside-setup-opensource-src-%{version}


%build

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
. /opt/rh/llvm-toolset-7/enable
%else
export CXX=/usr/bin/clang++
%endif
mkdir %{_target} && cd %{_target}
%if 0%{?rhel} == 7
%cmake3 -DUSE_PYTHON_VERSION=3 ../
%else
%cmake -DUSE_PYTHON_VERSION=3 ../
%endif
%make_build

%install
cd %{_target}
%make_install
cd -

# Generate egg-info manually and install since we're performing a cmake build.
%{__python3} setup.py egg_info
for name in PySide2 shiboken2 shiboken2_generator; do
  mkdir -p %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info
  cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
        %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
done

# Fix all Python shebangs recursively
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
# Need to list files that do not match ^[a-zA-Z0-9_]+\.py$ explicitly!
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/*


%check
# Lots of tests fail currently
#{__python3} testrunner.py test


%files -n python3-%{pypi_name}
%license LICENSE.LGPLv3
%doc README.md
%doc CHANGES.rst
%{_libdir}/libpyside2*.so.5.15*
%{python3_sitearch}/%{camel_name}/
%{python3_sitearch}/%{camel_name}-%{version}-py%{python3_version}.egg-info/

%files -n python3-%{pypi_name}-devel
%{_datadir}/PySide2/
%{_includedir}/PySide2/
%{_libdir}/libpyside2*.so
%{_libdir}/cmake/PySide2*
%{_libdir}/pkgconfig/pyside2.pc

%files -n pyside2-tools
%doc README.pyside*
%license LICENSE.GPL2
%{_bindir}/pyside*
%{_mandir}/man1/pyside*.1*

%files -n shiboken2
%doc README.shiboken2-generator.md
%license LICENSE.GPLv3
%{_bindir}/shiboken2
%{_bindir}/shiboken_tool.py

%files -n python3-shiboken2
%doc README.shiboken2.md
%license LICENSE.LGPLv3
%{_libdir}/libshiboken2*.so.5.15*
%{python3_sitearch}/shiboken2/
%{python3_sitearch}/shiboken2-%{version}-py%{python3_version}.egg-info/

%files -n python3-shiboken2-devel
%doc README.shiboken2.md
%{_includedir}/shiboken2/
%{_libdir}/cmake/Shiboken2-%{version}/
%{_libdir}/libshiboken2*.so
%{_libdir}/pkgconfig/shiboken2.pc
%{python3_sitearch}/shiboken2_generator/
%{python3_sitearch}/shiboken2_generator-%{version}-py%{python3_version}.egg-info/


%changelog
* Thu Jun 18 2020 Marie Loise Nolden <loise@kde.org> - 1:5.15.0-1
- Update to 5.15.0.
- Convert Qt BRs to cmake(Qt5...) variant.
- Include new supported Qt5 modules.

* Wed May 27 2020 Richard Shaw <hobbes1069@gmail.com> - 1:5.14.2.2-1
- Update to 5.14.2.2.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:5.14.2.1-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Richard Shaw <hobbes1069@gmail.com> - 1:5.14.2.1-1
- Update to 5.14.2.1.

* Fri Apr 10 2020 Richard Shaw <hobbes1069@gmail.com> - 1:5.14.2-1
- Update to 5.14.2.

* Thu Apr  09 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 1:5.13.2-3
- Fix ignored --debug-level issue

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Richard Shaw <hobbes1069@gmail.com> - 1:5.13.2-1
- Update to 5.13.2.

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.12.6-2
- rebuild (qt5)

* Fri Nov 22 2019 Richard Shaw <hobbes1069@gmail.com> - 1:5.12.6-1
- Update to 5.12.6.

* Wed Oct 09 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.12.5-1.1
- branch rebuild (qt5)

* Mon Sep 30 2019 Richard Shaw <hobbes1069@gmail.com> - 1:5.12.5-1
- Downgrade to 5.12.5 as the MAJOR & MINOR versions must match Qt.

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.1-2
- rebuild (qt5)

* Mon Sep 09 2019 Richard Shaw <hobbes1069@gmail.com> - 5.13.1-1
- Update to 5.13.1.

* Thu Aug 15 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.4-1
- Update to 5.12.4.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.3-1
- Update to 5.12.3.

* Tue Jun 04 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.1-4
- Change python3-shiboken-libs to python3-shiboken.

* Tue Apr 23 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.1-3
- Update per review comments.
- Make library globs dependent  on soname.
- Add explicit requires for skiboken2 on shiboken2-devel.
- Try to workaround qt5-qtwebengine not being available on ppc64le and s390x.

* Thu Apr 18 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.1-2
- Update spec per review request comments.

* Sat Mar 02 2019 Richard Shaw <hobbes1069@gmail.com> - 5.12.1-1
- Update to 5.12.1 now that the correct version of Qt5 is in Rawhide.

* Tue Feb 05 2019 Miro Hrončok <mhroncok@redhat.com> - 5.11.22-1
- Inital package

Name:          python-libarchive-c
Version:       2.9
Release:       2%{?dist}
Summary:       Python interface to libarchive
License:       CC0
URL:           https://github.com/Changaco/python-libarchive-c

%global forgeurl %{url}
%global tag %{version}
%forgemeta

Source0:       %forgesource

BuildRequires: libarchive-devel
BuildArch:     noarch

%global _description %{expand:
The libarchive library provides a flexible interface for reading and
writing archives in various formats such as tar and cpio. libarchive
also supports reading and writing archives compressed using various
compression filters such as gzip and bzip2.

A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.}

%description %_description

%package -n python%{python3_pkgversion}-libarchive-c
Summary:       %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-libarchive-c}
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-mock
BuildRequires: python%{python3_pkgversion}-pytest
Requires:      libarchive

%description -n python%{python3_pkgversion}-libarchive-c %_description

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build

%install
%py3_install
%{_fixperms} %{buildroot}

%check
%{?el7:export LANG=en_US.UTF-8}
pytest-%{python3_version} -s -vv tests %{?el7:-k "not test_check_archiveentry_using_python_testtar"}

%global _docdir_fmt %{name}

%files -n python%{python3_pkgversion}-libarchive-c
%doc README.rst
%license LICENSE.md
%{python3_sitelib}/libarchive*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020  <zbyszek@in.waw.pl> - 2.9-1
- Update to latest upstream version (#1763575)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Orion Poplawski <orion@nwra.com> - 2.8-7
- Add support for zstd

* Sat May 18 2019 Orion Poplawski <orion@nwra.com> - 2.8-6
- Build for EPEL7

* Sat May  4 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.8-5
- Fix compatibility with python3.8 (#1705558)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.8-3
- Subpackage python2-libarchive-c has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8-1
- Update to 2.8 (#1589605)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.5-2
- Rebuild for Python 3.6

* Mon Aug 15 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5-1
- Update to latest version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.3-1
- Update to latest release

* Wed May 04 2016 Pavel Raiskup <praiskup@redhat.com> - 2.2-5
- fix the build against new libarchive
- stop requiring libarchive 3.1.2 explicitly

* Wed May 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-4
- Rebuild for libarchive 3.2.0

* Wed Mar  9 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.2-3
- Add license text

* Tue Mar  8 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-2
- Remove debuginfo removal and enable tests

* Sat Dec 05 2015 Dhiru Kholia <dhiru@openwall.com> - 2.2-1
- Initial version

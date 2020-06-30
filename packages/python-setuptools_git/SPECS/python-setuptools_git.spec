%global srcname setuptools_git
%global pypi_name setuptools-git

%global common_desc \
This is a plugin for setup tools that enables Git integration.  Once \
installed, Setuptools can be told to include in a module distribution \
all the files tracked by git.  This is an alternative to explicit \
inclusion specifications with MANIFEST.in.

Name:           python-%{srcname}
Version:        1.1
Release:        17%{?dist}
Summary:        Setuptools revision control system plugin for Git

License:        BSD
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git

%description
%{common_desc}


%package -n python3-%{srcname}
Summary:  %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:  python3-setuptools

Provides:  python3-%{pypi_name} == %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}


%prep
%setup -q -n %{pypi_name}-%{version}
%{_bindir}/git config --global user.email "koji@dummy.lan"
%{_bindir}/git config --global user.name "Koji Builder"
%{_bindir}/git init
%{_bindir}/git add .
%{_bindir}/git commit -m'fake commit'


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test -vv
unset LANG


%files -n python3-%{srcname}
%doc PKG-INFO README.rst TODO.txt
%license AUTHORS.txt LICENSE.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-12
- Subpackage python2-setuptools_git has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-10
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-8
- Rebuilt for Python 3.7

* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 1.1-7
- Fix directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuild for Python 3.6

* Sun Sep 25 2016 Björn Esser <fedora@besser82.io> - 1.1-2
- License has changed to BSD, Authors.txt belongs to %%license
- Remove obsolete Group-tag
- Use a common description macro
- Run testsuite
- Conditionalize Python 3 for EPEL <= 7
- Add Requires: python{2,3}-setuptools
- Add Provides: python{2,3}-%%{pypi_name} for convinience

* Tue Jul 26 2016 Dominika Krejci <dkrejci@redhat.com> - 1.1-1
- Update to 1.1.
- Add Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Alan Pevec <apevec@redhat.com> 0.4.2-1
- Initial import, based on python-setuptools_hg RPM

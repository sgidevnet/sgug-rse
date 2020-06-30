%global srcname bna

Name:           python-%{srcname}
Version:        4.1.0
Release:        15%{?dist}
Summary:        Battle.net Authenticator routines in Python
License:        MIT
URL:            http://github.com/Adys/python-bna
Source0:        https://pypi.python.org/packages/source/b/bna/bna-%{version}.tar.gz
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildArch:      noarch

Provides: 		python3-%{srcname}

%description
This is a Python library of Battle.net Authenticator routines,
this package also contains a command-line Battle.net authenticator.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/bna
%{python3_sitelib}/bna*
%{python3_sitelib}/__pycache__/bna*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 19 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.1.0-2
- Provide python3-bna

* Tue Apr 19 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.1.0-1
- Update to version 4.1.0
- Change package to use Python 3
- Use of newest python macros
- Added license tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Christopher Meng <rpm@cicku.me> - 3.2-2
- Add license file.

* Thu Aug 15 2013 Christopher Meng <rpm@cicku.me> - 3.2-1
- Initial Package.

%global srcname nmap

Name:           python-%{srcname}
Version:        0.6.1
Release:        17%{?dist}
Summary:        A Python library which helps in using nmap port scanner

License:        GPLv3+
URL:            http://xael.org/norman/python/python-nmap/
Source0:        http://xael.org/pages/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       nmap

%description
python-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python3-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGELOG README.txt 
%license gpl-3.0.txt
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/python_nmap*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-12
- Remove superfluous variable

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.1-10
- Subpackage python2-nmap has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-8
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-7
- Fix directory ownership

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-2
- Update to latest upstream release 0.6.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-3
- Fix wrong package naming

* Wed Dec 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-2
- Fix package naming (rhbz#1174115)

* Wed Aug 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Switch to py3
- Update the URL and the source URL
- Update to latest upstream version 0.3.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream version 0.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to latest upstream version 0.2.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.4-1
- Initial package

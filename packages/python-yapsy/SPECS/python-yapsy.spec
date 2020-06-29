%global srcname Yapsy
%global modname yapsy

Name:           python-%{modname}
Version:        1.11.223
Release:        18%{?dist}
Summary:        Simple plugin system for Python applications

License:        BSD and CC-BY-SA
URL:            http://yapsy.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{modname}/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Yapsy’s main purpose is to offer a way to easily design a plugin system in\
Python. Yapsy only depends on Python’s standard library.

%description %{_description}

%package doc
Summary:        Documentation for python-yapsy, a plugin system for Python applications
BuildRequires:  python3-sphinx
Obsoletes:      python3-%{modname}-doc < 1.11.223-4

%description doc
Documentation for yapsy, a simple plugin system for Python applications.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build
%{__python3} setup.py build_sphinx

%install
%py3_install

%check
%{__python3} setup.py test || :

%files -n python3-%{modname}
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%files doc
%doc build/sphinx/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.223-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.223-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.223-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11.223-12
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.223-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11.223-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11.223-5
- Rebuild for Python 3.6

* Wed May 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.11.223-4
- Modernize spec
- Add %%check section
- Remove bundled egg

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.223-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.223-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 16 2015 José Matos <jamatos@fedoraproject.org> - 1.11.223-1
- Update to 1.11.223
- Sources for python 2 and 3 have been unified

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.423-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Pete Travis <immanetize@fedoraproject.org> - 1.10.423-1
- Updating to upstream release 1.10.423

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Oct 04 2013 Pete Travis <immanetize@fedoraproject.org> 1.10.2-3
- Turning on python3 boolean so python3 subpackage actually builds
- Correct build and install sections to properly create python3 subpackage
- Remove ill-conceived patches
- Add python3-yapsy-doc subpackage, as upstream procides py3 sources for docs

* Tue Aug 20 2013 Pete Travis <immanetize@fedoraproject.org> 1.10.2-2
- Updating spec file; cleaned up files section and BuildRequires,add noarch -doc subpackage

* Mon Aug 19 2013 Pete Travis <immanetize@fedoraproject.org> 1.10.2-1
- Initial revision

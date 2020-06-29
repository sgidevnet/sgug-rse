%global pypi_name anymarkup

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        3%{?dist}
Summary:        Parse or serialize any markup in Python

License:        BSD
URL:            https://github.com/bkabrda/anymarkup
Source0:        https://github.com/bkabrda/anymarkup/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Parse or serialize any markup. Currently supports ini, json, json5, toml,
xml and yaml.

%package -n python3-%{pypi_name}
Summary: %{summary}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-configobj
BuildRequires: python3-anymarkup-core >= 0.8.0
BuildRequires: python3-xmltodict
BuildRequires: python3-PyYAML
BuildRequires: python3-toml
BuildRequires: python3-json5
BuildRequires: python3-click
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
arse or serialize any markup. Currently supports ini, json, json5, toml,
xml and yaml.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to latest upstream release 0.8.1 (rhbz#1333989))
- Update spec file

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-13
- Subpackage python2-anymarkup has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Petr Viktorin <pviktori@redhat.com> - 0.5.0-7
- Rename the python-anymarkup subpackage to python2-anymarkup
- Change available python- Requires to python2-

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-1
- Update to 0.5.0 (rhbz#1273011)

* Mon Jul 27 2015 jchaloup <jchaloup@redhat.com> - 0.4.3-2
- Tests are not shipped in rpm => no need for pytest as a runtime dependency (rhbz#1247079)

* Wed Jun 17 2015 jchaloup <jchaloup@redhat.com> - 0.4.3-1
- Update to 0.4.3 (rhbz#1232519)

* Thu May 21 2015 jchaloup <jchaloup@redhat.com> - 0.4.2-1
- Initial package (rhbz#1223843)

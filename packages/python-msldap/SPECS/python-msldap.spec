%global pypi_name msldap

Name:           python-%{pypi_name}
Version:        0.3.10
Release:        1%{?dist}
Summary:        Python library to play with MS LDAP

License:        MIT
URL:            https://github.com/skelsec/msldap
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python library to play with MS LDAP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python library to play with MS LDAP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/msldap
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.10-1
- Update to latest upstream release 0.3.10 (rhbz#1851635)

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.9-1
- Update to latest upstream release 0.3.9 (rhbz#1849548)

* Thu Jun 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.8-1
- Update to latest upstream release 0.3.8 (rhbz#1833839)

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to latest upstream release 0.3.6 (rhbz#1833839)

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to latest upstream release 0.3.5 (rhbz#1833839)

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Update to latest upstream release 0.3.4 (rhbz#1833839)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.14-3
- Rebuilt for Python 3.9

* Thu May 14 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.14-2
- include a patch to work with newer prompt_toolkit

* Tue Apr 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.14-1
- Update to latest upstream release 0.2.14 (rhbz#1825710)

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.13-1
- Update to latest upstream release 0.2.13 (rhbz#1815002)

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.12-1
- Update to latest upstream release 0.2.12 (rhbz#1815002)

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.11-1
- Update to latest upstream release 0.2.11 (rhbz#1815002)

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.10-1
- LICENSE file is no in the source tarball
- Update to latest upstream release 0.2.10 (rhbz#1815002)

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.7-1
- Update to latest upstream release 0.2.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-2
- Fix requirement (rhbz#1790355)

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.5-1
- Initial package

%global pypi_name winacl

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Python ACL/ACE/Security Descriptor manipulation library

License:        MIT
URL:            https://github.com/skelsec/winacl
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Platform independent library for interfacing windows security descriptors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Platform independent library for interfacing windows security descriptors.

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
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Update to latest upstream release 0.0.5 (rhbz#1840959)

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Add license file
- Update to latest upstream release 0.0.4 (rhbz#1840959)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Initial package for Fedora

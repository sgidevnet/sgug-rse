%global pypi_name ailment

Name:           python-%{pypi_name}
Version:        8.20.6.8
Release:        1%{?dist}
Summary:        The angr intermediate language

License:        BSD
URL:            https://github.com/angr/ailment
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/angr/ailment/master/LICENSE
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
AIL is the angr intermediate language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
AIL is the angr intermediate language.

%prep
%autosetup -n %{pypi_name}-%{version}
cp -a %{SOURCE1} LICENSE
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
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora

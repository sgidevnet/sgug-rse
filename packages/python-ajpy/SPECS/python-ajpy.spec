%global pypi_name ajpy

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        2%{?dist}
Summary:        AJP package crafting library

License:        BSD
URL:            https://github.com/hypn0s/AJPy/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
AJPy aims to craft AJP requests in order to communicate with AJP connectors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
AJPy aims to craft AJP requests in order to communicate with AJP connectors.

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
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- License file was added by upstream
- Update to latest upstream release 0.0.5

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Initial package for Fedora

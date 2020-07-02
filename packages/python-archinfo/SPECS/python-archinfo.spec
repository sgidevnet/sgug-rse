%global pypi_name archinfo

Name:           python-%{pypi_name}
Version:        8.20.6.8
Release:        1%{?dist}
Summary:        Collection of classes that contain architecture-specific information

License:        BSD
URL:            https://github.com/angr/archinfo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora

%global pypi_name plugnplay

Name:           python-%{pypi_name}
Version:        0.5.4
Release:        2%{?dist}
Summary:        A generic plug-in system for Python

License:        BSD
URL:            http://github.com/daltonmatos/plugnplay
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Plug n' PLay (PnP) is a Generic plug-in system inspired by Trac's internal
component management. With PnP you can turn any program into a pluggable
software very easily. You just have to define the Interfaces and let others
implement them.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Plug n' PLay (PnP) is a Generic plug-in system inspired by Trac's internal
component management. With PnP you can turn any program into a pluggable
software very easily. You just have to define the Interfaces and let others
implement them.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.4-1
- Add upstream license file (rhbz#1809994)
- Update to latest upstream release 0.5.4

* Wed Mar 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.3-1
- Initial package for Fedora

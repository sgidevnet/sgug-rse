%global pypi_name friendlyloris

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        A Slow Loris package for Python

License:        MIT
URL:            https://github.com/jackdcasey/friendlyloris
Source0:        %{pypi_source}
BuildArch:      noarch

%description
friendlyloris is a simple slow loris library for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
friendlyloris is a simple slow loris library for Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/jackdcasey/friendlyloris/pull/1
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora

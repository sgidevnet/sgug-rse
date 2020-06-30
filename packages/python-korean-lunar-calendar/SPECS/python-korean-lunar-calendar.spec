%global pypi_name korean-lunar-calendar
%global internal_name korean_lunar_calendar

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Convert Korean lunar-calendar to Gregorian calendar

License:        MIT
URL:            https://github.com/usingsky/korean_lunar_calendar_py
Source0:        %{pypi_source %{internal_name}}
BuildArch:      noarch

%description
A library to convert Korean lunar-calendar to Gregorian calendar.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A library to convert Korean lunar-calendar to Gregorian calendar.

%prep
%autosetup -n %{internal_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{internal_name}/
%{python3_sitelib}/%{internal_name}-%{version}-py*.egg-info/

%changelog
* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Add LICENSE file from tarball
- Update to latest upstream release 0.2.1

* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora

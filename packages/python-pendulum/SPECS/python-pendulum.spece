%global pypi_name pendulum

Name:           python-%{pypi_name}
Version:        2.0.5
Release:        4%{?dist}
Summary:        Python datetimes made easy

License:        MIT
URL:            https://pendulum.eustace.io
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-2
- Fix description (rhbz#1790074)

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-1
- Initial package for Fedora

%global pypi_name nose-timer

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        A timer plugin for nosetests

License:        MIT
URL:            https://github.com/mahmoudimus/nose-timer
Source0:        %pypi_source
BuildArch:      noarch

%description
A timer plugin for nosetests that answers the question: How much time does
every test take?

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A timer plugin for nosetests that answers the question: How much time does
every test take?

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/nosetimer
%{python3_sitelib}/nose_timer-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0 (rhbz#1818574)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-2
- Better use of wildcards (rhbz#1786855)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-1
- Initial packagefor Fedora

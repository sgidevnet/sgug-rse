%global pypi_name baluhn

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        7%{?dist}
Summary:        A base-independent implementation of the Luhn algorithm for Python

License:        Unlicense
URL:            https://github.com/benhodgson/baluhn
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Baluhn provides a base-independent implementation of the Luhn algorithm for
Python. It is useful for generating and verifying check digits in arbitrary
bases.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Baluhn provides a base-independent implementation of the Luhn algorithm for
Python. It is useful for generating and verifying check digits in arbitrary
bases.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-2
- Fix license (rhbz#1713969)

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora

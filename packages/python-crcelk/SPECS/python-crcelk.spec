%global pypi_name crcelk

Name:           python-%{pypi_name}
Version:        1.3
Release:        7%{?dist}
Summary:        Python implementation of the CRC algorithm

License:        MIT
URL:            https://github.com/zeroSteiner/crcelk
Source0:        %{pypi_source}
BuildArch:      noarch

%description
CrcElk provides a pure Python implementation of the CRC algorithm and allows
for variants to easily be defined by providing their parameters such as width,
starting polynomial, etc.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
CrcElk provides a pure Python implementation of the CRC algorithm and allows
for variants to easily be defined by providing their parameters such as width,
starting polynomial, etc.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' crcelk.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}*.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Initial package for Fedora

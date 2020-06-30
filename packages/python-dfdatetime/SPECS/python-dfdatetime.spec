%global pypi_name dfdatetime
%global date 20200613

Name:           python-%{pypi_name}
Version:        0.0.%{date}
Release:        1%{?dist}
Summary:        Python module for digital forensics date and time

License:        ASL 2.0
URL:            https://github.com/log2timeline/dfdatetime
Source0:        %{url}/archive/%{date}/%{pypi_name}-%{date}.tar.gz
BuildArch:      noarch

%description
A Python module that provides date and time objects to preserve accuracy and
precision for digital forensics.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python module that provides date and time objects to preserve accuracy and
precision for digital forensics.

%prep
%autosetup -n %{pypi_name}-%{date}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{pypi_name}/*

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc ACKNOWLEDGEMENTS AUTHORS README
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200613-1
- Update to latest upstream release 20200613

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20190517-7
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190517-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190517-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190517-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190517-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190517-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20190517-1
- Update version (rhbz#1720885)

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190517-1
- Initial package for Fedora

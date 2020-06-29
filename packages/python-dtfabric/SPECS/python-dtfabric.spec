%global pypi_name dtfabric
%global date 20200621

Name:           python-%{pypi_name}
Version:        0.0.%{date}
Release:        3%{?dist}
Summary:        Tool to manage data types and structures, as used by libyal

License:        ASL 2.0
URL:            https://github.com/libyal/dtfabric
Source0:        %{url}/archive/%{date}/%{pypi_name}-%{date}.tar.gz
BuildArch:      noarch

%description
dtfabric is a project to manage data types and structures, as used in the
libyal projects.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
dtfabric is a project to manage data types and structures, as used in the
libyal projects.

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
%{_bindir}/*.py
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-3
- Update summary

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-2
- Add python3-setuptools as BR

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200621-1
- Update to latest upstream release 20200621 (rhbz#20200621)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20200119-2
- Rebuilt for Python 3.9

* Fri Mar 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20200119-1
- Update source URL
- Update to latet uptream release 20200119 (rhbz#1815602)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190120-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190120-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.20190120-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20190120-1
- Update version (rhbz#1720890)

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 20190120-1
- Initial package for Fedora

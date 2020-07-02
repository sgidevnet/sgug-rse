%global pypi_name cachy

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        5%{?dist}
Summary:        Simple yet effective caching library

License:        MIT
URL:            https://github.com/sdispater/cachy
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Cachy provides a simple yet effective caching library.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

#Recommends:     python3dist(memcached) >= 1.59
Recommends:     python3-msgpack >= 0.5.0
Recommends:     python3-redis >= 2.10.0
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cachy provides a simple yet effective caching library.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%exclude %{python3_sitelib}/tests/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Update to latest upstream release 0.3.0 (rhbz#1742549)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-4
- Clean-up spec file

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-2
- Add Recommends for optional dependencies.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Initial package.


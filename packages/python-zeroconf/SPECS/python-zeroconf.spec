%{?python_enable_dependency_generator}
%global pypi_name zeroconf

Name:           python-%{pypi_name}
Version:        0.27.1
Release:        1%{?dist}
Summary:        Pure Python Multicast DNS Service Discovery Library

License:        LGPLv2
URL:            https://github.com/jstasiak/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3dist(ifaddr)

# Integration tests work in mock but fail in Koji with PermissionError
%bcond_with integration

%description
A pure Python implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%package -n     python3-%{pypi_name}
Summary:        Pure Python 3 Multicast DNS Service Discovery Library
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A pure Python 3 implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install


%check
# IPv6 tests fail in Koji/mock
# test_ptr_optimization fails in Koji
%{__python3} -m pytest -n auto -v \
%if %{with integration}
  -k "not v6" \
%else %{without integration}
  -k "not integration and not test_ptr_optimization and not v6" \
%endif
  %{pypi_name}/test*


%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jun 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.27.1-1
- Update to 0.27.1

* Sat May 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.27.0-1
- Update to 0.27.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1

* Wed Apr 15 2020 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-1
- Update to 0.25.1 (#1823981)

* Tue Apr 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.25.0-1
- Update to 0.25.0

* Sun Mar 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.24.5-1
- Update to 0.24.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Miro Hrončok <mhroncok@redhat.com> - 0.24.4-1
- New version 0.24.4 (#1787774)

* Wed Dec 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-1
- New version 0.24.2

* Tue Dec 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.1-1
- New version 0.24.1

* Wed Nov 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.24.0-1
- New version 0.24.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.23.0-1
- New version 0.23.0

* Sun Apr 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.22.0-1
- New version 0.22.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.3-2
- Enable python dependency generator

* Mon Dec 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.21.3-1
- New version 0.21.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.20.0-1
- New version 0.20.0
- Drop python2 package (retired upstream, no more Fedora users)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.19.1-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-1
- New version 0.19.1 (#1461043)
- Updated (B)Rs to use python2- where possible

* Tue Mar 14 2017 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-2
- Remove enum-compat from install_requires (#1432165)

* Sat Feb 18 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.18.0-1
- Update to 0.18.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-3
- Rebuild for Python 3.6

* Wed Dec 21 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-2
- Add Python 2 subpackage

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17.6-1
- Initial package

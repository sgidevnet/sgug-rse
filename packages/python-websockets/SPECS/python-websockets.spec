%global pypi_name websockets

Name:           python-%{pypi_name}
Version:        8.0.2
Release:        5%{?dist}
Summary:        An implementation of the WebSocket Protocol for python with asyncio

License:        BSD
URL:            https://pypi.python.org/pypi/websockets
Source0:        https://github.com/aaugustin/websockets/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%global _description \
websockets is a library for developing WebSocket servers and clients in\
Python. It implements RFC 6455 with a focus on correctness and simplicity. It\
passes the Autobahn Testsuite.\
\
Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it\
provides an API based on coroutines, making it easy to write highly concurrent\
applications.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove upstream's egg-info
rm -vrf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
# Remove installed C file
rm -vf %{buildroot}%{python3_sitearch}/%{pypi_name}/speedups.c

%check
# Skip tests because they fail on Python 3.8. See: https://github.com/aaugustin/websockets/issues/648
# WEBSOCKETS_TESTS_TIMEOUT_FACTOR=100 %%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.2-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Julien Enselme <jujens@jujens> - 8.0.2-1
- Update to 8.0.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 8.0-2
- Skip tests because it prevents rebuild for Python 3.8. They fail because tests check the number of deprecation warnings and more are raised on Python 3.8.

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 8.0-1
- Update to 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Julien Enselme <jujens@jujens.eu> - 6.0
- Update to 6.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-2
- Rebuilt for Python 3.7

* Sat Jun 02 2018 Julien Enselme <jujens@jujens.eu> - 5.0.1-1
- Update to 5.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 4.0.1-1
- Update to 4.0.1

* Mon Aug 21 2017 Julien Enselme <jujens@jujens.eu> - 3.4-2
- Remove tests with timeouts

* Mon Aug 21 2017 Julien Enselme <jujens@jujens.eu> - 3.4-1
- Update to 3.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 3.3-1
- Update to 3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2-3
- Rebuild for Python 3.6

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 3.2-2
- Correct tests on Python 3.5.2

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 3.2-1
- Update to 3.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 21 2016 Julien Enselme <jujens@jujens.eu> - 3.1-1
- Update to 3.1

* Sun Feb 14 2016 Julien Enselme <jujens@jujens.eu> - 3.0-1
- Update to 3.0
- Correct build on rawhide

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Julien Enselme <jujens@jujens.eu> - 2.7-1
- Update to 2.7

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 26 2015 Julien Enselme <jujens@jujens.eu> - 2.6-1
- Initial package

%global srcname paho-mqtt

Name:           python-%{srcname}
Version:        1.5.0
Release:        5%{?dist}
Summary:        Python MQTT version 3.1/3.1.1/5.0 client class

License:        EPL-1.0
URL:            http://eclipse.org/paho/
Source0:        https://github.com/eclipse/paho.mqtt.python/archive/v%{version}/%{srcname}-%{version}.tar.gz
Buildarch:      noarch

%description
This library provides a client class which enable applications to connect to
an MQTT broker to publish messages, and to subscribe to topics and receive
published messages. It also provides some helper functions to make publishing
one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M) connectivity protocol. Designed
as an extremely lightweight publish/subscribe messaging transport, it is useful
for connections with remote locations where a small code footprint is required
and/or network bandwidth is at a premium.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library provides a client class which enable applications to connect to
an MQTT broker to publish messages, and to subscribe to topics and receive
published messages. It also provides some helper functions to make publishing
one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M) connectivity protocol. Designed
as an extremely lightweight publish/subscribe messaging transport, it is useful
for connections with remote locations where a small code footprint is required
and/or network bandwidth is at a premium.

%prep
%autosetup -n paho.mqtt.python-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CONTRIBUTING.md README.rst *.html
%license LICENSE.txt
%{python3_sitelib}/paho/
%{python3_sitelib}/paho*.egg-info

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-5
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-2
- Fix license tag

* Fri Nov  1 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.0-1
- Update to 1.5.0 with MQTT 5.0 support

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Sep 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to new upstream version 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Update to new upstream version 1.3.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to new upstream version 1.3.0

* Sat Apr 22 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to new upstream version 1.2.3

* Wed Apr 12 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to new upstream version 1.2.2

* Tue Apr 04 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to new upstream version 1.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to new upstream version 1.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-4
- Cleanup

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Update to new upstream version 1.1

* Wed Aug 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial package

# Currently fails
%define with_tests 0

Name:           python-can
Version:        3.3.3
Release:        2%{?dist}
Summary:        Controller Area Network (CAN) support for Python

License:        LGPLv3
URL:            https://github.com/hardbyte/python-can
Source0:        https://github.com/hardbyte/python-can/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_tests}
BuildRequires:  python3-nose
BuildRequires:  python3-mock
%endif

%description
The Controller Area Network is a bus standard designed to allow microcontrollers
and devices to communicate with each other. It has priority based bus
arbitration, reliable deterministic communication. It is used in cars, trucks,
boats, wheelchairs and more.

The can package provides controller area network support for Python developers;
providing common abstractions to different hardware devices, and a suite of
utilities for sending and receiving messages on a can bus.

%package -n python3-can
Summary:        Controller Area Network (CAN) support for Python 3
%{?python_provide:%python_provide python3-can}

%description -n python3-can
The Controller Area Network is a bus standard designed to allow microcontrollers
and devices to communicate with each other. It has priority based bus
arbitration, reliable deterministic communication. It is used in cars, trucks,
boats, wheelchairs and more.

The can package provides controller area network support for Python developers;
providing common abstractions to different hardware devices, and a suite of
utilities for sending and receiving messages on a can bus.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/test/

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-can
%license LICENSE.txt
%{_bindir}/can_logger.py
%{_bindir}/can_player.py
%{_bindir}/can_viewer.py
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 3.3.3-1
- New upstream 3.3.3 release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.3.1-1
- New upstream 3.3.1 release
- Cleanups for review

* Fri Dec  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-3
- Fix license, fix provides

* Fri Dec  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-2
- Package updates

* Thu Sep 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-1
- initial packaging

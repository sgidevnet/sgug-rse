# disable tests due to intermittent failures
# https://github.com/altdesktop/i3ipc-python/issues/149
%bcond_with     tests

Name:           python-i3ipc
Version:        2.1.1
Release:        2%{?dist}
Summary:        An improved Python library to control i3wm
License:        BSD
URL:            https://github.com/altdesktop/i3ipc-python
BuildArch:      noarch

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/altdesktop/i3ipc-python/pull/76
Patch0:         0001-Adapt-test-launcher-for-our-envirnoment.patch
# https://github.com/altdesktop/i3ipc-python/issues/128
Patch1:         %{url}/commit/4cc59d5550eab1eb3f0679461fd9c86449b407bc.patch#/0002-remove-enum-compat-dependency.patch

BuildRequires:  python3-devel
%if %{with tests}
# Test deps
BuildRequires:  i3
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-xlib
BuildRequires:  xorg-x11-server-Xvfb
%endif

%global desc \
i3's interprocess communication (or ipc) is the interface i3wm uses to receive\
commands from client applications such as i3-msg. It also features\
a publish/subscribe mechanism for notifying interested parties of window\
manager events.\
\
i3ipc-python is a Python library for controlling the window manager. This\
project is intended to be useful for general scripting, and for applications\
that interact with the window manager like status line generators, notification\
daemons, and pagers.\

%description
%{desc}

%package -n python3-i3ipc
Summary:        %{summary}
%{?python_provide:%python_provide python3-i3ipc}

%description -n python3-i3ipc
%{desc}

%prep
%autosetup -p1 -n i3ipc-python-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
# testing on python3 only, as the test runner is broken on python2
python3 run-tests.py --timeout 20
%endif

%files -n python3-i3ipc
%{python3_sitelib}/*
%license LICENSE
%doc README.rst

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Aleksei Bavshin <alebastr89@gmail.com> - 2.1.1-1
- Update to upstream version 2.1.1 (#1708021)
- Update upstream URL
- Disable tests due to failures

* Wed Feb 26 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.5.1-8
- Patch: 0002-remove-enum-compat-dependency (#1770839)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.1-2
- Subpackage python2-i3ipc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 07 2018 Michael Simacek <msimacek@redhat.com> - 1.5.1-1
- Update to upstream version 1.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Michael Simacek <msimacek@redhat.com> - 1.4.0-1
- Update to upstream version 1.4.0
- Enable tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Michael Simacek <msimacek@redhat.com> - 1.3.0-2
- Fix Requires on python2-enum34

* Wed Aug 16 2017 Michael Simacek <msimacek@redhat.com> - 1.3.0-1
- Update to upstream version 1.3.0
- Enable python3 support

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 19 2016 Michael Simacek <msimacek@redhat.com> - 1.2.0-1
- Initial packaging

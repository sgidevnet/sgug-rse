# Created by pyp2rpm-3.2.2
Name:           ampy
Version:        1.0.5
Release:        8%{?dist}
Summary:        Command line tool to interact with a MicroPython board over a serial connection

License:        MIT
URL:            https://github.com/adafruit/ampy

# Use GitHub archive instead of PyPi sdist to have tests, README, LICENSE
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

Provides:       adafruit-%{name} = %{version}-%{release}
Provides:       python3-adafruit-%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-adafruit-%{name}}


%description
Adafruit MicroPython tool is a command line tool to interact with a MicroPython
board over a serial connection.

Ampy is meant to be a simple command line tool to manipulate files and run code
on a MicroPython board over its serial connection. With ampy you can send files
from your computer to a MicroPython board's file system, download files from a
board to your computer, and even send a Python script to a board to be
executed.

Note that ampy by design is meant to be simple and does not support advanced
interaction like a shell or terminal to send input to a board. 


%prep
%autosetup -n %{name}-%{version}

# shebangs
sed -i '1d' $(grep -lr '#!/usr/')


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m unittest tests/test_*.py -v


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/adafruit_ampy-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-5
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-1
- Update to 1.0.5 (#1610571)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Initial package

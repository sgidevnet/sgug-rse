%global srcname RPi.GPIO

%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-rpi-gpio
Version:        0.7.0
Release:        3%{?dist}
Summary:        Class to control the GPIO on a Raspberry Pi

License:        MIT
URL:            https://sourceforge.net/projects/raspberry-gpio-python/
Source0:        http://sourceforge.net/projects/raspberry-gpio-python/files/RPi.GPIO-%{version}.tar.gz

ExclusiveArch:  %{arm} aarch64

BuildRequires:  gcc

%description
Python library for GPIO access on a Raspberry Pi.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python 3 library for GPIO access on a Raspberry Pi.

%prep
%autosetup -n %{srcname}-%{version}

%build
CFLAGS="${RPM_OPT_FLAGS} -fcommon"
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.txt
%license LICENCE.txt
%{python3_sitearch}/RPi*

%changelog
* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-3
- Fix FTBFS (rhbz#1799949)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Update to latest upstream release 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.5-1
- Update to latest upstream release 0.6.5
- Remove Python2 support
- Fix FTBFS (rhbz#1605892, rhbz#1675786)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-1
- Update to 0.6.3
- Only build on supported architectures

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuild for Python 3.6

* Mon Aug 29 2016 Dominika Krejci <dkrejci@redhat.com> 0.6.2-1
- Update to 0.6.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Add py3 support
- Update to new upstream version 0.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.11-1
- Update to 0.5.11

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 30 2012 Kushal Das <kushal@fedoraproject.org> 0.3.1a-1
- Intial package

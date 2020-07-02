%global srcname shadowsocks
%global sum A fast tunnel proxy that help you get through firewalls

Name:           python-shadowsocks
Version:        2.9.1
Release:        13%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://shadowsocks.org/
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Shadowsocks is a socks5 tunnel proxy, designed to secure your Internet
traffic.

%package -n python3-%{srcname}
Summary:        %{sum} (Python 3)
# libsodium is loaded with ctypes
Requires:       libsodium
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Shadowsocks is a socks5 tunnel proxy, designed to secure your Internet
traffic.

This package contains the client and server implementation for Shadowsocks in
Python 3.

%prep
%setup -q -n %{srcname}-%{version}
# remove shebangs in the module files
sed -i -e '/^#!\//, 1d' %{srcname}/*.py %{srcname}/crypto/*.py
# explicitly remove the included egg
rm -fr %{srcname}*.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{_bindir}/sslocal
%{_bindir}/ssserver
%{python3_sitelib}/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct  4 2018 Robin Lee <cheeselee@fedoraproject.org> - 2.9.1-7
- Remove python2 subpackage (BZ#1634883)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Remi Collet <remi@fedoraproject.org> - 2.9.1-3
- rebuild for libsodium

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Robin Lee <cheeselee@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1, github version
- python-shadowsocks renamed to python2-shadowsocks
- Only packages the Python 3 version of commands
- Fix problem with openssl 1.1 (BZ#1447274)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 23 2016 Robin Lee <cheeselee@fedoraproject.org> - 2.8.2-5
- Requires libsodium for chacha20 encryption method.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 30 2015 Robin Lee <cheeselee@fedoraproject.org> - 2.8.2-2
- 2.8.2 license changed to ASL 2.0

* Fri Oct 30 2015 Robin Lee <cheeselee@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.4.3-2
- Build a subpackage for python3

* Sun Nov 16 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Sat Sep 13 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Tue Jul 15 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11, LICENSE included
- Explicitly remove the included egg

* Sat Jul 12 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.0.10-2
- BuildRequires python2-setuptools

* Sat Jul 12 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10
- Requries and BuildRequires m2crypto

* Sun Jul  6 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.0.8-2
- Explicitly use python2 macros

* Sat Jun 28 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.0.8-1
- Initial package for Fedora

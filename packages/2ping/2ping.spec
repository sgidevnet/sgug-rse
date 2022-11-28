Name:           2ping
Version:        4.3
Release:        3%{?dist}
Summary:        Bi-directional ping utility
License:        GPLv2+
URL:            https://www.finnie.org/software/2ping
Source0:        https://www.finnie.org/software/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN, 
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%autosetup

%build
%py3_build

%install
%py3_install
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}/%{_mandir}/man1/2ping6.1

%check
%{__python3} setup.py test

%files
%doc ChangeLog README
%license COPYING
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_bindir}/%{name}6
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}6.1*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.3-2
- Spec cleanup and modernization, thanks to Fabian Affolter (fab)

* Thu Jul 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.3-1
- Update to 4.3 (thanks to Ryan Finnie) fixes rhbz#1473919

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 4.1-1
- Update to 4.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Tue Mar 01 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.2.0-2
- Fix for EL6 and EPEL7
- Cleanup the SPEC file

* Tue Mar 01 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Tue Mar 01 2016 Ryan Finnie <ryan@finnie.org> - 3.1.0-1
- Update to 3.1.0 (#1275261)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.0-5
- Perl 5.20 rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 2.0-2
- Perl 5.18 Rebuild.

* Thu May 17 2012 Christopher Meng <rpm@cicku.me> - 2.0-1
- Initial Package.

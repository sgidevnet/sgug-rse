Name:              bashmount
Version:           3.2.0
Release:           11%{?dist}

Summary:           A menu-driven bash script for mounting removable media
License:           GPLv2
URL:               http://sourceforge.net/projects/bashmount
Source0:           http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz

BuildArch:         noarch

%if 0%{?rhel} >= 7 || 0%{?fedora}
# This dependency is actually optional, but RPM doesn't support optional
# or suggested dependencies yet.
Requires:          udisks2
%endif

%description
bashmount is a menu-driven bash script that uses udisks2 to easily mount,
unmount or eject removable devices without dependencies on any GUI or
desktop environment. An extensive configuration file allows custom commands
to be run on devices.

The use of udisks2 is optional. The mount command can be used, or any other
suitable back-end can be configured.


%prep
%setup -q


%build
#nothing to do


%install
install -p -D -m755 bashmount \
    %{buildroot}%{_bindir}/bashmount
install -p -D -m644 bashmount.conf \
    %{buildroot}%{_sysconfdir}/bashmount.conf
install -p -D -m644 bashmount.1 \
    %{buildroot}%{_mandir}/man1/bashmount.1


%files
%doc COPYING NEWS
%{_bindir}/bashmount
%{_mandir}/man1/bashmount.1*
%config(noreplace) %{_sysconfdir}/bashmount.conf


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-3
- fix macro for udisks2 dependency

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-2
- do not depend on udisks2 on EL6

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.2.0-1
- update to upstream release 3.2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-3
- preserve timestamps
- remove some unnecessary macros

* Tue Feb 07 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-2
- remove redundant BuildRoot tag
- remove redundant cleaning of BuildRoot within the install section
- remove redundant clean section

* Mon Feb 06 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.2-1
- update to 1.6.2

* Sun Feb 05 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.6.1-1
- initial Fedora package

Name:           bournal
Version:        1.5
Release:        19%{?dist}
Summary:        Write personal, password-protected journal entries

License:        GPLv3+
URL:            https://github.com/jose1711/bournal
Source0:        https://github.com/jose1711/bournal/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       gnupg
Requires:       vim

%description
Bournal is a bash script that allows you to keep a personal,
minimalistic, password-protected journal, log, or diary. It
includes encryption, regexp searches, and a date-sorted list
for editing old entries. Since Bournal is pure bash, it should
be easily editable for the CLI-savvy.

%prep
%setup -q

%build
#nothing to build

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%doc changelog.txt README
%license LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-18
- Update URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-8
- Spec file updated

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-6
- Updated to match new guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-3
- Rebuilt

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Fabian Affolter <fabian@bernewireless.net> - 1.5-1
- Switched from ccrypt to gnupg
- Updated to new upstream version 1.5

* Sat Feb 27 2010 Fabian Affolter <fabian@bernewireless.net> - 1.4.1-1
- Updated URL and source URL
- Updated to new upstream version 1.4.1 to fix #568440

* Sun Aug 02 2009 Fabian Affolter <fabian@bernewireless.net> - 1.3-2
- Removed all icons and desktop stuff

* Thu Mar 19 2009 Fabian Affolter <fabian@bernewireless.net> - 1.3-1
- Added icons
- Added .desktop file
- Removed nano, vim is enough
- Updated to new upstream version 1.3

* Wed Jan 20 2009 Fabian Affolter <fabian@bernewireless.net> - 1.2-1
- Initial spec for Fedora

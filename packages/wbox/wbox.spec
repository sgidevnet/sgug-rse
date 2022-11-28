Name:           wbox
Version:        5
Release:        18%{?dist}
Summary:        HTTP testing tool and configuration-less HTTP server

License:        BSD
URL:            http://www.hping.org/wbox/
Source0:        http://www.hping.org/%{name}/%{name}-%{version}.tar.gz
# Man page from http://patch-tracker.debian.org/patch/debianonly/view/wbox/5-1
Source1:        wbox.1

BuildRequires:  gcc

%description
Wbox aims to help you having fun while testing HTTP related stuff.
You can use it to perform many tasks, including the following.
 * Benchmarking how much time it takes to generate content
   for your web application.
 * Web server and web application stressing.
 * Testing virtual domains configuration without the need to alter
   your local resolver.
 * Check if your redirects are working correctly emitting
   the right HTTP code.
 * Test if the HTTP compression is working and if it is actually
   serving pages faster.
 * Use it as a configuration-less HTTP server to share files!

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" 

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc AUTHORS Changelog README
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 5-15
- Fix BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Fabian Affolter <mail@fabian-affolter.ch> - 5-5
- Whitespaces removed
- Comment added

* Thu Jan 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 5-4
- Minor updates

* Tue Dec 27 2011 Athmane Madjoudj <athmane@fedoraproject.org> - 5-3
- Use version macro
- Remove rm -rf buildroot

* Mon Dec 19 2011 Athmane Madjoudj <athmane@fedoraproject.org> - 5-2
- Add manpage from Debian project
- Some minor fixes

* Mon Dec 19 2011 Athmane Madjoudj <athmane@fedoraproject.org> - 5-1
- Initial spec

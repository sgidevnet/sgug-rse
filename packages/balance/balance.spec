Name: balance
Version: 3.57
Release: 4%{?dist}
Summary: TCP load-balancing proxy server with round robin and failover mechanisms
License: GPLv2
Source0: http://www.inlab.de/%{name}-%{version}.tar.gz
URL: http://www.inlab.de/balance.html

BuildRequires: gcc

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms.  The program behaviour can
be controlled at runtime using a simple command line syntax. 

%prep
%setup -q

%build
%{__make} %{?_smp_mflags} CFLAGS="%optflags"

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{_localstatedir}/run/%{name}
%{__install} -Dp -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
%{__install} -Dp -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README COPYING
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_localstatedir}/run/%{name}

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Luis Bazan <lbazan@fedoraproject.org> - 3.57-1
- New upstream version

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.52-16
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-3
- Rebuilt for glibc bug#747377

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 27 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.52-1
- new version 3.52

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Ville Skyttä <ville.skytta at iki.fi> - 3.42-6
- Build with $RPM_OPT_FLAGS (#497435).

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 11 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.42-4
- the ipv6 code in balance is broken, disabling it for now

* Mon Nov 10 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.42-3
- Changes from bugzilla #470626 Comment #1 From Fabian Affolter ->
- simplify %%build section summarizing the commands
- improve macros usage

* Fri Nov 07 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 3.42-2
- Rebuild for Fedora 10.

* Tue Apr 08 2008 T.Obermair > 3.42 
- update version

* Sat Nov 24 2007 T.Obermair > 3.40 
- update version

* Mon Jan 15 2007 T.Obermair > 3.35 
- update version

* Sat Mar 18 2006 T.Obermair > 3.34 
- update version

* Wed Oct 19 2005 T.Obermair > 3.28 
- update version

* Fri Oct 31 2003 Bojan Smojver <bojan at rexursive dot com> 3.11-1 
- update version

* Mon Sep  22 2003 Thomas Steudten <thomas at steudten dot com> 3.10-2 
- rebuild
- fix/expand specfile

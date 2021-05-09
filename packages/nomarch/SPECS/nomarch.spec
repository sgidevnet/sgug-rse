Name:    nomarch
Version: 1.4
Release: 22%{?dist}

Summary: GPLed Arc de-archiver

License:   GPLv2+
URL:       http://www.svgalib.org/rus/nomarch.html
Source:    ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.gz

BuildRequires: gcc


%description
nomarch lists/extracts/tests `.arc' archives. (It also handles `.ark'
files, they're exactly the same.) This is a *very* outdated file
format which should never be used for anything new, but unfortunately,
you can still run into it every so often.


%prep
%setup -q


%build
%make_build CFLAGS="%{optflags}"


%install
%make_install \
  BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1"


%files
%doc ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.4-5
- Rebuild against gcc 4.4 and rpm 4.6

* Wed Sep 3 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-4
- Update URL

* Fri Feb 08 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-3
- gcc 4.3 rebuild
- License fix

* Sat Sep 02 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-2
- FE6 Rebuild

* Sun Jul 30 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-1
- upstream made a new release! Packager nirvana ends...

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.3-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 16 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.3-4
- me is gcc4.1-proof

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com>
- 1.3-3
- rebuild on all arches

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.3-0.fdr.1
- Fedorization

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- 1.3-0
- Initial package. (using DAR)

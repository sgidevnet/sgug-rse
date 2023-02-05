Name:    freeze
Version: 2.5.0
Release: 27%{?dist}
Summary: freeze/melt/fcat compression utilities

# Confirmed with upstream, see email text in Source1
License:   GPL+
# No one agrees on the canonical download site, everyone uses the same version
Source0:   http://www.ibiblio.org/pub/Linux/utils/compress/freeze-%{version}.tar.gz
Source1:   Freeze_license_email.txt
Patch0:    freeze-2.5.patch
Patch1:    freeze-2.5.0-printf.patch
Patch2:    freeze-2.5.0-deffile.patch

BuildRequires: gcc

%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

%prep
%setup -q
cp -a %{SOURCE1} .
%patch0 -p1 -b .Makefile
%patch1 -p1 -b .printf
%patch2 -p1 -b .deffile

%build
chmod u+x configure
%configure
%make_build CFLAGS="$RPM_OPT_FLAGS -Dputc=putc"

%install
%make_install \
  DEST="%{buildroot}%{_bindir}" MANDEST="%{buildroot}%{_mandir}/man1/" \
  INSTALL_PROGRAM='install -D -p -m 0755' INSTALL_DATA='install -D -p -m 0644'

### Fix symlinks properly
for bin in fcat melt unfreeze; do
        ln -fs freeze %{buildroot}%{_bindir}/$bin
        rm -f %{buildroot}%{_mandir}/man1/$bin.1
        ln -fs freeze.1.gz %{buildroot}%{_mandir}/man1/$bin.1.gz
done

%files
%doc MANIFEST README Freeze_license_email.txt
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.5.0-10
- Rebuilt against gcc 4.4 and rpm 4.6

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.5.0-9
- fix license tag with copyright holder clarification

* Fri Feb 08 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-8
- gcc 4.3 rebuild

* Sat Sep 02 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-7
- FE6 Rebuild

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-6
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 16 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 2.5.0-5
- rebuild with gcc 4.1

* Sat Jul 23 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- 2.5.0-4
- Fix bad printf string (#149613).
- Fix default cnf file location in readme and man page.
- Don't strip.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 11 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- 2.5.0-0.fdr.2
- Build with rpm opt flags.

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 
- 0:2.5.0-0.fdr.1
- Fedorization

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com>
- 2.5-2
- Cosmetic rebuild for Group-tag.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com>
- 2.5-1
- Initial package. (using DAR)

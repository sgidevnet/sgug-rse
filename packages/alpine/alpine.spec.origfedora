# Fedora review: http://bugzilla.redhat.com/249365

# crasher workaround, http://bugzilla.redhat.com/1282092
%undefine _hardened_build

Summary: powerful, easy to use console email client
Name: alpine
Version: 2.24
Release: 1%{?dist}

License: ASL 2.0
URL:     http://alpine.x10host.com/
Source0: http://alpine.x10host.com/alpine/patches/alpine-%{version}/alpine-%{version}.tar.xz
Source1: README.fedora

Patch1: alpine-2.24-useragent.patch
Patch2: alpine-2.23-gcc10.patch

# Using "Conflicts" instead of Obsoletes because while alpine is substantially
# compatible with pine the change to Unicode breaks important user
# functionality such as non-ASCII encoded saved passwords. Additionally, there
# are also many patches to pine floating around that for political/technical
# reasons will not be integrated into alpine. (I'd like to stay out of it...
# just search "Mark Crispin maildir" for the gory details.) Since licensing
# prevents a Fedora pine package, I cannot predict what patches users might
# have and so want to warn them instead of automatically replacing their pine
# install with an alpine that could break their configuration. 
# I understand this to be a special case of the "Optional Functionality"
# description at http://fedoraproject.org/wiki/Packaging/Conflicts
Conflicts: pine

Provides: re-alpine = %{version}-%{release}

#BuildRequires: automake libtool
BuildRequires: gettext
BuildRequires: hunspell
## passing --with-npa=/usr/bin/inews
#BuildRequires: inews
BuildRequires: krb5-devel
BuildRequires: ncurses-devel 
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: passwd
# passing --with-smtp-msa=/usr/sbin/sendmail instead
#BuildRequires: /usr/sbin/sendmail 

Requires: hunspell
Requires: mailcap
Requires: /usr/sbin/sendmail

BuildRequires: gcc

%description
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.  
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.
Changes and enhancements over pine:
  * Released under the Apache Software License, Version 2.0.
  * Internationalization built around new internal Unicode support.
  * Ground-up reorganization of source code around new "pith/" core 
routine library.
  * Ground-up reorganization of build and install procedure based on 
GNU Build System's autotools.


%prep
%setup -q -n alpine-%{version}
%patch1 -p1
%patch2 -p1

install -m644 -p %{SOURCE1} .


%build
touch imap/ip6
# --without-tcl disables the TCL-based CGI "Web Alpine"
%configure \
  --enable-debug=no \
  --without-tcl \
  --with-c-client-target=lfd \
  --with-smtp-msa=/usr/sbin/sendmail \
  --with-npa=/usr/bin/inews \
  --with-passfile=.alpine.passfile \
  --with-simple-spellcheck=hunspell \
  --with-interactive-spellcheck=hunspell \
  --with-system-pinerc=%{_sysconfdir}/pine.conf \
  --with-system-fixed-pinerc=%{_sysconfdir}/pine.conf.fixed

%make_build EXTRACFLAGS="$RPM_OPT_FLAGS"


%install
%make_install

# create/touch %ghost'd files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed


%files
%doc README
%doc README.fedora
%license LICENSE
%ghost %config(noreplace) %{_sysconfdir}/pine.conf
%ghost %config(noreplace) %{_sysconfdir}/pine.conf.fixed
%{_bindir}/alpine
%{_bindir}/pico
%{_bindir}/pilot
%{_bindir}/rpload
%{_bindir}/rpdump
%{_mandir}/man1/alpine.1*
%{_mandir}/man1/pico.1*
%{_mandir}/man1/pilot.1*
%{_mandir}/man1/rpload.1*
%{_mandir}/man1/rpdump.1*


%changelog
* Sun Oct 11 2020 josef radinger <cheese@nosuchhost.net> - 2.24-1
- bump version
- modify %%patch1

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 josef radinger <cheese@nosuchhost.net> - 2.23-2
- 2.23 fixes CVE-2020-14929 (#1850048) and new version (#1848786)

* Mon Jun 22 2020 josef radinger <cheese@nosuchhost.net> - 2.23-1
- bump version
- update patch2 alpine-2.23-gcc10.patch

* Tue Mar 24 2020 josef radinger <cheese@nosuchhost.net> - 2.22-1
- bump version

* Thu Feb 13 2020 Than Ngo <than@redhat.com> - 2.21-13
- fixed multiple definition of symbols

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Paul Wouters <pwouters@redhat.com> - 2.21-10
- Patch to suppress sending the user-agent per default

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.21-7
- new URL
- use %%license, %%make_build, %%make_install

* Tue Mar 06 2018 josef radinger <cheese@nosuchhost.net> - 2.21-6
- add Buildrequires: gcc
  https://fedoraproject.org/wiki/Packaging:C_and_C++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.21-4
- use patched features release tarball, adjust Source0 URL accordingly (#1486899)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.21-1
- alpine 2.21, update URL, .spec cosmetics

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Rex Dieter <rdieter@fedoraproject.org> 2.20-4
- workaround crash on imap login (#1282092)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Rex Dieter <rdieter@fedoraproject.org> 2.20-2
- use patched alpine sources (#1270331,#1270183)

* Mon Jul 06 2015 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 2.20-1
- Build from new upstream for 2.20, fixes rhbz#1092688 rhbz#1142890

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Rex Dieter <rdieter@fedoraproject.org> 2.11-1
- alpine-2.11, drop old/unused patches

* Thu Oct 31 2013 Rex Dieter <rdieter@fedoraproject.org> 2.10-4
- re-add README.fedora

* Sat Aug 03 2013 Dennis Gilmore <dennis@ausil.us> - 2.10-3
- remove refrences to non existant README.fedora file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Paul Wouters <pwouters@redhat.com> - 2.10-1
- Build from new upstream for 2.10, fixes rhbz#838359

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 2.03-2
- add README.fedora

* Thu Dec 20 2012 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 2.03-1
- re-alpine-2.03 (#880328,#888204)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.02-1
- re-alpine-2.02 (#465341)

* Mon Jul 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.00-9
- --with-npa=/usr/bin/inews
- --with-smtp-msa=/usr/sbin/sendmail

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.00-8
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Caolán McNamara <caolanm@redhat.com> - 2.00-6
- --with-spellcheck-prog isn't a configure option use
  --with-simple-spellcheck/--with-interactive-spellcheck and patch
  to prefer hunspell to aspell (#509387)

* Wed May 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.00-5
- "reply to all recipients" doesn't include anyone on the Cc list (#496400)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> 2.00-3
- rebuild with new openssl

* Wed Nov 26 2008 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 2.00-2
- Fix package Summary text to not include package name
- http://www.redhat.com/archives/fedora-devel-list/2008-November/msg01484.html

* Wed Aug 27 2008 Rex Dieter <rdieter@fedoraproject.org> 2.00-1
- alpine-2.00 (#460332)

* Mon Mar 24 2008 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 1.10-4
- No changes; Bump for tag system

* Mon Mar 24 2008 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 1.10-3
- No changes; Bump for tag system

* Mon Mar 24 2008 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 1.10-2
- Change License string to "ASL 2.0" instead of "Apache Software License"
- Disable debug files with "--enable-debug=no" (BZ #427013)

* Mon Mar 24 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.10-1
- alpine-1.10
- cosmetic (Build)Req cleanup

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.00-3
- Autorebuild for GCC 4.3

* Sat Dec 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.00-2
- --with-system-pinerc=%%_sysconfdir/pine.conf
  --with-system-fixed-pinerc=%%_sysconfdir/pine.conf.fixed (#426512)

* Fri Dec 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.00-1
- alpine-1.00

* Tue Dec 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.99999-4
- Bump-n-build for openldap/openssl soname changes

* Thu Nov 15 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.99999-3
- BuildRequires aspell to make configure happy

* Fri Nov 09 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.99999-2
- update to latest 

* Thu Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org. 0.9999-4
- omit sample pine.conf, instead use %%ghost to preserve existing pine.conf's

* Wed Oct 24 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9999-3
- include stock pine.conf, pine.conf.fixed

* Fri Sep 07 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.9999-2
- update to latest 

* Fri Aug 24 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.999-3
- EXTRACFLAGS=$RPM_OPT_FLAGS
- --with-c-client-target=lfd
- --with-passfile=.alpine.passfile
- Requires: mailcap

* Tue Jul 24 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.999-2.2
- remove problem cc5.sol file
- integrate changes from Patrick "Jima" Laughton <jima@beer.tclug.org>

* Tue Jul 24 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.999-2.1
- correct spec syntax, explain Conflicts tag

* Mon Jul 23 2007 Joshua Daniel Franklin <joshuadfranklin@yahoo.com> 0.999-2.0
- initial alpine spec
- Apache Software License 2.0


Name:           dumpasn1
Version:        20170309
Release:        6%{?dist}
Summary:        ASN.1 object dump utility

License:        Copyright only
#   You can use this code in whatever way you want, as long as you don't try
#   to claim you wrote it.
URL:            https://www.cs.auckland.ac.nz/~pgut001/
Source0:        https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c
Source1:        https://www.cs.auckland.ac.nz/~pgut001/dumpasn1.cfg
# man page extracted from http://ftp.debian.org/debian/pool/main/d/dumpasn1/dumpasn1_20030222-1.diff.gz
Source2:        dumpasn1.1


BuildRequires:  gcc
BuildRequires:  sed >= 3.95

%description
dumpasn1 is an ASN.1 object dump program that will dump data encoded
using any of the ASN.1 encoding rules in a variety of user-specified
formats.


%prep
%setup -q -c -T

install -pm 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} .

sed -i -e 's|/etc/dumpasn1/|%{_sysconfdir}/dumpasn1/|' dumpasn1.{c,1}

%build
# -std=c99 for fwide
%{__cc} $RPM_OPT_FLAGS -std=c99 -DDEBIAN -o dumpasn1 dumpasn1.c

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 dumpasn1 $RPM_BUILD_ROOT%{_bindir}/dumpasn1
install -Dpm 644 dumpasn1.cfg \
    $RPM_BUILD_ROOT%{_sysconfdir}/dumpasn1/dumpasn1.cfg
install -Dpm 644 dumpasn1.1 $RPM_BUILD_ROOT%{_mandir}/man1/dumpasn1.1



%files
%config(noreplace) %{_sysconfdir}/dumpasn1/
%{_bindir}/dumpasn1
%{_mandir}/man1/dumpasn1.1*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170309-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170309-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 François Kooman <fkooman@tuxed.net> - 20170309-4
- update dumpasn1.c (2018-06-11)
- update dumpasn1.cfg (2018-06-14)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170309-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170309-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 François Kooman <fkooman@tuxed.net> - 20170309-1
- update to 20170309

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170307-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170307-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 François Kooman <fkooman@tuxed.net> - 20170307-1
- update to 20170307 (file date 20170308)

* Wed Mar 01 2017 François Kooman <fkooman@tuxed.net> - 20170218-1
- update to 20170218 (file date 20170220)
- update cfg (file date 20161025)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150808-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 François Kooman <fkooman@tuxed.net> - 20150808-1
- update to 20150808 (file date 20150809)
- update cfg (file date 20150313)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141219-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 François Kooman <fkooman@tuxed.net> - 20141219-1
- update to 20141219

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 François Kooman <fkooman@tuxed.net> - 20130608-3
- fix format string vulnerability (RHBZ #1037045)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130608-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 F. Kooman <fkooman@tuxed.net> - 20130608-1
- update to 20130608
- update cfg to 20130805

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 F. Kooman <fkooman@tuxed.net> - 20130113-2
- apply patch to change BYTE to char

* Mon Jan 28 2013 F. Kooman <fkooman@tuxed.net> - 20130113-1
- update to 20130113

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120521-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 F. Kooman <fkooman@tuxed.net> - 20120521-1
- update dumpasn1 to 20120521 (Jun 08 2012 13:27)

* Thu May 17 2012 F. Kooman <fkooman@tuxed.net> - 20120501-1
- update dumpasn1 to 20120501 (May 14 2012 16:32), update config to 
  new version of 20110201 (May 14 2012 16:31)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 F. Kooman <fkooman@tuxed.net> - 20101112-1
- update to 20101112 (dumpasn1) and 20110201 (dumpasn1.cfg) 

* Fri Aug 20 2010 Adam Tkac <atkac redhat com> - 20100318-2
- rebuild to ensure F14 has higher NVR than F13

* Fri Jun 11 2010 François Kooman <fkooman@tuxed.net> - 20100318-1
- new upstream version
- restore patch to fix undefined BYTE

* Sat May 8 2010  François Kooman <fkooman@tuxed.net> - 20090721-2
- upstream updated source files in place at 20100312 without
  updating version mentioned in the files themselves

* Sun Sep 13 2009 François Kooman <fkooman@tuxed.net> - 20090721-1
- update to upstream version 20090721

* Tue Aug 11 2009 François Kooman <fkooman@tuxed.net> - 20090318-4
- upstream changed source file in place, update
- remove patch which is no longer required

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090318-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 François Kooman <fkooman@tuxed.net> - 20090318-2
- cfg file already has unix line endings
- create patch instead of using sed to replace BYTE with char
 
* Thu Jul 16 2009 François Kooman <fkooman@tuxed.net> - 20090318-1
- Update to 20090318 and config to 20090531

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Ville Skyttä <ville.skytta at iki.fi> - 20090107-1
- Update to 20090107 and config to 20090125.

* Sat Aug  2 2008 Ville Skyttä <ville.skytta at iki.fi> - 20080414-2
- Update to 20080708 updated sources (upstream version unchanged).
- Drop Debian patchset, just include man page from it separately.

* Fri May  2 2008 Ville Skyttä <ville.skytta at iki.fi> - 20080414-1
- Update to 20080414.

* Sun Mar 30 2008 Ville Skyttä <ville.skytta at iki.fi> - 20080204-2
- Fix implicit function declarations.
- Update dumpasn1.cfg to 20080323.

* Sat Feb  9 2008 Ville Skyttä <ville.skytta at iki.fi> - 20080204-1
- 20080204.

* Thu Aug 16 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060622-3
- License: Copyright only

* Thu Feb  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060622-2
- Update dumpasn1.cfg to 20070127.

* Tue Aug 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060622-1
- Update to 20060622.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050404-2
- Rebuild.

* Mon Aug 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050404-1
- Use macros more consistently (#165497).

* Tue Aug  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050404-0.1
- Update to 20050404.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 20030222-0.1
- Rebuild for FC4.

* Mon Aug 30 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:20030222-0.fdr.1
- First build, based on Debian package.

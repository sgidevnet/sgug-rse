#
# pidgin_major_ver and pidgin_minor_ver should be defined to match the minimum
# Pidgin API version _required_ to build Guifications
# Due to the way Pidgin checks plugin versions, we need to also ensure that
# the correct minimum version of Pidgin is Require:'d based on what version of
# the Pidgin headers we actually build with.
#
%define pidgin_major_ver 2
%define pidgin_minor_ver 0
%define pidgin_next_major_ver %(echo $((%{pidgin_major_ver}+1)))
%define pidgin_build_minor_ver %(pkg-config --modversion pidgin | awk -F. '{ print $2 }')

Summary:    Guifications Plugin for Pidgin
Name:       pidgin-guifications
Version:    2.16
Release:    21%{?dist}
License:    GPLv2+
Url:        http://plugins.guifications.org/trac/wiki/Guifications
Source:     http://downloads.guifications.org/plugins/Guifications2/pidgin-guifications-%{version}.tar.bz2
Patch0:     pidgin-guifications-2.14-stdc.patch

BuildRequires:  libtool, gtk2-devel, gettext
BuildRequires:  pidgin-devel >= %{pidgin_major_ver}.%{pidgin_minor_ver}
BuildRequires:  perl(XML::Parser)
BuildRequires:  autoconf, automake, libtool, intltool
Requires:       pidgin >= %{pidgin_major_ver}.%{pidgin_build_minor_ver}

Provides:   gaim-guifications = %{version}-%{release}
Obsoletes:  gaim-guifications < 2.14

%description
Guifications is a graphical notification plugin for the open source 
instant messaging client Pidgin.

%prep

%setup -q
%patch0 -p1 -b .stdc

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la $RPM_BUILD_ROOT%{_libdir}/pidgin/*.a

%find_lang guifications

%files -f guifications.lang
%doc AUTHORS ChangeLog COPYING README doc/flow.png doc/flow.dia doc/QUOTES
%{_libdir}/pidgin/*.so
%{_datadir}/pixmaps/pidgin/guifications

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.16-6
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Stu Tomlinson <stu@nosnilmot.com> 2.16-2
- Fix building with libtool 2.2

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.16-1
- update to 2.16
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.14-4
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Stu Tomlinson <stu@nosnilmot.com> 2.14-3
- Don't force use of strict ISO C99 compiler, fixes building with gcc 4.3

* Fri May 18 2007 Stu Tomlinson <stu@nosnilmot.com> 2.14-2
- New upstream release
- Works with Pidgin
- Obsoletes/Provides gaim-guifications

* Thu Jan 25 2007 Radek Vokál <rvokal@redhat.com> 2.13-0.6.beta6
- update to beta6 package

* Mon Jan 22 2007 Radek Vokál <rvokal@redhat.com> 2.13-0.5.beta5
- rebuilt

* Sat Dec 09 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 2.13-0.4.beta5
- add BR perl(XML::Parser)

* Sat Dec 09 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 2.13-0.3.beta5
- apply patch from Gen Zhang 2.13-0.3.beta5 in #212742 that updates to beta5:
 - bump
 - make the language build work
- Update URL/Source0

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.13-0.3.beta3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 2.13-0.2.beta3
- keep this guy alive, bump to 2.13 beta3

* Wed Mar 15 2006 Radek Vokál <rvokal@redhat.com> - 2.12-3
- rebuild

* Thu Aug 18 2005 Jeremy Katz <katzj@redhat.com> - 2.12-2
- rebuild for new cairo

* Thu Aug 4 2005 Colin Charles <colin@fedoraproject.org> 2.12-1
- bump to new upstream release

* Tue Jun 28 2005 Colin Charles <colin@fedoraproject.org> 2.10-4
- remove redundant CFLAGS in %%configure (Ralf)

* Mon Jun 27 2005 Colin Charles <colin@fedoraproject.org> 2.10-3
- remove BuildRequires on pkgconfig; brought in by gtk2-devel

* Sat Jun 25 2005 Colin Charles <colin@fedoraproject.org> 2.10-2
- changed from tar.gz to tar.bz2 for file size reduction
- fix rpmlint description-line-too-long, as well as download URL

* Sat Jun 25 2005 Colin Charles <colin@fedoraproject.org> 2.10-1
- initial FE build, with preferred BuildRoot

* Sat Apr  9 2005 Stu Tomlinson <stu@nosnilmot.com>
- spec file cleanup

* Fri Dec 17 2004 Stu Tomlinson <stu@nosnilmot.com>
- Tweaks to the Gaim version dependencies

* Sat Oct  9 2004 Stu Tomlinson <stu@nosnilmot.com>
- Add Gaim version checks to match new Gaim versioning

* Wed Jun 30 2004 Stu Tomlinson <stu@nosnilmot.com>
- Initial spec file for Guifications 2

# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: A lightweight multi-tabbed terminal emulator for X
Name: mrxvt 
Version: 0.5.4
Release: 26%{?dist} 
URL: http://materm.sourceforge.net/wiki/Main/HomePage
License: GPLv2+
BuildRequires:  gcc
#BuildRequires: imake pkgconfig ncurses-devel libXft-devel libXaw-devel libXext-devel desktop-file-utils 
BuildRequires: pkgconfig ncurses-devel
#BuildRequires: libpng-devel libjpeg-devel libutempter-devel 
BuildRequires: libpng-devel libjpeg-devel

Source0: http://downloads.sourceforge.net/materm/%{name}-%{version}.tar.gz
#Source1: http://littlehat.homelinux.org:8000/FEDORA/mrxvt/current/0.5.3/%{name}.desktop

#Patch1: http://downloads.sourceforge.net/materm/no-scroll-with-buffer-mrxvt-0.5.3.patch
Patch2: mrxvt.sgifixes.patch

%description
Mrxvt (previously materm) is based on 2.7.11 CVS of rxvt and aterm.

%prep

%setup -q 
#%patch1 -p0 -b .no-scroll-with-buffer-mrxvt-0.5.3
%patch2 -p1
sed -i 's|\r||' share/scripts/mrxvt.vbs

%build

#configure \
#           --enable-everything \
#           --disable-debug
# mrxvt & the config cache aren't happy together
unset CONFIG_SITE
%configure \
           --enable-sgi-scroll \
           --with-tab-radius=0

make %{?_smp_mflags}

%install

rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" install 

#desktop-file-install \
#%if 0%{?fedora} && 0%{?fedora} < 19
#        --vendor=fedora \
#%endif
#        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
#        %{SOURCE1}

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%files 
%doc doc/README* doc/*.txt*
%doc share/scripts/
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/mrxvt
%{_mandir}/man1/mrxvt.1*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/mrxvt/default.menu
%config(noreplace) %{_sysconfdir}/mrxvt/mrxvtrc
%config(noreplace) %{_sysconfdir}/mrxvt/mrxvtrc.sample
%config(noreplace) %{_sysconfdir}/mrxvt/submenus.menu
#%if 0%{?fedora} && 0%{?fedora} < 19
#%{_datadir}/applications/fedora-mrxvt.desktop
#%else
#%{_datadir}/applications/mrxvt.desktop
#%endif
%{_datadir}/pixmaps/%{name}*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.3- 13 
- remove --vendor from desktop-file-install on F19+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.5.3-11
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.5.3-10
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.3-7
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5.3-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.3-2
- Autorebuild for GCC 4.3

* Tue Nov 27 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.3-1
- Fixing SRPM build problem that was created by improper import.

* Tue Nov 27 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.3-0
- New version release for Fedora 8.
- New version of mrxvt with scroll patch.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.5.2-10
- Rebuild for selinux ppc32 issue.

* Mon Jun 18 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-9
- Removed extraneous build comments.
- Modified "end-of-line" fix to fit one line after patch1.
- Fixed comment for 0.5.2-6 

* Mon Jun 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.2-8
- Clean up %%prep stage

* Sat Jun 16 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-7 
- Removed Version entry from desktop file.

* Sun Jun 10 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-6 
- Fixed "end-of-line" encoding error with sed replacement
- Fixed release tag

* Mon Jun 4 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-5
- Remove all files under datadir/doc/name
- Add proper document link
- Remove INSTALL file
- Timestamp unmodified text/images

* Mon Jun 4 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-4
- Updated spec file per suggestions in bug #: 223422
- Fixed changelog
- Fixed sourceURL per sf.net rules
- Added parallel make
- Removed root owernship of executable
- Added directory ownership
- Removed unnecesary macros
- Added noreplace

* Sun Jun 3 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-3
- Implemented review guidelines 

* Thu May 31 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-2
- Implemented naming guidelines 

* Tue Jan 16 2007 Adam M. Dutko <gnome at dux-linux org> - 0.5.2-1
- Added X patch

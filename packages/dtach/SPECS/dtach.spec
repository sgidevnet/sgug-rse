Summary: A simple program that emulates the detach feature of screen
Name: dtach
Version: 0.9
Release: 8%{?dist}
License: GPLv2+
URL: http://dtach.sourceforge.net
Source: http://prdownloads.sourceforge.net/dtach/dtach-%{version}.tar.gz

BuildRequires:  gcc
%description

dtach is a program that emulates the detach feature of screen, with
less overhead.  It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 dtach $RPM_BUILD_ROOT/%{_bindir}/dtach
install -m 644 dtach.1 $RPM_BUILD_ROOT/%{_mandir}/man1/dtach.1

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/dtach
%{_mandir}/*/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Lon Hohberger <lon@redhat.com> - 0.9-1
- Rebase to 0.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Lon Hohberger <lhh@redhat.com> - 0.8-9
- Properly handle closes.  Patch from Luk Claes <luk at debian dot org>
- Resolves: rhbz#835853

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Lon Hohberger <lon@fedoraproject.org> - 0.8-4
- Update spec file to include dist tag in package revision

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 28 2008 Lon Hohberger <lhh@redhat.com> - 0.8-1
- New upstream version 0.8 of dtach

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7-3
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7-2.2.3
- Autorebuild for GCC 4.3

* Sat Feb 03 2007 Jef Spaleta <jspaleta@gmail.com> - 0.7-1.2.3
- Specfile clean up for merge review

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.7-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Mar 14 2005 Lon Hohberger <lhh@redhat.com>
- Upgrade to 0.7

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.5.3
- Rebuild in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec  3 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.5-1
- 0.5

* Fri Nov 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.4-1
- s/Copyright/License/
- Minor description change
- fix use of %%doc
- Add full location of source tarball

* Sat Nov 03 2001 Ned T. Crigler <crigler@hell-city.org> 0.4
- Portability updates thanks to sourceforge's compile farm. dtach should now
  work on: FreeBSD, Debian/alpha, Debian/PPC, Debian/sparc, Debian/PPC, and
  Solaris.

* Thu Sep 27 2001 Ned T. Crigler <crigler@hell-city.org>
- Modified spec file URL: to point to http://dtach.sourceforge.net

* Wed Sep 26 2001 Ned T. Crigler <crigler@hell-city.org> 0.3
- Use getrlimit and dynamically allocate the data structures, if possible.
- Added some more autoconf checks.
- Initial sourceforge release.

* Thu Sep 20 2001 Ned T. Crigler <crigler@hell-city.org>
- Changed the master to send a stream of text to attaching clients instead
  of sending a huge packet all the time.
- Decreased the client <-> master packet size.
- Changed the attach code so that it tells the master when a suspend occurs.

* Tue Sep 18 2001 Ned T. Crigler <crigler@hell-city.org>
- Fixed a typo in dtach.1

* Tue Sep 18 2001 Ned T. Crigler <crigler@hell-city.org> 0.2
- Removed silly thinko regarding terminal settings in attach, we
  always set the terminal to raw mode now.
- Moved redraw code into the master, which tries to be smarter when
  using ^L.
- Moved the code that obtains the current terminal settings into main,
  preventing a race condition between the master and attach processes.
- Rewrote argument parsing code.
- Changed name to dtach.
- Added a man page.

* Mon Sep 17 2001 Ned T. Crigler <crigler@hell-city.org>
- Changed fchmod to chmod in create_socket.

* Mon Sep 17 2001 Isaiah Weiner <iweiner@redhat.com>
- Modified spec file to correct detach binary permissions
- Modified spec file to correct detach documentation path
- Modified spec file URL: to point to http://people.redhat.com/iweiner/detach
- Modified spec file clean section to remove buildroot and builddir.

* Mon Sep 17 2001 Ned T. Crigler <crigler@hell-city.org> 0.1
- Initial rpm release.

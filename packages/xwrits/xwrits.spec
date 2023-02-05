Summary: Reminds you take wrist breaks

Name: xwrits
Version: 2.26
Release: 16%{?dist}
Source: http://www.lcdf.org/xwrits/xwrits-%{version}.tar.gz
Source2: xwrits.png
Source3: xwrits.desktop

URL: http://www.lcdf.org/xwrits/

License: GPLv2
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libXt-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel

%description
Xwrits reminds you to take wrist breaks, which
should help you prevent or manage a repetitive
stress injury. It pops up an X window when you
should rest; you click on that window, then take a
break.

Xwrits's graphics are brightly colored pictures of
a wrist and the attached hand. The wrist clenches
and stretches ``as if in pain'' when you should
rest, slumps relaxed during the break, and points
forward valiantly when the break is over. It is
trapped behind bars while the keyboard is locked.
Other gestures are included.

Extensive command line options let you control how
often xwrits appears. It can escalate its behavior
over time -- by putting up more flashing windows
or actually locking you out of the keyboard, for
example -- which makes it harder to cheat.

%prep
%setup -q

%build
CFLAGS="${RPM_OPT_FLAGS}" ./configure --prefix=${RPM_BUILD_ROOT}%{_prefix} --libdir=${RPM_BUILD_ROOT}%{_libdir} --mandir=${RPM_BUILD_ROOT}%{_mandir}
make %{?_smp_mflags}

%install
make install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
cp -p %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
desktop-file-install                            \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --add-category X-Fedora                                 \
        %{SOURCE3}

%files
%doc NEWS README GESTURES TODO
%{_bindir}/xwrits
%{_mandir}/man1/*
%{_datadir}/pixmaps/xwrits.png
%{_datadir}/applications/xwrits.desktop

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.26-4
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Jeff Layton <jlayton@redhat.com> 2.26-1
- update to new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.24-4
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.24-3
- Autorebuild for GCC 4.3

* Tue Sep 12 2006 Jeff Layton <jlayton@redhat.com> 2.24-2
- rebuild for FC6

* Sun Jul 16 2006 Jeff Layton <jlayton@redhat.com> 2.24-1
- new upstream rev

* Thu Jun 29 2006 Jeff Layton <jlayton@redhat.com> 2.23-1
- new upstream rev
- fix problems with mwm_hints data sizes on x86_64 [BZ 197168]

* Fri Jun 23 2006 Jeff Layton <jlayton@redhat.com> 2.22-3
- spec changes per rpmlint and Kevin Fenzi's recommendations

* Sun Jun 11 2006 Jeff Layton <jlayton@redhat.com> 2.22-2
- bump release number

* Sun May 28 2006 Jeff Layton <jlayton@redhat.com> 2.22-1
- first packaging for Fedora Extras


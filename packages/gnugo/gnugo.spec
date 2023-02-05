Name:           gnugo
Version:        3.8
Release:        21%{?dist}

Summary:        Text based go program

License:        GPLv3+
URL:            http://www.gnu.org/software/gnugo/gnugo.html
Source0:        http://ftp.gnu.org/gnu/gnugo/gnugo-%{version}.tar.gz
Patch0:         gnugo-3.8-format-security.patch

BuildRequires:  gcc
BuildRequires:  ncurses-devel readline-devel
BuildRequires:  texinfo
Requires(post): info
Requires(preun): info


%description
This software is a free program that plays the game of Go. GNU Go has played
thousands of games on the NNGS Go server. GNU Go is now also playing regularly
on the Legend Go Server in Taiwan and the WING server in Japan.


%prep
%setup -q
%patch0 -p1
# convert docs to UTF-8
for f in AUTHORS THANKS; do
  iconv -f iso8859-1 -t utf-8 $f > $f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done


%build
%configure --enable-color --with-readline
make %{?_smp_mflags}


%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO THANKS doc/newlogo.jpg doc/oldlogo.jpg
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_infodir}/gnugo.*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.8-20
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.8-13
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.8-9
- Fix FTBFS with -Werror=format-security (#1037096, #1106693)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Michel Salim <salimma@fedoraproject.org> - 3.8-1
- Update to 3.8
- License is now GPLv3+
- Enable readline support

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.6-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.6-6
- Autorebuild for GCC 4.3

* Mon Oct  9 2006 Michel Salim <michel.salim@gmail.com> 3.6-5
- Rebuild for FE6

* Wed Mar  1 2006 Chris Ricker <kaboom@oobleck.net> 3.6-4
- rebuild for FE 5
- add dist tag

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 14 2005 David Woodhouse <dwmw2@infradead.org> - 3.4-2
- Remove unpackaged %%{_infodir}/dir which breaks build

* Sat Nov 27 2004 Phillip Compton <pcompton at proteinmedia dot com> - 3.4-1
- 3.6.

* Thu Nov 11 2004 Phillip Compton <pcompton at proteinmedia dot com> - 3.4-0.fdr.3
- Clean up spec/Bump release.

* Tue Aug 05 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.4-0.fdr.2
- Added logos to %%doc.

* Sat Aug 02 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.4-0.fdr.1
- Updated to 3.4.

* Fri Jul 18 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.23-0.fdr.1
- Updated to 3.3.23.

* Mon Jul 14 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.22-0.fdr.2
- post/preun require texinfo -> info.
- fix in preun script.

* Mon Jul 07 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.22-0.fdr.1
- Updated to 3.3.22.

* Thu Jun 19 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.21-0.fdr.2
- Corrected changelog typo.

* Sat Jun 14 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.21-0.fdr.1
- Updated to 3.3.21.

* Wed Jun 04 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.20-0.fdr.1
- Updated to 3.3.20.

* Thu May 08 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.19-0.fdr.2
- Applied patch from Adrian.
- Removed INSTALL from docs.
- Replaced buildroot with RPM_BUILD_ROOT.

* Tue Apr 29 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.19-0.fdr.1
- Updated to 3.3.19

* Sun Apr 27 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.18-0.fdr.2
- Removed hard coded paths.
- Added ncurses-devel as BuildRequires.
- Fixed Group.

* Fri Apr 25 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.18-0.fdr.1
- Updated to 3.3.18.

* Fri Apr 18 2003 Phillip Compton <pcompton at proteinmedia dot com> - 0:3.3.14-0.fdr.1
- Fedorafied

* Thu Aug 22 2002 Kevin Sonney <ksonney@redhat.com> 3.3.14-1
- Version bump

* Thu Aug 22 2002 Kevin Sonney <ksonney@redhat.com> 3.2-0.1
- Initial Spec File


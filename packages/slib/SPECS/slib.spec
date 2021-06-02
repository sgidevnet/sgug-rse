Summary:      Platform independent library for scheme
Name:         slib
Version:      3b5
Release:      10%{?dist}
License:      SLIB
BuildArch:    noarch
Source0:      http://swiss.csail.mit.edu/ftpdir/scm/slib-%{version}.zip
URL:          http://swissnet.ai.mit.edu/~jaffer/SLIB.html

# Fix guile2 support
Patch1:       slib-guile2.patch

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accommodate packages specific to a site,
implementation, user, or directory.

%prep
%setup -q -n %{name}
%patch1 -p1 -b .guile2
sed -r -i "s,/usr/(local/)?lib/slib,%{_datadir}/slib,g" *.init

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/slib
cp *.scm *.init *.xyz *.txt *.dat *.ps ${RPM_BUILD_ROOT}%{_datadir}/slib
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
install -m644 slib.info $RPM_BUILD_ROOT%{_infodir}

%files
%dir %{_datadir}/slib
%doc ANNOUNCE README COPYING FAQ ChangeLog
%{_datadir}/slib/*
%{_infodir}/slib.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Miroslav Lichvar <mlichvar@redhat.com> 3b5-7
- drop obsolete install-info scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3b5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Miroslav Lichvar <mlichvar@redhat.com> 3b5-1
- update to 3b5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Miroslav Lichvar <mlichvar@redhat.com> 3b4-3
- fix guile2 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Miroslav Lichvar <mlichvar@redhat.com> 3b4-1
- update to 3b4
- remove obsolete macros

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Miroslav Lichvar <mlichvar@redhat.com> 3b3-1
- update to 3b3

* Tue Aug 11 2009 Miroslav Lichvar <mlichvar@redhat.com> 3b2-1
- update to 3b2
- suppress install-info errors

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3b1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Miroslav Lichvar <mlichvar@redhat.com> 3b1-1
- update to 3b1

* Wed Jan 09 2008 Miroslav Lichvar <mlichvar@redhat.com> 3a5-1
- update to 3a5
- replace slib paths only in .init files

* Fri Jun 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 3a4-2
- fix summary and buildroot (#226421)

* Tue Jan 23 2007 Miroslav Lichvar <mlichvar@redhat.com> 3a4-1
- update to 3a4
- make scriptlets safer (#223717)

* Wed Jul 12 2006 Miroslav Lichvar <mlichvar@redhat.com> 3a3-2
- fix requires for install-info
- drop slibcat, include *.dat and grapheps.ps files

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3a3-1.1
- rebuild

* Tue May 09 2006 Miroslav Lichvar <mlichvar@redhat.com> 3a3-1
- update to slib3a3
- install info, remove html
- fix typo in description (#189650)

* Mon Feb 27 2006 Miroslav Lichvar <mlichvar@redhat.com> 3a1-6
- spec cleanup

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Sep  8 2005 Jindrich Novy <jnovy@redhat.com> 3a1-5
- regenerate slibcat to remove all links to umb-scheme
  to make gnucash work with slib
- don't ship slib.spec from the upstream tarball
- replace bogus links to /usr/lib
- don't ship unneeded files in slib directory
- add slib html documentation

* Thu Sep 08 2005 Florian La Roche <laroche@redhat.com> 3a1-4
- no need to provide slib for this package

* Tue Sep  6 2005 Jindrich Novy <jnovy@redhat.com> 3a1-3
- use _datadir instead of /usr/local/lib and don't use
  /usr/local prefix (#167490)

* Wed Dec  8 2004 Jindrich Novy <jnovy@redhat.com> 3a1-2
- remove symlinks creation for guile, it's done by guile itself

* Wed Oct  6 2004 Jindrich Novy <jnovy@redhat.com> 3a1-1
- new package
- original spec file from R. J. Meier and Radey Shouman

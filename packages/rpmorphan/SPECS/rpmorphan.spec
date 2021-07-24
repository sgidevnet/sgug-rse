Summary:          List packages that have no dependencies (like deborphan)
Name:             rpmorphan
Version:          1.17
Release:          8%{?dist}
License:          GPLv2+

BuildArch:        noarch

URL:              http://rpmorphan.sourceforge.net

# Note upstream have the habit of releasing updated tarballs which
# have the same version number (happened with 1.12).
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch100:		  rpmorphan.sgifixes.patch

BuildRequires:    /usr/sgug/bin/pod2man
BuildRequires:    perl-generators

#Requires:         perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
#Requires:         perl(Curses::UI)
#Requires:         logrotate
#Requires:         perl-Tk



%description
rpmorphan finds "orphaned"[1] packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages.  It intends to be clone of
deborphan Debian tools for rpm packages.

It will try to help you to remove unused packages, for example:
* after a distribution upgrade
* when you want to suppress packages after some tests

Several tools are also provided :
* rpmusage - display rpm packages last use date
* rpmdep - display the full dependency of an installed rpm package
* rpmduplicates - find programs with several version installed

Yum offers a program called 'package-cleanup' which you can use to
carry out similar tasks.

[1] Note that orphan is used in the sense of Debian's deborphan, and
is NOT the same as Fedora orphaned packages which are packages that
have no current maintainer.


%prep
%setup -q
%patch100 -p1 -b .sgifixes
sed -i -e "s|/usr/lib|/usr/sgug/share|g" rpm*

%build
# Nothing needed here.


%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 0644 rpmorphan.logrotate $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/rpmorphan
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT/usr/sgug/lib/%{name}/* $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -f $RPM_BUILD_ROOT/var/log/rpmorphan.log


%files
%doc rpmorphan.lsm Authors COPYING Changelog NEWS Todo Readme rpmorphanrc.sample
%{_bindir}/grpmorphan
%{_bindir}/rpmextra
%{_bindir}/rpmextra.pl
%{_bindir}/rpmorphan.pl
%{_bindir}/rpmorphan
%{_bindir}/rpmusage.pl
%{_bindir}/rpmusage
%{_bindir}/rpmdep.pl
%{_bindir}/rpmdep
%{_bindir}/rpmduplicates.pl
%{_bindir}/rpmduplicates
#%ghost %config(noreplace) %{_localstatedir}/log/rpmorphan.log
%dir %{_localstatedir}/lib/rpmorphan
%attr(644, root, root)%{_localstatedir}/lib/rpmorphan/keep
%config(noreplace) %{_sysconfdir}/logrotate.d/rpmorphan
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/rpmorphanrc
%{_mandir}/man1/rpmextra.1*
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%{_mandir}/man1/rpmdep.1*
%{_mandir}/man1/rpmduplicates.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.17-1
- New upstream version 1.17 (RHBZ#1471378).

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-2
- Perl 5.24 rebuild

* Tue Apr 26 2016 Dave Johansen <davejohansen@gmail.com> - 1.16-1
- Upstream released 1.16

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 "D. Johnson" <fenris02@fedoraproject.org> - 1.15-1
- Upstream released 1.15

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-6
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.12-4
- New upstream version.
  NOTE: It has the same version number, upstream did not increment it!
- Remove patch; the code is fixed upstream, albeit in a different way.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Orion Poplawski <orion@cora.nwra.com> - 1.12-1
- Update to 1.12
- Add patch for bug 880603
- spec cleanup

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.11-4
- Perl 5.18 rebuild

* Mon Feb 18 2013 Richard W.M. Jones <rjones@redhat.com> - 1.11-3
- +BR pod2man.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Adam Miller <maxamillion@fedoraproject.org> - 1.11-1
- Update to latest upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.10-3
- Perl 5.16 rebuild

* Wed Feb 1 2012 Alexander Kurtakov <akurtako@redhat.com> 1.10-2
- Patch to have localizations in _datadir instead of /usr/lib.

* Wed Feb 1 2012 Alexander Kurtakov <akurtako@redhat.com> 1.10-1
- Update to latest upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.7-6
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.7-5
- Perl 5.14 mass rebuild


* Fri Mar 04 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7-4
- Added missing perl module dependency
- Resolves rhbz#600136
- Update spec to match current guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.7-2
- Mass rebuild with perl-5.12.0

* Wed Mar  3 2010 Richard W.M. Jones <rjones@redhat.com> - 1.7-1
- New upstream version 1.7 (RHBZ#566907).
- New programs (rpmorphan-curses-lib.pl and rpmorphan-tk-lib.pl).
- %%build section was incorrect.  The 'make all' and 'make install'
  rules do the same thing, so 'make' in %%build section is unnecessary.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.4-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Richard W.M. Jones <rjones@redhat.com> - 1.4-5
- Clarify the documentation, usage of 'orphan' and other terminology.

* Wed Mar 25 2009 Richard W.M. Jones <rjones@redhat.com> - 1.4-4
- Combine all %%doc lines into one.
- Remove Makefile from %%doc section.
- Use %%{?_smp_mflags}.

* Wed Mar 25 2009 Richard W.M. Jones <rjones@redhat.com> - 1.4-3
- Missing Requires perl-Tk (Leigh Scott).
- Added %%{?dist} to Release.

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.4-2
- Initial build for Fedora.

* Mon Jan 05 2009 <gerbier@users.sourceforge.net> 1.4-1
- improve diagnostic if "rpm -e" return some comments

* Mon Oct 20 2008 <gerbier@users.sourceforge.net> 1.3-1
- fix a bug if exclude are set in config file (thanks Szymon Siwek)
- display number of deleted file

* Mon Apr 7 2008 <gerbier@users.sourceforge.net> 1.2-1
- write log to /var/log/rpmorphan.log
- add rpmdep.pl tool
- add rpmduplicate.pl tool

* Thu Nov 22 2007 <gerbier@users.sourceforge.net> 1.1-1
- (rpmorphan) add a default target : guess-lib
- (rpmorphan) test rpm delete
- fix warnings from perlcritic tool
- (rpmorphan) split too complex code (add read_one_rc, init_cache)
- (rpmorphan) add keep-file option, which allow to cutomize the keep file
- add rpmorphan-lib.pl to store common code for rpmorphan, rpmusage
- (rpmusage) add a default target : all
- use rpmlint to build a better rpm package

* Fri Apr 27 2007 <gerbier@users.sourceforge.net> 1.0
- fix bug with tk : core dump because update call before mainloop
- add w_ prefix for widgets variables
- add dry-run (simulation) mode
- (gui) add 3 counters : packages, orphans, selected
- (gui) display_status call debug sub
- new Liste_pac global variable
- (gui) change curses geometry to work on console
- (gui) recursive analysis
- improve virtuals : now check if how many package provide this one

* Wed Mar 28 2007 <gerbier@users.sourceforge.net> 0.9
- add curses interface
- test for root access before removing packages
- add optionnal configuration file
- recode debugging system
- apply conway coding rules
- add tk_get_current_elem sub
- add get_from_command_line sub
- add status widget

* Tue Mar 06 2007 <gerbier@users.sourceforge.net> 0.8
- add simple graphical user iinterface (optionnal)
- remove global variable opt_verbose
- split code in functions : access_time_filter, read_rpm_data, search_orphans

* Wed Feb 28 2007  <gerbier@users.sourceforge.net> 0.4
- add optionnal cache

* Sat Feb 03 2007  <gerbier@users.sourceforge.net> 0.3
- add rpmusage tool
- add a link from rpmorphan.pl to rpmorphan

* Tue Jan 30 2007  <gerbier@users.sourceforge.net> 0.2
- add permanent exclude list

* Tue Jan 23 2007  <gerbier@users.sourceforge.net> 0.1
- Initial spec file 

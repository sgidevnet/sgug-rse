Name:           imapfilter
Version:        2.6.12
Release:        2%{?dist}
Summary:        A flexible client side mail filtering utility for IMAP servers

License:        MIT
URL:            https://github.com/lefcha/imapfilter/
Source0:        https://github.com/lefcha/imapfilter/archive/v%{version}.tar.gz
Patch0:         imapfilter-makefile-fix.patch

BuildRequires:  gcc
BuildRequires:  openssl-devel lua-devel pcre-devel

%description
IMAPFilter is a mail filtering utility. It connects to remote mail servers
using the Internet Message Access Protocol (IMAP), sends searching queries
to the server and processes mailboxes based on the results. It can be used
to delete, copy, move, flag, etc. messages residing in mailboxes at the
same or different mail servers. The 4rev1 and 4 versions of the IMAP
protocol are supported.


%prep
%autosetup -p1 -n imapfilter-%{version}

%build
# imapfilter does not have any autotools based ./configure - just a plain Makefile
CFLAGS=$RPM_OPT_FLAGS make PREFIX=%{_prefix} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT


%files
%doc README LICENSE
%{_bindir}/imapfilter
%{_datadir}/imapfilter/
%{_mandir}/man1/imapfilter.1.gz
%{_mandir}/man5/imapfilter_config.5.gz


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Andrea Veri <averi@fedoraproject.org> - 2.6.12-1
- New upstream release. (This release introduces SNI support, fixes
  RH BZ #1713160)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Matěj Cepl <mcepl@redhat.com> - 2.6.10-2
- add PREFIX to %%build make as well

* Thu Aug 03 2017 Matěj Cepl <mcepl@redhat.com> - 2.6.10-1
- Update to the latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 24 2013 Andrea Veri <averi@fedoraproject.org> - 2.5.6-1
- New upstream release.
- Make use of the patch file available on the git repository itself,
  update Patch0 accordingly.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 David Sommerseth <davids@redhat.com> - 2.5.5-1
- Updated to upstream imapfilter-2.5.5
- Updated download URL and generally cleaned up spec file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 David Sommerseth <davids@redhat.com> - 2.5-1
- Updated to latest upstream version
- Replaced the configure patch with a makefile patch, as upstream has changed their building methods

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.2.2-4
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 25 2010 David Sommerseth <davids@redhat.com> - 2.2.2-1
- Updated to latest upstream version

* Tue Oct 13 2009 David Sommerseth <davids@redhat.com> - 2.0.11-3
- Apply patch overriding -O optimisation and removed not needed install lines

* Thu Sep 24 2009 David Sommerseth <davids@redhat.com> - 2.0.11-2
- Use $RPM_OPT_FLAGS as CFLAGS

* Wed Sep 23 2009 David Sommerseth <davids@redhat.com> - 2.0.11-1
- Updated to imapfilter-2.0.11 and more clean up in spec rules

* Mon Aug 10 2009 David Sommerseth <davids@redhat.com> - 2.0.10-2
- Cleaned up the spec rules

* Thu Aug  6 2009 David Sommerseth <davids@redhat.com> - 2.0.10-1
- First cut at spec file for imapfilter


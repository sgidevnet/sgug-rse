Summary:	PostgreSQL monitoring script
Name:		check_postgres
Version:	2.24.0
Release:	3%{?dist}
License:	BSD
Source0:	https://bucardo.org/downloads/%{version}.tar.gz
URL:		https://bucardo.org/wiki/Check_postgres
BuildArch:	noarch
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-generators

%description
check_postgres.pl is a script for checking the state of one or more
Postgres databases and reporting back in a Nagios-friendly manner. It is
also used for MRTG.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/auto/check_postgres/.packlist
%{__rm} -f %{buildroot}%{_libdir}/perl5/perllocal.pod

%files
%doc %{name}.pl.html README.md TODO
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}.pl

%changelog
* Fri Aug 9 2019 Devrim Gündüz <devrim@gunduz.org> - 2.24.0-3
- Attempt to fix FTBFS, and also use more macros.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Devrim Gündüz <devrim@gunduz.org> - 2.24.0-1
- Update to 2.24.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 03 2016 Devrim Gündüz <devrim@gunduz.org> - 2.22.0-1
- Update to 2.22.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 Devrim Gündüz <devrim@gunduz.org> - 2.21.0-1
- Update to 2.21.0
- Simplify spec file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 - Devrim GUNDUZ <devrim@gunduz.org> 2.20.1-1
- Update to 2.20.1, per changes described at
  https://mail.endcrypt.com/pipermail/check_postgres-announce/2013-June/000033.html

* Thu Aug  8 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.19.0-6
- Fix FTBFS with unversioned %%{_docdir_fmt} (#992052).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.19.0-4
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 - Devrim GUNDUZ <devrim@gunduz.org> 2.19.0-1
- Update to 2.19.0, per changes described at
  https://mail.endcrypt.com/pipermail/check_postgres-announce/2012-January/000028.html

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 3 2011 - Devrim GUNDUZ <devrim@gunduz.org> 2.18.0-1
- Update to 2.18.0, per changes described at
  https://mail.endcrypt.com/pipermail/check_postgres-announce/2011-October/000027.html

* Tue Feb 15 2011 - Devrim GUNDUZ <devrim@gunduz.org> 2.16.0-1
- Update to 2.16.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 10 2010 - Devrim GUNDUZ <devrim@gunduz.org> 2.14.3-1
- Update to 2.14.3

* Sat Feb 27 2010 - Devrim GUNDUZ <devrim@gunduz.org> 2.14.2-1
- Update to 2.14.2
- Add -p options to install, per bz review #543917, comment #3.
- Remove postgresql-server requirement, since this plugin can be used to
  control remote PostgreSQL servers.

* Mon Feb 1 2010 - Devrim GUNDUZ <devrim@commandprompt.com> 2.13.0-1
- Update to 2.13.0
- Refactor spec file:
  * Use tarball, instead of .pl file directly.
  * Add man page

* Wed Sep 2 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.12.0-1
- Update to 2.12.0

* Wed Sep 2 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.11.1-1
- Update to 2.11.1

* Tue Aug 4 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.9.10-1
- Update to 2.9.10

* Tue Jul 28 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.9.2-1
- Update to 2.9.2

* Sat Jul 4 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.9.1-1
- Update to 2.9.1

* Mon May 18 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.8.1-1
- Update to 2.8.1

* Thu May 7 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.8.0-1
- Update to 2.8.0

* Tue Feb 17 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.7.3-1
- Update to 2.7.3

* Sun Feb 1 2009 - Devrim GUNDUZ <devrim@commandprompt.com> 2.6.0-1
- Update to 2.6.0

* Fri Dec 19 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.5.3-1
- Update to 2.5.3

* Wed Dec 17 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.5.2-1
- Update to 2.5.2

* Sun Dec 7 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.5.0-1
- Update to 2.5.0

* Tue Dec 2 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.4.3-1
- Update to 2.4.3

* Tue Oct 7 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.3.0-1
- Update to 2.3.0
- Make package noarch

* Mon Sep 29 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.2.1-1
- Update to 2.2.1

* Tue Sep 23 2008 - Devrim GUNDUZ <devrim@commandprompt.com> 2.1.4-1
- Initial RPM packaging for yum.pgsqlrpms.org

#
# Rebuild option:
#
#   --with testsuite         - run the test suite
#

Name:           perl-Cairo
Version:        1.106
Release:        13%{?dist}
Summary:        Perl interface to the cairo library
License:        LGPLv2+
URL:            https://metacpan.org/release/Cairo
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSCH/Cairo-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Test::Number::Delta), perl(ExtUtils::MakeMaker)
BuildRequires:  cairo-devel >= 1.0.0
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Cairo provides Perl bindings for the vector graphics library cairo.
It supports multiple output targets, including the X Window Systems,
PDF, and PNG.  Cairo produces identical output on all those targets
and makes use of hardware acceleration wherever possible.

%prep
%setup -q -n Cairo-%{version}
chmod -c a-x examples/*.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc ChangeLog.pre-git LICENSE NEWS README TODO examples/
%{perl_vendorarch}/Cairo*
%{perl_vendorarch}/auto/Cairo/
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Tom Callaway <spot@fedoraproject.org> - 1.106-1
- update to 1.106

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.105-2
- Perl 5.22 rebuild

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 1.105-1
- update to 1.105

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.104-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Tom Callaway <spot@fedoraproject.org> - 1.104-1
- update to 1.104

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.090-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.090-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.090-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.090-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.090-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.090-2
- Perl 5.16 rebuild

* Mon Jan 30 2012 Tom Callaway <spot@fedoraproject.org> - 1.090-1
- update to 1.090

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.060-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.060-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.060-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.060-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.060-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.060-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.060-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.060-1
- update to 1.060

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.045-1
- update to 1.045
- change references to ATSUI to QUARTZ (resolves bz 440741)

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.044-4
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.044-3
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.044-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.044-1
- 1.044

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.041-2
- Rebuild for selinux ppc32 issue.

* Tue Jun 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.041-1
- Update to 1.041.

* Sat Jun 16 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.040-1
- Update to 1.040.

* Mon Feb 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.023-1
- Update to 1.023.

* Sun Dec 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.022-1
- Update to 1.022.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.021-1
- Update to 1.021.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-1
- Update to 1.02.

* Mon Oct  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-2
- Rebuild (https://www.redhat.com/archives/fedora-maintainers/2006-October/msg00005.html).

* Tue Sep 26 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- Update to 1.01.

* Tue Sep  5 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-1
- Update to 1.00.

* Wed Aug 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.92-1
- Update to 0.92.

* Sat Aug 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.91-1
- Update to 0.91.

* Sun Jul 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.90-1
- Update to 0.90.

* Tue Apr 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.03-2
- Disabled the test suite as it fails in mock.

* Sun Mar 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.03-1
- First build.

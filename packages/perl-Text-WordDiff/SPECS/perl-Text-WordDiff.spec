Name:           perl-Text-WordDiff
Version:        0.09
Release:        6%{?dist}
Summary:        Track changes between documents
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Text-WordDiff
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMK/Text-WordDiff-%{version}.tar.gz
Patch0:         Text-WordDiff-0.08-uselib.patch
BuildArch:      noarch
# Module Build
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Encode) >= 1.20
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
BuildRequires:  perl(Test::Pod)
Requires:       perl(Algorithm::Diff) >= 1.19

# Filter under-specified dependency
%global __requires_exclude ^perl\\(Algorithm::Diff\\)$

%description
This module is a variation on the lovely Text::Diff module. Rather than
generating traditional line-oriented diffs, however, it generates word-
oriented diffs. This can be useful for tracking changes in narrative
documents or documents with very long lines. To diff source code, one is
still best off using Text::Diff. But if you want to see how a short
story changed from one version to the next, this module will do the job
very nicely.

%prep
%setup -q -n Text-WordDiff-%{version}

# Don't try to use upstream's personal modules
%patch0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::WordDiff.3pm*
%{_mandir}/man3/Text::WordDiff::ANSIColor.3pm*
%{_mandir}/man3/Text::WordDiff::HTML.3pm*
%{_mandir}/man3/Text::WordDiff::HTMLTwoLines.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-1
- Update to 0.09
- Remove Group tag and add %%license macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-12
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08
  - Moved repository to GitHub
  - Added bug reporting and repository metadata
  - Added Text::WordDiff::HTMLTwoLines
  - Control and punctuation characters are now treated as standalone chunks
    rather than as part of the words that precede them, which makes for much
    more intuitive-looking diffs
- Drop %%defattr, redundant since rpm 4.4
- Make %%files list more explicit
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Specify all dependencies
- Avoid trying to use upstream's private modules in the test suite

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.05-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.05-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Steven Pritchard <steve@kspei.com> 0.05-1
- Update to 0.05.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.04-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.04-1
- Update to 0.04.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-3
- Rebuild for new perl

* Mon Jul 16 2007 Steven Pritchard <steve@kspei.com> 0.02-2
- BR Test::More and Test::Pod.

* Thu May 17 2007 Steven Pritchard <steve@kspei.com> 0.02-1
- Specfile autogenerated by cpanspec 1.70.
- Fix Summary and description.

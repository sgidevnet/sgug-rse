Name:           perl-Text-Shellwords
Version:        1.08
Release:        37%{?dist}
Summary:        A thin wrapper around the shellwords.pl package

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-Shellwords
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/Text-Shellwords-1.08.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Test:
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This is a thin wrapper around the shellwords.pl package, which comes
preinstalled with Perl.  This module imports a single subroutine,
shellwords().  The shellwords() routine parses lines of text and
returns a set of tokens using the same rules that the Unix shell does
for its command-line arguments.  Tokens are separated by whitespace,
and can be delimited by single or double quotes.  The module also
respects backslash escapes.


%prep
%setup -q -n Text-Shellwords-%{version}
# Clean up /usr/local/bin/perl mess
#%%{__perl} -pi -e 's|/usr/local/bin/perl\b|%%{__perl}|' \
#  qd.pl bdf_scripts/cvtbdf.pl demos/{*.{pl,cgi},truetype_test}

# avoid dependencies
#chmod 644 examples/* 


%build 
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags} 


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-37
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-34
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-31
- Modernize spec file

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-30
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-27
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-25
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Petr Pisar <ppisar@redhat.com> - 1.08-23
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-21
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-20
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.08-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.08-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.08-12
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.08-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.08-5
- Remove old check construct that prevents F-10+ build (#449489)

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.08-4
- rebuild for new perl

* Mon Oct 15 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.08-3
- Add missing BR: perl(ExtUtils::MakeMaker)

* Tue Sep 04 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.08-2
- Clarified license terms: GPL+ or Artistic

* Sat Mar 24 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.08-1
- Updated to 1.08
- Removed superfluous BR: Perl as per suggestion from Ralf Corsepius

* Wed Apr 06 2005 Hunter Matthews <thm@duke.edu> 1.07-2
- Review suggestions by José Pedro Oliveira

* Tue Mar 22 2005 Hunter Matthews <thm@duke.edu> 1.07-1
- Initial build.

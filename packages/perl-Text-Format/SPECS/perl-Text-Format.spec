Name:           perl-Text-Format
Version:        0.61
Release:        9%{?dist}
Summary:        Various subroutines to format text

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-Format
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Format-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests - not execute
# BuildRequires:  perl(Pod::Coverage::TrustPod)
# BuildRequires:  perl(Test::Code::TidyAll) >= 0.24
# BuildRequires:  perl(Test::CPAN::Changes)
# BuildRequires:  perl(Test::EOL)
# BuildRequires:  perl(Test::NoTabs)
# BuildRequires:  perl(Test::Pod) >= 1.41
# BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# BuildRequires:  perl(Test::TrailingSpace)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))


%description
The format routine will format under all circumstances even if the width isn't
enough to contain the longest words. Text::Wrap will die under these
circumstances, although I am told this is fixed. If columns is set to a small
number and words are longer than that and the leading 'whitespace' than there
will be a single word on each line. This will let you make a simple word list
which could be indented or right aligned. There is a chance for croaking if you
try to subvert the module. If you don't pass in text then the internal text is
worked on, though not modified. Text::Format is meant for more powerful text
formatting than Text::Wrap allows.


%prep
%setup -q -n Text-Format-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-9
- Perl 5.32 rebuild

* Fri Feb 28 2020 Petr Pisar <ppisar@redhat.com> - 0.61-8
- Build-require blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-1
- 0.61 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-1
- 0.60 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-5
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Xavier Bachelot <xavier@bachelot.org> - 0.59-2
- Add LICENSE and README to %%doc.

* Mon Feb 10 2014 Xavier Bachelot <xavier@bachelot.org> - 0.59-1
- Update to 0.59.
- Add more BR: for better tests coverage.
- Modernize specfile.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.58-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Xavier Bachelot <xavier@bachelot.org> - 0.58-1
- Update to 0.58.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.56-2
- Perl 5.16 rebuild

* Mon Jun 04 2012 Xavier Bachelot <xavier@bachelot.org> - 0.56-1
- Update to 0.56.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.53-2
- Perl mass rebuild

* Thu May 12 2011 Xavier Bachelot <xavier@bachelot.org> - 0.53-1
- Update to 0.53.

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.52-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.52-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.52-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.52-2
Rebuild for new perl

* Fri Feb 01 2008 Xavier Bachelot <xavier@bachelot.org> - 0.52-1
- Initial build.

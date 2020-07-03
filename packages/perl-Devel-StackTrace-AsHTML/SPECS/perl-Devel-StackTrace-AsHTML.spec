Name:           perl-Devel-StackTrace-AsHTML
Summary:        Displays a stack trace in HTML
Version:        0.15
Release:        13%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Devel-StackTrace-AsHTML-%{version}.tar.gz 
URL:            https://metacpan.org/release/Devel-StackTrace-AsHTML
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.75
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
# Test::Spelling not used
# Test::Synopsis not used
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(warnings)

%{?perl_default_filter}

%description
Devel::StackTrace::AsHTML adds an 'as_html' method to Devel::StackTrace
which displays the stack trace in beautiful HTML, with code snippet
context and function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical
variables of each stack frame.

%prep
%setup -q -n Devel-StackTrace-AsHTML-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.24 rebuild

* Fri Apr 08 2016 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-8
- Modernize spec.
- Remove inc/.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-6
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.14-2
- Perl 5.18 rebuild

* Fri Feb 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-1
- Upstream update.
- Remove Obsoletes/Provides *-tests.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-5
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.11-1
- Upstream update.

* Tue Jan 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10-1
- Upstream update.
- Abandon perl-Devel-StackTrace-AsHTML-tests.

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> - 0.09-2
- Rebuild against perl-5.12

* Sun Apr 11 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- specfile by Fedora::App::MaintainerTools 0.006



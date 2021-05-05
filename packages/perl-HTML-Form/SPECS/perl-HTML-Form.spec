Name:           perl-HTML-Form
Version:        6.04
Release:        3%{?dist}
Summary:        Class that represents an HTML form element
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-Form
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Form-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6.03
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Request::Common) >= 6.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%prep
%setup -q -n HTML-Form-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-2
- Perl 5.30 rebuild

* Sun Mar 31 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 6.04-1
- Update to 6.04

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-18
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-15
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-11
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-9
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 6.03-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.03-2
- Perl 5.16 rebuild

* Sat Mar 31 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 6.03-1
- Update to 6.03

* Sat Feb 25 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 6.02-1
- Update to 6.02

* Sun Feb 19 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 6.01-1
- Update to 6.01
- Clean up spec file
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-5
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-4
- Perl mass rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-3
- Perl mass rebuild

* Tue Mar 29 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 6.00-2
- Add missing Requires per review (#691226).

* Sun Mar 27 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 6.00-1
- Specfile autogenerated by cpanspec 1.78.

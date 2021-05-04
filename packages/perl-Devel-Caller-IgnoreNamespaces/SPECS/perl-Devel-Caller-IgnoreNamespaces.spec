Name:           perl-Devel-Caller-IgnoreNamespaces
Version:        1.1
Release:        7%{?dist}
Summary:        Make available a function which can ignore name-spaces that you tell it about
License:        GPLv2 or Artistic
URL:            https://metacpan.org/release/Devel-Caller-IgnoreNamespaces
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-Caller-IgnoreNamespaces-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
If your module should be ignored by caller(), just like Hook::LexWrap is
by its magic caller(), then call this module's register() subroutine
with its name.

%prep
%setup -q -n Devel-Caller-IgnoreNamespaces-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ARTISTIC.txt CHANGES GPL2.txt README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.1-1
- Update to 1.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-22
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.0-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.0-11
- Remove no-longer-used macros
- Add Test::Pod::Coverage to the BuildRequires

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.0-9
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.0-3
- Mass rebuild with perl-5.12.0

* Sat Mar 13 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.0-2
- Add perl(Test::More) and perl(Test::Pod) to BuildRequires.

* Sat Mar 13 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.0-1
- Specfile autogenerated by cpanspec 1.78.

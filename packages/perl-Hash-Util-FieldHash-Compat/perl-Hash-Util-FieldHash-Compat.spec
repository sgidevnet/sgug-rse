Name:		perl-Hash-Util-FieldHash-Compat
Version:	0.11
Release:	10%{?dist}
Summary:	Use Hash::Util::FieldHash or ties, depending on availability
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Hash-Util-FieldHash-Compat
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Hash-Util-FieldHash-Compat-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter
%if 0%{?fedora} > 20 || 0%{?rhel} > 7
BuildRequires:	perl-generators
%endif
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(parent)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	perl(Tie::RefHash)
BuildRequires:	perl(Tie::RefHash::Weak) >= 0.08
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Under older perls this module provides a drop in compatible API to
Hash::Util::FieldHash using perltie. When Hash::Util::FieldHash is
available, it will use that instead.

%prep
%setup -q -n Hash-Util-FieldHash-Compat-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENCE
%else
%doc LICENCE
%endif
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Hash/
%{_mandir}/man3/Hash::Util::FieldHash::Compat.3*
%{_mandir}/man3/Hash::Util::FieldHash::Compat::Heavy.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 14 2016 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11
  - Be gentle to older toolchains by avoiding the use of Module::Metadata in
    configure-requires (CPAN RT#115310)
- BR: perl-generators where available
- Simplify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Paul Howarth <paul@city-fan.org> - 0.10-2
- Drop provides filter, no longer needed

* Mon Sep 28 2015 Paul Howarth <paul@city-fan.org> - 0.10-1
- Update to 0.10
  - Fix invalid prereq specification for Heavy implementation (changed in 0.09)

* Mon Aug 17 2015 Paul Howarth <paul@city-fan.org> - 0.09-1
- Update to 0.09
  - Update some distribution tooling
- Classify buildreqs by usage
- Use %%license where possible

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.20 rebuild

* Fri Jul 18 2014 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08
  - Add missing prereq declarations needed for perl 5.6 (CPAN RT#97000)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Paul Howarth <paul@city-fan.org> - 0.07-1
- Update to 0.07
  - Better fix for misleading 'provides' metadata
  - Now skipping back-compat tests on newer perls; this test will now run for
    authors only

* Thu Mar 20 2014 Paul Howarth <paul@city-fan.org> - 0.06-1
- Update to 0.06
  - Fix misleading 'provides' metadata (added in 0.05) that may confuse some
    tools
- BR: perl(Devel::Hide) for new test

* Sun Feb 16 2014 Paul Howarth <paul@city-fan.org> - 0.05-1
- Update to 0.05
  - Convert to Dist::Zilla, with more metadata
- Package upstream CONTRIBUTING, LICENSE and README files

* Sun Feb  2 2014 Paul Howarth <paul@city-fan.org> - 0.04-1
- Update to 0.04
  - Localize $SIG{__DIE__} before an eval (CPAN RT#83667)
- This release by ETHER -> update source URL
- Clean up spec for modern rpmbuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.03-15
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.03-12
- Perl 5.16 rebuild

* Mon Jan 23 2012 Paul Howarth <paul@city-fan.org> - 0.03-11
- Spec clean-up
  - BR: perl(Scalar::Util), perl(Tie::RefHash) and perl(Tie::RefHash::Weak)
  - Make %%files list more explicit
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Don't use macros for commands
  - Use search.cpan.org source URL

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-9
- Perl mass rebuild

* Wed May  4 2011 Paul Howarth <paul@city-fan.org> - 0.03-8
- Fix provides filter for rpm 4.9.x and filter the unversioned provide rather
  than the versioned one

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-6
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-4
- Rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Allisson Azevedo <allisson@gmail.com> - 0.03-1
- Initial rpm release

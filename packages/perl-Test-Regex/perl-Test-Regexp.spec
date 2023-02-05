Name:		perl-Test-Regexp
Version:	2017040101
Release:	9%{?dist}
Summary:	Test your regular expressions
License:	MIT
URL:		https://metacpan.org/release/Test-Regexp
Source0:	https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Test-Regexp-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-interpreter >= 4:5.10.0
%if 0%{?fedora} > 20 || 0%{?rhel} > 7
BuildRequires:	perl-generators
%endif
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(charnames)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Hash::Util::FieldHash)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Tester)
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module is intended to test your regular expressions. Given a subject
string and a regular expression (a.k.a. pattern), the module not only tests
whether the regular expression completely matches the subject string, it
performs a utf8::upgrade or utf8::downgrade on the subject string and
performs the tests again, if necessary. Furthermore, given a pattern with
capturing parenthesis, it checks whether all captures are present, and in the
right order. Both named and unnamed captures are checked.

%prep
%setup -q -n Test-Regexp-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Regexp.3*

%changelog
* Tue Oct 06 2020  HAL <notes2@gmx.de> - 2017040101-9
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017040101-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2017040101-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017040101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017040101-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2017040101-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017040101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017040101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2017040101-2
- Perl 5.26 rebuild

* Sat Apr  1 2017 Paul Howarth <paul@city-fan.org> - 2017040101-1
- Update to 2017040101
  - Prepare for 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016060501-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun  5 2016 Paul Howarth <paul@city-fan.org> - 2016060501-1
- Update to 2016060501
  - Fix POD spelling errors

* Sun May 29 2016 Paul Howarth <paul@city-fan.org> - 2016052701-1
- Update to 2016052701
  - Allow specifying how you want to display characters that aren't printable
    ASCII characters (it used to be displayed as hex escapes); we also now
    allow named escapes "as is", \n/\r/\t only or "only escape non-printable
    ASCII", which is the new default
- BR: perl-generators where available
- Simplify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2015110201-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015110201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Paul Howarth <paul@city-fan.org> - 2015110201-2
- Sanitize for Fedora submission

* Fri Jan  8 2016 Paul Howarth <paul@city-fan.org> - 2015110201-1
- Initial RPM version

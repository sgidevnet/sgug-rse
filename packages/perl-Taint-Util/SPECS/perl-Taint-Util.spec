Name:		perl-Taint-Util
Version:	0.08
Release:	24%{?dist}
Summary:	Test for and flip the taint flag without regex matches or eval
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Taint-Util
Source0:	https://cpan.metacpan.org/modules/by-module/Taint/Taint-Util-%{version}.tar.gz
Patch0:		Taint-Util-0.08-utf8.patch
# ============= Module Build ====================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Man) >= 2.26
BuildRequires:	perl(warnings)
# ============= Module Runtime ==================
BuildRequires:	perl(strict)
BuildRequires:	perl(XSLoader)
# ============= Test Suite ======================
BuildRequires:	perl(Test::More)
# ============= Module Runtime ==================
Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Wraps perl's internal routines for checking and setting the taint flag and
thus does not rely on regular expressions for untainting or odd tricks
involving eval and kill for checking whether data is tainted; instead, it
checks and flips a flag on the scalar in-place.

%prep
%setup -q -n Taint-Util-%{version}

# Re-code README as UTF-8
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc ChangeLog README
%{perl_vendorarch}/auto/Taint/
%{perl_vendorarch}/Taint/
%{_mandir}/man3/Taint::Util.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-24
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct  5 2019 Paul Howarth <paul@city-fan.org> - 0.08-22
- Spec tidy-up
  - Use author-independent source URL
  - Drop redundant buildroot cleaning in %%install section
  - Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-20
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-17
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-11
- Perl 5.24 rebuild

* Wed Apr 20 2016 Paul Howarth <paul@city-fan.org> - 0.08-10
- Fix FTBFS due to missing buildreq perl-devel
- Simplify find commands using -empty and -delete
- Use %%license where possible

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Paul Howarth <paul@city-fan.org> - 0.08-3
- BR: perl(Pod::Man) ≥ 2.26 to get manpage rendered properly (#998447)

* Mon Aug 19 2013 Paul Howarth <paul@city-fan.org> - 0.08-2
- Sanitize for Fedora submission

* Fri Aug 16 2013 Paul Howarth <paul@city-fan.org> - 0.08-1
- Initial RPM version

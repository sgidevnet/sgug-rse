Name:           perl-HTML-Lint
Version:        2.32
Release:        4%{?dist}
Summary:        HTML::Lint Perl module
License:        Artistic 2.0
URL:            https://metacpan.org/release/HTML-Lint
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/HTML-Lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser) >= 3.47
BuildRequires:  perl(HTML::Tagset) >= 3.03
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional
BuildRequires:  perl(LWP::Simple)

# For improved testing
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Convenience to users looking for weblint
Provides:       weblint = %{version}-%{release}

%description
HTML::Lint Perl module, a pure-Perl HTML parser and checker for syntactic
legitmacy.

%prep
%setup -q -n HTML-Lint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{_bindir}/weblint
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.32-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.32-1
- Update to 2.32.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.30-1
- Update to 2.30.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.26-1
- Update to 2.26.

* Sat Dec 10 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.24-1
- Update to 2.24.
- Drop 0001-doc-tag-required-errors-are-now-sorted-by-tag-name.patch.

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.22-5
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-3
- Perl 5.22 rebuild

* Mon Apr 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.22-2
- Add 0001-doc-tag-required-errors-are-now-sorted-by-tag-name.patch
  (RHBZ #1211215, https://github.com/petdance/html-lint/issues/39)

* Tue Apr 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.22-1
- Upstream update.
- Modernize spec.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.20-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 2.20-3
- Perl 5.16 rebuild

* Thu Apr 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.20-2
- Bump release due to typo in spec.

* Thu Apr 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.20-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 2.10-1
- License change.
- Upstream update.
- Spec file cleanup.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.06-8
- Perl mass rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.06-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 2.06-1
- Initial Fedora submission.

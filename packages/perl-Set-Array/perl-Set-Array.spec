Name:           perl-Set-Array
Version:        0.30
Release:        17%{?dist}
Summary:        Arrays as objects with lots of handy methods
License:        Artistic 2.0
URL:            https://metacpan.org/release/Set-Array
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Set-Array-%{version}.tgz
Patch0:         Set-Array-0.30-utf8.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(attributes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Want)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Set::Array allows you to create arrays as objects and use OO-style methods
on them. Many convenient methods are provided here that appear in the
FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc. In addition,
there are Set methods with corresponding (overloaded) operators for the
purpose of Set comparison, i.e. +, ==, etc.

%prep
%setup -qn Set-Array-%{version}

# Fix documentation character encoding
%patch0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Set/
%{_mandir}/man3/Set::Array.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-16
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-8
- Perl 5.24 rebuild

* Mon Feb 29 2016 Paul Howarth <paul@city-fan.org> - 0.30-7
- Classify buildreqs by usage
- Make %%files list more explicit
- Use a patch rather than scripted iconv to fix character encoding

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Christopher Meng <rpm@cicku.me> - 0.30-1
- New version.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.29-3
- Perl 5.18 rebuild

* Thu Jul 11 2013 Christopher Meng <rpm@cicku.me> - 0.29-2
- Fix UTF8 issue.

* Wed Jul 03 2013 Christopher Meng <rpm@cicku.me> - 0.29-1
- Change the license so can be accepted by Fedora.

* Sun Dec 23 2012 Christopher Meng <rpm@cicku.me> - 0.28-1
- Initial Package.

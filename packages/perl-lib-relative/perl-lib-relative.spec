Name:           perl-lib-relative
Version:        1.000
Release:        3%{?dist}
Summary:        Add paths relative to the current file to @INC
License:        Artistic 2.0
URL:            https://metacpan.org/release/lib-relative
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/lib-relative-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module proposes a straightforward method for adding local directory to
@INC. It takes a path relative to the current file, absolutize it, and add
it to @INC.

%prep
%setup -q -n lib-relative-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-2
- Perl 5.30 rebuild

* Tue Mar 19 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-1
- 1.000 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> 0.002-1
- Specfile autogenerated by cpanspec 1.78.

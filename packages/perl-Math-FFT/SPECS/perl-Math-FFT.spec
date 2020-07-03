Name:           perl-Math-FFT
Version:        1.34
Release:        14%{?dist}
Summary:        Perl module to calculate Fast Fourier Transforms
# Perl module code is GPL+ or same as Perl itself
# arrays.c has same licence as Perl itself
# FFT code is based on the C routine of fft4g.c Takuya OOURA,
# which is public domain
License:        (GPL+ or Artistic) and Public Domain
URL:            https://metacpan.org/release/Math-FFT
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Math-FFT-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module implements some algorithms for calculating Fast Fourier
Transforms for one-dimensional data sets of size 2^n. 

%prep
%setup -q -n Math-FFT-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-14
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-13
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-7
- Perl 5.28 rebuild

* Mon Feb 19 2018 Miroslav Suchy <msuchy@redhat.com> - 1.34-6
- add BR gcc
- remove unneeded Group tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-2
- Perl 5.26 rebuild

* Thu Apr 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-1
- 1.34 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

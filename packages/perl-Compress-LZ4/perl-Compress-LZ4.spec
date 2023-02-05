Name:           perl-Compress-LZ4
Version:        0.25
Release:        10%{?dist}
Summary:        Perl interface to the LZ4 compression library
# other files:  GPL+ or Artistic
## Not in binary package
# src:          BSD
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Compress-LZ4
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-LZ4-%{version}.tar.gz
# Do not use bundled lz4 sources
Patch0:         Compress-LZ4-0.22-Build-against-system-lz4.patch
BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  lz4-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.82
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter) >= 5.57

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Exporter\\)$

%description
The Compress::LZ4 module provides an interface to the LZ4 compression library

%prep
%setup -q -n Compress-LZ4-%{version}
%patch0 -p1
# Remove bundled lz4
rm -Rf src
sed -i -e '/^src\//d' MANIFEST
# Correct permissions
chmod -c -x ex/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README ex
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Compress*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.26 rebuild

* Mon Apr 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump

* Thu Apr 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-1
- 0.24 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- 0.23 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 09 2015 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-2
- Perl 5.22 rebuild

* Sat Aug 23 2014 David Dick <ddick@cpan.org> - 0.20-1
- Initial release

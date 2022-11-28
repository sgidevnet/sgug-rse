%global         _hardened_build 1

Name:           perl-Text-Fuzzy
Version:        0.28
Release:        4%{?dist}
Summary:        Partial string matching using edit distances
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-Fuzzy

Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Text-Fuzzy-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)

# Testing
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Levenshtein::Damerau::XS)
BuildRequires:  perl(utf8)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module calculates edit distances between words, and searches arrays
and files to find the nearest entry by edit distance. It handles both byte
strings and character strings (strings containing Unicode), treating each
Unicode character as a single entity.

%prep
%setup -q -n Text-Fuzzy-%{version}

%build
# partially fixing hardening if not fully supported
export CFLAGS="%{optflags} -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,now -Wl,--as-needed"

# fixing interpreter used
perl -pi -e 's|#!.*$|#!/usr/bin/perl|' examples/{*.cgi,*.pl}

# removing non-needed files
rm -f make-pod.pl

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

# fixing scripts provided in docs
chmod a-x -c examples/{*.cgi,*.pl}

%check
make test

%files
%doc examples/ Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Denis Fateyev <denis@fateyev.com> - 0.28-1
- Update to 0.28 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Denis Fateyev <denis@fateyev.com> - 0.27-1
- Update to 0.27 release

* Sun Aug 06 2017 Denis Fateyev <denis@fateyev.com> - 0.26-4
- Fixing Perl interpreter path

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Denis Fateyev <denis@fateyev.com> - 0.26-1
- Update to 0.26 release

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 0.25-1
- Update to 0.25 release

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-4
- Perl 5.24 rebuild

* Fri Feb 12 2016 Denis Fateyev <denis@fateyev.com> - 0.24-3
- Docs permission fixes

* Mon Feb 08 2016 Denis Fateyev <denis@fateyev.com> - 0.24-2
- Package spec cleanup

* Fri Feb 05 2016 Denis Fateyev <denis@fateyev.com> - 0.24-1
- Initial release

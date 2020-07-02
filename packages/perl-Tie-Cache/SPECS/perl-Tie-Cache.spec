Name:           perl-Tie-Cache
Version:        0.21
Release:        17%{?dist}
Summary:        LRU Cache in Memory
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tie-Cache

Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHAMAS/Tie-Cache-%{version}.tar.gz
%{?el5:BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(Benchmark)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# filter dependencies
%{?perl_default_filter}

%description
This module implements a least recently used (LRU) cache in memory
through a tie interface. Any time data is stored in the tied hash,
that key/value pair has an entry time associated with it, and as
the cache fills up, those members of the cache that are the oldest
are removed to make room for new entries.


%prep
%setup -q -n Tie-Cache-%{version}

%if 0%{?el5}
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(Benchmark)/d' \
    -e '/perl(Tie::Cache)/d' \
    -e '/perl(Tie::Cache::LRU)/d'
EOF

%global __perl_requires %{_builddir}/Tie-Cache-%{version}/%{name}-req
chmod +x %{__perl_requires}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%if 0%{?el5}
rm -rf %{buildroot}
%endif
make pure_install DESTDIR=%{buildroot}

# drop benchmarking tool here
rm -f %{buildroot}/%{perl_vendorlib}/Tie/tie-cache-bench.pl

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README CHANGES
%doc tie-cache-bench.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-14
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.22 rebuild

* Sat Feb 28 2015 Denis Fateyev <denis@fateyev.com> - 0.21-2
- Strip unnecessary dependencies

* Wed Feb 25 2015 Denis Fateyev <denis@fateyev.com> - 0.21-1
- Initial release

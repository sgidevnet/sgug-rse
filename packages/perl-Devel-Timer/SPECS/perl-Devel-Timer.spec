Name:           perl-Devel-Timer
Version:        0.13
Release:        3%{?dist}
Summary:        Track and report execution time for parts of code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-Timer

Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Devel-Timer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(Capture::Tiny) >= 0.25
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))


%description
Devel::Timer allows developers to accurately time how long a specific
piece of code takes to execute. This can be helpful in locating the
slowest parts of an existing application.

%prep
%setup -q -n Devel-Timer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test


%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Denis Fateyev <denis@fateyev.com> - 0.13-1
- Update to 0.13 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-2
- Perl 5.26 rebuild

* Sun Feb 12 2017 Denis Fateyev <denis@fateyev.com> - 0.12-1
- Update to 0.12 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Denis Fateyev <denis@fateyev.com> - 0.10-1
- Update to 0.10 release

* Fri Oct 28 2016 Denis Fateyev <denis@fateyev.com> - 0.09-1
- Update to 0.09 release

* Fri Oct 14 2016 Denis Fateyev <denis@fateyev.com> - 0.08-1
- Update to 0.08 release

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.24 rebuild

* Sat Feb 06 2016 Denis Fateyev <denis@fateyev.com> - 0.07-1
- Update to 0.07 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-2
- Perl 5.22 rebuild

* Sat Nov 08 2014 Denis Fateyev <denis@fateyev.com> - 0.06-1
- Update to 0.06 release

* Tue Oct 07 2014 Denis Fateyev <denis@fateyev.com> - 0.05-2
- Small spec improvements

* Sat Sep 06 2014 Denis Fateyev <denis@fateyev.com> - 0.05-1
- Initial release

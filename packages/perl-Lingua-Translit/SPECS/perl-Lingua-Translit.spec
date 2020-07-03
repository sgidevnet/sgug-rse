Name:           perl-Lingua-Translit
Version:        0.28
Release:        9%{?dist}
Summary:        Transliterates text between writing systems
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Lingua-Translit

Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALINKE/Lingua-Translit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Lingua::Translit can be used to convert text from one writing system to
another, based on national or international transliteration tables. Where
possible a reverse transliteration is supported.

%prep
%setup -q -n Lingua-Translit-%{version}

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
%doc Changes README
%{_bindir}/translit
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Denis Fateyev <denis@fateyev.com> - 0.28-1
- Update to 0.28 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.26 rebuild

* Sat Apr 29 2017 Denis Fateyev <denis@fateyev.com> - 0.27-1
- Update to 0.27 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 25 2016 Denis Fateyev <denis@fateyev.com> - 0.26-1
- Update to 0.26 release

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.24 rebuild

* Wed Apr 06 2016 Denis Fateyev <denis@fateyev.com> - 0.25-1
- Changed the license to same as Perl
- Update to 0.25 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Denis Fateyev <denis@fateyev.com> - 0.24-1
- Update to 0.24 release

* Mon Nov 23 2015 Denis Fateyev <denis@fateyev.com> - 0.23-1
- Update to 0.23 release

* Wed Nov 18 2015 Denis Fateyev <denis@fateyev.com> - 0.22-2
- Some spec cleanup

* Mon Nov 16 2015 Denis Fateyev <denis@fateyev.com> - 0.22-1
- Initial release

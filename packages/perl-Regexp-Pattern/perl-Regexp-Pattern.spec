Name:           perl-Regexp-Pattern
Version:        0.2.9
Release:        2%{?dist}
Summary:        Collection of regexp patterns
License:        Perl

URL:            https://metacpan.org/release/Regexp-Pattern
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Regexp-Pattern-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Regexp::Pattern is a convention for organizing reusable regexp patterns in modules.


%prep
%autosetup -n Regexp-Pattern-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=%{buildroot}


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Regexp::Pattern*.*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Sandro Mani <manisandro@gmail.com> - 0.2.9-1
- Update to 0.2.9

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.8-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Sandro Mani <manisandro@gmail.com> - 0.2.8-1
- Update to 0.2.8

* Tue Sep 11 2018 Sandro Mani <manisandro@gmail.com> - 0.2.7-1
- Update to 0.2.7

* Mon Sep 10 2018 Sandro Mani <manisandro@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.3-2
- Perl 5.28 rebuild

* Thu Apr 05 2018 Sandro Mani <manisandro@gmail.com> - 0.2.3-1
- Update to 0.2.3

* Mon Mar 26 2018 Sandro Mani <manisandro@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Sandro Mani <manisandro@gmail.com> - 0.1.4-1
- Initial package

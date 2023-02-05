Name:           perl-System-Info
Version:        0.059
Release:        2%{?dist}
Summary:        Factory for system specific information objects
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/System-Info
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/System-Info-%{version}.tgz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
#BuildRequires:  perl(Haiku::SysInfo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
System::Info tries to present system-related information, like number of
CPU's, architecture, OS and release related information in a system-
independent way. This releases the user of this module of the need to know
if the information comes from Windows, Linux, HP-UX, AIX, Solaris, Irix, or
VMS, and if the architecture is i386, x64, pa-risc2, or arm.

%prep
%setup -q -n System-Info-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog CONTRIBUTING.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.059-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.059-1
- 0.059 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.058-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.058-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-2
- Perl 5.28 rebuild

* Thu May 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.058-1
- 0.058 bump

* Mon Feb 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.057-1
- 0.057 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.056-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.056-1
- 0.056 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.055-1
- Initial release

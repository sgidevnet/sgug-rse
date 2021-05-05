Name:           perl-Sys-Detect-Virtualization
Version:        0.107
Release:        18%{?dist}
Summary:        Library to detect if a UNIX system is running as a virtual machine
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sys-Detect-Virtualization
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-Detect-Virtualization-%{version}.tar.gz
# Included from https://rt.cpan.org/Public/Bug/Display.html?id=86673 to allow building on archs that do not have Parse::DMIDecode
Patch1:         sys_detect_virt_dmidecode.patch
# Included from https://rt.cpan.org/Public/Bug/Display.html?id=95536 to pass POD tests
Patch2:         sys_detect_virt_perldoc.patch
# Fix building on Perl without "." in @INC, CPAN RT#121721
Patch3:         Sys-Detect-Virtualization-0.107-Fix-building-on-Perl-without-.-in-INC.patch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
# The dmidecode package (and perl-Parse-DMIDecode) are only available on the following archs
%ifarch %{ix86} x86_64 ia64
BuildRequires:  perl(Parse::DMIDecode) >= 0.03
%endif
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
# BuildRequires:  perl(Test::CheckManifest) not required except for author tests
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
%ifarch %{ix86} x86_64 ia64
Requires:       perl(Parse::DMIDecode) >= 0.03
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module attempts to detect whether or not a system is running as a
guest under virtualization, using various heuristics.

%prep
%setup -q -n Sys-Detect-Virtualization-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# There is no need for a debug package, the only reason an arch is important is because of the BuildRequires
%define debug_package %{nil}
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n virtdetect
Summary:        Detect if a UNIX system is running as a virtual machine
# The BuildArch is now irrelevant, Sys::Detect::Virtualization hides the dependency on dmidecode
BuildArch:      noarch

%description -n virtdetect
This script attempts to detect whether or not a system is running as a
guest under virtualization, using various heuristics.

%files -n virtdetect
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-17
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-14
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-10
- Perl 5.26 rebuild

* Wed May 17 2017 Petr Pisar <ppisar@redhat.com> - 0.107-9
- Fix building on Perl without "." in @INC (CPAN RT#121721)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.107-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 David Dick <ddick@cpan.org> - 0.107-1
- Update to 0.107-1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 David Dick <ddick@cpan.org> - 0.106-1
- Initial release

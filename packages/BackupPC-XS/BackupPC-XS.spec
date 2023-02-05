Name:           BackupPC-XS
Version:        0.62
Release:        1%{?dist}
Summary:        Implementation of various BackupPC functions in a perl-callable module

License:        GPLv3+ and (GPL+ or Artistic) and zlib
URL:            https://github.com/backuppc/backuppc-xs
Source0:        https://github.com/backuppc/backuppc-xs/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  perl-interpreter perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Testing requirement
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides:       bundled(zlib) = 1.2.3

%description
BackupPC::XS implements various BackupPC functions in a perl-callable
module.  This module is required for BackupPC V4+.


%prep
%autosetup


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}


%check
make test


%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/BackupPC::XS.3pm*


%changelog
* Sun Jun 21 2020 Richard Shaw <hobbes1069@gmail.com> - 0.62-1
- Update to 0.62.

* Sat May 30 2020 Richard Shaw <hobbes1069@gmail.com> - 0.60-1
- Update to 0.60.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-2
- Perl 5.30 rebuild

* Mon Apr 08 2019 Richard Shaw <hobbes1069@gmail.com> - 0.59-1
- Update to 0.59.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Richard Shaw <hobbes1069@gmail.com> - 0.58-1
- Update to BackupPC-XS 0.58.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Richard Shaw <hobbes1069@gmail.com> - 0.57-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Richard Shaw <hobbes1069@gmail.com> - 0.56-1
- Update to latest upstream release.

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Richard Shaw <hobbes1069@gmail.com> - 0.55-1
- Update to latest upstream release.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-2
- Perl 5.26 rebuild

* Sun May 28 2017 Richard Shaw <hobbes1069@gmail.com> - 0.54-1
- Update to latest upstream release.

* Fri Mar 24 2017 Richard Shaw <hobbes1069@gmail.com> - 0.53-1
- Update to latest upstream release, 0.53.

* Mon Mar 13 2017 Richard Shaw <hobbes1069@gmail.com> - 0.52-1
- Initial packaging.

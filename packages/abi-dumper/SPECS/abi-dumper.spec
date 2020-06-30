Name:           abi-dumper
Version:        1.1
Release:        12%{?dist}
Summary:        Tool to dump ABI of an ELF object containing DWARF debug info

License:        GPLv2
URL:            http://github.com/lvc/abi-dumper/
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         abi-dumper-perl-brace.patch
Patch1:         0001-Support-for-new-elfutils-Fedora-30.patch

BuildArch:      noarch

BuildRequires:  coreutils
%if 0%{?rhel}
BuildRequires:  perl
%else
BuildRequires:  perl-interpreter
%endif
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  sed
# https://bugzilla.redhat.com/show_bug.cgi?id=1741795
%if ! 0%{?rhel} > 7
BuildRequires:  txt2man
%endif

Requires:       elfutils
Requires:       vtable-dumper >= 1.1
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%{?perl_default_filter}

%description
A tool to dump ABI of an ELF object containing DWARF debug info.

The tool is intended to be used with ABI Compliance Checker tool for tracking
ABI changes of a C/C++ library or kernel module.

%prep
%autosetup -p1


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_prefix}
%{__perl} Makefile.pl -install --prefix=%{buildroot}%{_prefix}

chmod 0755 %{buildroot}%{_bindir}/%{name}

%if ! 0%{?rhel} > 7
# Create manpage
mkdir -p %{buildroot}%{_mandir}/man1
%{__perl} abi-dumper.pl --help | sed "s|:$||g" | \
  txt2man -t ABI-DUMPER -s 1 -v "User Commands" -r "ABI Dumper %{version}" > \
  %{buildroot}%{_mandir}/man1/%{name}.1
%endif


%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%if ! 0%{?rhel} > 7
%{_mandir}/man1/%{name}.1*
%endif


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-12
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-9
- Appy patch to fix debuginfo ouput for Fedora 30+, fixes RHBZ#1726719.

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-8.1
- Perl 5.30 rebuild

* Tue Mar 12 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-7.1
- Actually apply the patch.

* Mon Mar 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-7
- Fix un-escaped left brace, fixex BZ#1685441.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-4
- Perl 5.28 rebuild

* Thu May 10 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1-3
- Add elfutils as a package requirement, fixes 1576565.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Richard Shaw <hobbes1069@gmail.com> - 1.1-1
- Update to latest upstream release.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0-1
- Update to latest upstream release.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.19-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.19-1
- Update to latest upstream release.

* Thu Oct  6 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.18-1
- Update to latest upstream release.

* Fri Aug 26 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.17-1
- Update to latest upstream release.

* Wed Jul  6 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.16-1
- Update to latest upstream release.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.15-2
- Perl 5.24 rebuild

* Sun Mar 13 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.15-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.14-1
- Update to latest upstream release.

* Sat Dec 12 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.13-1
- Update to latest upstream release.

* Sun Nov  1 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.12-1
- Update to latest upstream release.

* Sun Oct 18 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.11-1
- Update to latest upstream release.

* Thu Sep 17 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.10-1
- Update to latest upstream release.

* Thu Aug 27 2015 Petr Šabata <contyk@redhat.com> - 0.99.8-6
- Prevent FTBFS by correcting the build time dependency list

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.8-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.8-3
- Perl 5.20 rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar  4 2014 Richard Shaw <hobbes1069@gmail.com> - 0.99.8-1
- Update to latest upstream release.

* Sun Oct 27 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.7-1
- Update to latest upstream release.

* Wed Sep 18 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.6-1
- Update to latest upstream release.

* Thu Aug  8 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.5-1
- Update to latest upstream release.

* Wed Jul 31 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.1-1
- Update to latest upstream release with reduced memory usage.

* Fri Jul 19 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99-1
- Update to latest upstream release.

* Wed Jul  3 2013 Richard Shaw <hobbes1069@gmail.com> - 0.98-1
- Initial packaging.

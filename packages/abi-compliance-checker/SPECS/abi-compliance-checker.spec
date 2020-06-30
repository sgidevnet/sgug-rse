Name:           abi-compliance-checker
Version:        2.3
Release:        6%{?dist}
Summary:        An ABI Compliance Checker

License:        GPLv2+ or LGPLv2+
URL:            http://lvc.github.io/abi-compliance-checker/
Source0:        https://github.com/lvc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
Requires:       gcc >= 4.5
Requires:       gcc-c++ >= 4.5
Requires:       binutils
Requires:       findutils
Requires:       ctags >= 5.8
Requires:       ccache >= 3.1.2
Requires:       abi-dumper >= 0.99.15

%{?perl_default_filter}

%description
A tool for checking backward binary compatibility of a shared C/C++ library. It
checks for changes in calling stack, changes in v-table, removed symbols, etc.


%prep
%autosetup -p1


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*


%files
%license LICENSE
%doc README.md doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Wed Mar 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.3-6
- Add perl dependencies needed for build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Richard Shaw <hobbes1069@gmail.com> - 2.3-1
- Update to 2.3.

* Tue May 08 2018 Richard Shaw <hobbes1069@gmail.com> - 2.2-3
- Rebased patch from upstream commit for gcc 8 compatibility, fixes 1575520.
- Add findutils as a package requirement, fixes 1576567.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Richard Shaw <hobbes1069@gmail.com> - 2.2-1
- Update to latest upstream release.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Richard Shaw <hobbes1069@gmail.com> - 2.1-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Richard Shaw <hobbes1069@gmail.com> - 2.0-1
- Update to latest upstream release.

* Thu Oct 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1.99.25-1
- Update to latest upstream release.

* Mon May 16 2016 Richard Shaw <hobbes1069@gmail.com> - 1.99.20-1
- Update to latest upstream release.

* Tue Apr 26 2016 Richard Shaw <hobbes1069@gmail.com> - 1.99.19-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Richard Shaw <hobbes1069@gmail.com> - 1.99.13-1
- Update to latest upstream release.

* Tue Sep  8 2015 Richard Shaw <hobbes1069@gmail.com> - 1.99.10-1
- Update to latest upstream release.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar  4 2014 Richard Shaw <hobbes1069@gmail.com> - 1.99.9-1
- Update to latest bugfix release.

* Tue Oct  8 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.8.5-1
- Update to latest bugfix release.

* Fri Sep 27 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.8.4-1
- Update to latest bugfix release.

* Wed Sep 18 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.8.3-1
- Update to latest bugfix release.

* Sat Aug 10 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.8.2-1
- Update to latest bugfix release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.99.7-2
- Perl 5.18 rebuild

* Fri Jun 28 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.7-1
- Update to latest bugfix release.

* Tue Jun 25 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.2-1
- Update to latest bugfix release.

* Sat Jun  8 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99.1-1
- Update to latest bugfix release.

* Tue May 28 2013 Richard Shaw <hobbes1069@gmail.com> - 1.99-1
- Update to latest upstream release.

* Fri May 03 2013 Richard Shaw <hobbes1069@gmail.com> - 1.98.8-2
- Add package requires for gcc-c++, ctags, ccache.

* Sat Feb  9 2013 Richard Shaw <hobbes1069@gmail.com> - 1.98.8-1
- Update to latest upstream release.

* Sat Dec 15 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98.7-1
- Update to latest upstream release.

* Wed Dec 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98.6-1
- Update to latest upstream release.

* Sun Oct 21 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98.4-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98.2-1
- Update to latest upstream release.

* Mon Jun 18 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98.1-1
- Update to latest upstream release.

* Mon Jun 11 2012 Richard Shaw <hobbes1069@gmail.com> - 1.97.8-1
- Update to latest upstream release.

* Mon Jun 04 2012 Richard Shaw <hobbes1069@gmail.com> - 1.97.7-1
- Update to latest upstream release.

* Tue May 15 2012 Richard Shaw <hobbes1069@gmail.com> - 1.97.5-1
- Update to latest upstream release.

* Tue Apr 17 2012 Richard Shaw <hobbes1069@gmail.com> - 1.97.4-1
- Update to latest upstream release.

* Tue Dec 20 2011 Richard Shaw <hobbes1069@gmail.com> - 1.96.1-1
- Update to 1.96.1.
- Fixes false positive: http://forge.ispras.ru/issues/2097

* Wed Dec 07 2011 Richard Shaw <hobbes1069@gmail.com> - 1.95.13-1
- Updated to 1.95.13.

* Thu Nov 17 2011 Richard Shaw <hobbes1069@gmail.com> - 1.95.10-1
- Updated license field based on upstream response.
- Updated to 1.95.10.
- Added SVN changelog.

* Wed Nov 16 2011 Richard Shaw <hobbes1069@gmail.com> - 1.95.9-2
- Fix perl private module install location.
- Fix spec license field.
- Minor specfile cleanup.

* Mon Nov 14 2011 Richard Shaw <hobbes1069@gmail.com> - 1.95.9-1
- Initial release.

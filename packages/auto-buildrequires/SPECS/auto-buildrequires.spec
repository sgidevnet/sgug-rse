Summary:       Work out BuildRequires for rpmbuild automatically
Name:          auto-buildrequires
Version:       1.2
Release:       10%{?dist}

License:       GPLv2+

URL:           http://people.redhat.com/~rjones/auto-buildrequires/
Source0:       http://people.redhat.com/~rjones/auto-buildrequires/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:      rpm-build
Requires:      perl-String-ShellQuote

%description
Auto-BuildRequires is a simple set of scripts for automatically suggesting 
BuildRequires lines for programs.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files
%doc COPYING README
%{_bindir}/auto-br
%{_bindir}/auto-br-rpmbuild
%{_libexecdir}/auto-br-analyze.pl
%{_libexecdir}/%{name}-preload.so
%{_mandir}/man1/autobuildrequires.1*
%{_mandir}/man1/auto-br.1*
%{_mandir}/man1/auto-br-rpmbuild.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2-1
- New upstream version 1.2.
- Add man pages.
- Make explicit the BuildRequires on perl, pod2man.
- Modernize the spec file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-10
- Fix URLs (thanks David Woodhouse).

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-1
- New upstream version 1.1.
- Fixes bug when LANG != C (RHBZ#545867).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0-3
- New upstream version 1.0:
  . Fixes 32-bit platforms.
  . Add a missing runtime requires for a Perl library.
- High release number is so that we are larger than the release number
  in the upstream specfile.

* Fri Mar  6 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9-2
- Prepared the SPEC file for Review Request submission

* Fri Mar  6 2009 Richard Jones <rjones@redhat.com> - 0.9-1
- Imported to git and rebuilt.

* Thu Nov  6 2008 Richard Jones <rjones@redhat.com> - 0.1-2
- Initial build.

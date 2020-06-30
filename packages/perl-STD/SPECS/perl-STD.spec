Name:           perl-STD
Version:        20101111
Release:        20%{?dist}
Summary:        The Standard Perl 6 Grammar
License:        Artistic 2.0
URL:            https://metacpan.org/release/STD
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SOREAR/STD-%{version}.tar.gz
# Remove /usr/bin/env from shebang
Patch0:         STD-20101111-Remove-usr-bin-env-from-shebang.patch
# Enable loading objects from YAML documents, bug #1799856, CPAN RT#132275
Patch1:         STD-20101111-Enable-loading-objects-from-YAML-documents.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build) >= 0.37
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# No tests run
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(File::ShareDir) >= 1.02
Provides:       perl(STD) = %{version}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::ShareDir\\)$
# Remove private packages 
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(mangle.pl|STD_P5|STD_P6|RE_ast|STD::Cursor\\)$

%description
%{summary}.

%prep
%setup -q -n STD-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Build.PL installdirs=core
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc LICENSE
%{perl_privlib}/*
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-20
- Perl 5.32 rebuild

* Tue Mar 31 2020 Petr Pisar <ppisar@redhat.com> - 20101111-19
- Enable loading objects from YAML documents (bug #1799856)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Petr Pisar <ppisar@redhat.com> - 20101111-11
- Remove /usr/bin/env from shebang

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20101111-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 20101111-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 20101111-1
- 20101111 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32116-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 32116-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32116-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32116-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 32116-7
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 32116-6
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32116-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 32116-4
- add new filter

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 32116-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 22 2010 Petr Pisar <ppisar@redhat.com> 32116-1
- Specfile autogenerated by cpanspec 1.78.
- Remove pre-F12 spec statements (BuildRoot etc.)
- Filter private packages mangle.pl, STD_P5, STD_P6, RE_ast, STD::Cursor out of
  Requires
- Provide versioned perl(STD)

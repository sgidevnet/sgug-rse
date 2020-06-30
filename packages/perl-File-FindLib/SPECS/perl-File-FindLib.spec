Name:           perl-File-FindLib
Version:        0.001004
Release:        18%{?dist}
Summary:        Find and use a file/directory from a directory above your script file
License:        Unlicense
URL:            https://metacpan.org/release/File-FindLib
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-FindLib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(lib)

%description
File::FindLib starts in the directory where your script (or library) is
located and looks for the file or directory whose name you pass in. If it
isn't found, then FindLib looks in the parent directory and continues
moving up parent directories until it finds it or until there is not
another parent directory.

%prep
%setup -q -n File-FindLib-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-18
- Perl 5.32 rebuild

* Thu Mar 12 2020 Petr Pisar <ppisar@redhat.com> - 0.001004-17
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.001004-2
- Perl 5.20 rebuild

* Wed Jul 30 2014 David Dick <ddick@cpan.org> - 0.001004-1
- Initial release

Name:           perl-App-ccdiff
Version:        0.28
Release:        3%{?dist}
Summary:        Colored Character diff

License:        Artistic 2.0
URL:            https://metacpan.org/release/App-ccdiff
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/App-ccdiff-%{version}.tgz

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  make

BuildRequires:  perl(warnings)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Getopt::Long)

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Capture::Tiny)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# For pod2man / nroff
Requires:       perl-podlators
Requires:       groff-base

# For pod2usage
Requires:       perl(Pod::Usage)

%{?perl_default_filter}

%description
All command-line tools that show the difference between two files fall
short in showing minor changes visuably useful. This tool tries to give
the look and feel of `diff --color` or `colordiff`, but extending the
display of colored output from red for deleted lines and green for added
lines to red for deleted characters and green for added characters within
the changed lines.


%prep
%setup -q -n App-ccdiff-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc ChangeLog CONTRIBUTING.md README.md
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Richard Fearn <richardfearn@gmail.com> 0.28-1
- Update to new version 0.28 (#1748007)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Richard Fearn <richardfearn@gmail.com> 0.26-5
- Add version constraint to ExtUtils::MakeMaker dependency (due to use of
  NO_PACKLIST)

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-4
- Don't explicitly delete empty directories - it is done automatically

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-3
- Don't create .packlist files at build time

* Mon Jan 07 2019 Richard Fearn <richardfearn@gmail.com> 0.26-2
- Add missing BuildRequires and Requires

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> 0.26-1
- Initial version for Fedora

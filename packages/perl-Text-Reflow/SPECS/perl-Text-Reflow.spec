Name:           perl-Text-Reflow
Version:        1.17
Release:        13%{?dist}
Summary:        Perl module for reflowing text files using Knuth's paragraphing algorithm
License:        GPLv3+ and (GPL+ or Artistic)
URL:            https://metacpan.org/release/Text-Reflow
Source0:        https://cpan.metacpan.org/authors/id/M/MW/MWARD/Text-Reflow-%{version}.tar.gz
# Build
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
These routines will reflow the paragraphs in the given file, filehandle,
string or array using Knuth's paragraphing algorithm (as used in TeX) to
pick "good" places to break the lines.

%package -n reflow
Summary:        A utility for reflowing text files using Knuth's paragraphing algorithm
License:        GPLv2+
BuildArch:      noarch

%description -n reflow
%{summary}.

%prep
%setup -q -n Text-Reflow-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text
%{_mandir}/man3/*

%files -n reflow
%{_bindir}/reflow
%{_mandir}/man1/reflow*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-10
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.17-1
- Update to 1.17

* Sun Dec 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.15-1
- Update to 1.15

* Sun Nov 27 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.12-1
- Update to 1.12

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Petr Šabata <contyk@redhat.com> - 1.11-1
- 1.11 bump; only fixes a typo in the changelog, really

* Fri Jul 17 2015 Petr Šabata <contyk@redhat.com> - 1.10-1
- 1.10 bump
- Drop the patch, incorporated upstream (rt#105774)
- Don't package the modules files twice

* Thu Jul 09 2015 Petr Šabata <contyk@redhat.com> 1.09-1
- Initial packaging

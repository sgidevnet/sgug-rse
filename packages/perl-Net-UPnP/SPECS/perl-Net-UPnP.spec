Name:       perl-Net-UPnP
Version:    1.4.6
Epoch:      1
Release:    6%{?dist}
Summary:    Perl extension for UPnP
License:    BSD
URL:        https://metacpan.org/release/Net-UPnP
Source0:    https://cpan.metacpan.org/authors/id/S/SK/SKONNO/Net-UPnP-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# Socket not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This package provides some functions to control UPnP devices.

%prep
%setup -q -n Net-UPnP-%{version}
# Fix file attributes
find -name '*.pm' -exec chmod a-x '{}' +

# Fix shebangs
for file in examples/*.pl; do
    sed '1 s|^#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|g' \
        "$file" > "${file}.mod" && \
    touch -r "$file" "${file}.mod" && \
    mv "${file}.mod" "$file"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc AUTHORS Changes README examples/
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::UPnP*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.6-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.6-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Petr Pisar <ppisar@redhat.com> - 1:1.4.6-1
- 1.4.6 bump

* Fri Nov 09 2018 Petr Pisar <ppisar@redhat.com> - 1:1.4.5-1
- 1.4.5 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.4-2
- Perl 5.28 rebuild

* Fri May 25 2018 Petr Pisar <ppisar@redhat.com> - 1:1.4.4-1
- 1.4.4 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.3-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.3-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.3-2
- Perl 5.22 rebuild

* Mon Oct 20 2014 Petr Pisar <ppisar@redhat.com> - 1:1.4.3-1
- 1.4.3 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4.2-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:1.4.2-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1:1.4.2-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.4.2-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.4.2-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 14 2010 Petr Pisar <ppisar@redhat.com> - 1:1.4.2-4
- Remove duplicate BuildRequires perl(version)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.4.2-3
- Added BR: perl(version) to fix FTBFS.

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.4.2-2
- Mass rebuild with perl-5.12.0

* Sun Dec 27 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1:1.4.2-1
- Update to 1.4.2.
- Fix spelling in rpm version: 1.4.1 instead of previous 1.41.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.4.1-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-3
- Review fixes.

* Sun Apr 12 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-2
- Add missing BR: Test::More.

* Sun Apr 12 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.4.1-1
- Specfile autogenerated by cpanspec 1.77.


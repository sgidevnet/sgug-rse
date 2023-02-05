Name:           perl-Lingua-Identify
Summary:        Language identification
Version:        0.56
Release:        13%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Lingua-Identify
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Lingua/Lingua-Identify-%{version}.tar.gz

# https://rt.cpan.org/Public/Bug/Display.html?id=83071
Patch0:         Lingua-Identify-0.51-Fix-a-unit-test.patch

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Factory::Util) >= 1.6
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Affixes) >= 0.07
BuildRequires:  perl(Text::ExtractWords)
BuildRequires:  perl(Text::Ngram) >= 0.13
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Class::Factory::Util) >= 1.6
Requires:       perl(Text::Affixes) >= 0.07
Requires:       perl(Text::Ngram) >= 0.13

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Factory::Util|Text::Affixes|Text::Ngram)\\)$

%description
Lingua::Identify identifies the language a given string or file is written in.


%package tools
Summary:        Tools related to Lingua::Identify
Requires:       %{name} == %{version}-%{release}
Requires:       perl(Text::Affixes) >= 0.07
Requires:       perl(Text::Ngram) >= 0.13

%description tools
Tools related to Lingua::Identify.


%prep
%setup -q -n Lingua-Identify-%{version}
%patch0 -p1


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{_mandir}/man3/Lingua::Identify*
%{perl_vendorlib}/Lingua

%files tools
%{_bindir}/langident
%{_bindir}/make-lingua-identify-language
%{_mandir}/man1/langident.1*
%{_mandir}/man1/make-lingua-identify-language.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.56-1
- Update to 0.56 (#1230634)

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.51-4
- Perl 5.18 rebuild

* Mon Feb 04 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.51-3
- Add missing build requirements.
- Patch a unit test so it actually tests something (RT#83071)

* Thu Jan 24 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.51-2
- Replace usage of the %%{__perl} macro by the plain perl command.
- Use DESTDIR instead of PERL_INSTALL_ROOT in the install section.
- Add missing build requirements.

* Fri Jan 18 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.51-1
- Initial package for Fedora, with help from cpanspec.

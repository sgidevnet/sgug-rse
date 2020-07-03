%global cpan_version v1.1.1

Name:           perl-URI-Encode
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        13%{?dist}
Summary:        Percent encoding/decoding for URIs
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/URI-Encode
Source0:        https://cpan.metacpan.org/modules/by-module/URI/URI-Encode-%{cpan_version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.38
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(Encode) >= 2.12

# Drop under-specified dependencies
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Encode\\)$

%description
This module provides a method to encode strings (mainly URLs) into a format 
which can be pasted into a plain text emails, and that those links are 
'click-able' by the person reading that email.  This can be accomplished by NOT
encoding the reserved characters.

%prep
%setup -q -n URI-Encode-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI/
%{_mandir}/man3/URI::Encode.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Paul Howarth <paul@city-fan.org> - 1.1.1-11
- Spec tidy-up
  - Classify buildreqs by usage
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-1
- 1.1.1 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.1-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.1-1
- 1.0.1 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.22 rebuild

* Wed Oct 01 2014 David Dick <ddick@cpan.org> - 0.09-1
- Initial release

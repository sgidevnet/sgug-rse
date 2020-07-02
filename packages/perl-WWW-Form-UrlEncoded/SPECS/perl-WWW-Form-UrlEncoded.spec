Name:           perl-WWW-Form-UrlEncoded
Version:        0.26
Release:        4%{?dist}
Summary:        Parser and builder for application/x-www-form-urlencoded
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WWW-Form-UrlEncoded
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.008001

BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build) > 0.4005
BuildRequires:  perl(Test::More) >= 0.98

BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

# N/A in Fedora
# Suggests: perl(WWW::Form::UrlEncoded::XS)

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded parser and
builder. This module aims to have compatibility with other CPAN modules
like HTTP::Body's urlencoded parser.

%prep
%setup -q -n WWW-Form-UrlEncoded-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
BREAK_BACKWARD_COMPAT=1 ./Build

%install
BREAK_BACKWARD_COMPAT=1 ./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
BREAK_BACKWARD_COMPAT=1 ./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.26-1
- Update to 0.26.
- Drop WWW-Form-UrlEncoded-0.23-arch.patch,
  use BREAK_BACKWARD_COMPAT=1 instead.

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Update to 0.25.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-2
- Perl 5.26 rebuild

* Wed Mar 01 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Update to 0.24.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 22 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-2
- Reflect feedback from review.

* Sat Oct 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Initial Fedora packages.

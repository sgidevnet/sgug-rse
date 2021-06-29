Name:           perl-HTTP-Tiny-Multipart
Version:        0.08
Release:        3%{?dist}
Summary:        Add post_multipart to HTTP::Tiny

License:        Artistic 2.0
URL:            https://search.cpan.org/dist/HTTP-Tiny-Multipart/
Source0:        https://www.cpan.org/modules/by-module/HTTP/HTTP-Tiny-Multipart-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >=  1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.


%prep
%autosetup -n HTTP-Tiny-Multipart-%{version} -p 1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%doc Changes
%license CONTRIBUTORS LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.30 rebuild

* Mon Feb 25 2019 Björn Esser <besser82@fedoraproject.org> - 0.08-1
- Bump release to stable (#1680373)

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.08-0.4
- Changes as suggested in review (#1680373)
- Add a set of explicit BuildRequires
- Improve Summary tag and %%description

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.08-0.3
- Add explicit perl module compat requires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.08-0.2
- Add missing BuildRequires: perl(Test::More)

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.08-0.1
- Initial rpm release (#1680373)

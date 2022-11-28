Name:           perl-Graphics-ColorUtils
Version:        0.17
Release:        4%{?dist}
Summary:        Easy-to-use color space conversions and more
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Graphics-ColorUtils
Source:         https://cpan.metacpan.org/authors/id/J/JA/JANERT/Graphics-ColorUtils-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(:VERSION) >= 5.8.3
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Makefile:
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Tests:
BuildRequires:  perl(Test::More)

%description
This modules provides some utility functions to handle colors and color space
conversions.

The interface has been kept simple, so that most functions can be called
"inline" when making calls to graphics libraries such as GD, Tk, or when
generating HTML/CSS.


%prep
%setup -q -n Graphics-ColorUtils-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/Graphics::ColorUtils.3*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-1
- Initial package release

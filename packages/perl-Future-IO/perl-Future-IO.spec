Name:           perl-Future-IO
Version:        0.06
Release:        2%{?dist}
Summary:        Future-returning IO core methods
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Future-IO
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-IO-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-interpreter >= 5.10
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.4004
# runtime requirements
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Future)
BuildRequires:  perl(strict)
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This package provides a few basic methods that behave similarly to the
same-named core perl functions relating to IO operations but yield
their results asynchronously via Future instances.

%prep
%setup -q -n Future-IO-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Future*
%{_mandir}/man3/Future*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.06-1
- Update to 0.06

* Sun Jun 16 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.05-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.

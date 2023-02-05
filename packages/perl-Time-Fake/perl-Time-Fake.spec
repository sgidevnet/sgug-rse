Name:           perl-Time-Fake
Version:        0.11
Release:        2%{?dist}
Summary:        Simulate different times without changing your system clock
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Time-Fake/
Source0:        https://cpan.metacpan.org/modules/by-module/Time/Time-Fake-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Use this module to achieve the effect of changing your system clock, but
without actually changing your system clock. It overrides the Perl
builtin subs time, localtime, and gmtime, causing them to return a
"faked" time of your choice. From the script's point of view, time still
flows at the normal rate, but it is just offset as if it were executing
in the past or present.

%prep
%setup -q -n Time-Fake-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2020 Xavier Bachelot <xavier@bachelot.org> 0.11-2
- Review fixes.

* Tue Jan 07 2020 Xavier Bachelot <xavier@bachelot.org> 0.11-1
- Initial package.

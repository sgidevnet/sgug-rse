Name:           perl-Array-IntSpan
Version:        2.004
Release:        2%{?dist}
Summary:        Handles arrays of scalars or objects using integer ranges
License:        Artistic 2.0

URL:            https://metacpan.org/release/Array-IntSpan
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Array-IntSpan-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)


Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
Array::IntSpan brings the speed advantages of Set::IntSpan to arrays. Uses
include manipulating grades, routing tables, or any other situation where you
have mutually exclusive ranges of integers that map to given values.


%prep
%autosetup -p1 -n Array-IntSpan-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Array::IntSpan*.*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.004-2
- Perl 5.32 rebuild

* Fri Mar 27 2020 Sandro Mani <manisandro@gmail.com> - 2.004-1
- Initial package

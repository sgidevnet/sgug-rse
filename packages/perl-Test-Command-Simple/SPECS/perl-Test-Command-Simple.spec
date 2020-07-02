Name:           perl-Test-Command-Simple
Version:        0.05
Release:        2%{?dist}
Summary:        Test external commands (nearly) as easily as loaded modules
License:        Perl

URL:            https://metacpan.org/release/Test-Command-Simple
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMCBRIDE/Test-Command-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This test module is intended to simplify testing of external commands. It does
so by running the command under IPC::Open3, closing the stdin immediately, and
reading everything from the command's stdout and stderr. It then makes the
output available to be tested.


%prep
%autosetup -p1 -n Test-Command-Simple-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/Test::Command::Simple*.*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.32 rebuild

* Sun Feb 23 2020 Sandro Mani <manisandro@gmail.com> - 0.05-1
- Initial package

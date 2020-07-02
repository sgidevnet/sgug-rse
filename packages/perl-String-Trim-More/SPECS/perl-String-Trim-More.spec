Name:           perl-String-Trim-More
Version:        0.03
Release:        5%{?dist}
Summary:        Various string trimming utilities
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/String-Trim-More
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/String-Trim-More-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)


Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This is an alternative to String::Trim. Instead of a single trim function, this
module provides several from which you can choose on, depending on your needs.


%prep
%autosetup -n String-Trim-More-%{version}


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
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::Trim::More*.*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Sandro Mani <manisandro@gmail.com> - 0.03-3
- Fix license tag

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 0.03-2
- Fix / constrain BRs
- Pass NO_PACKLIST=1 to Makefile.PL
- Run fixperms on buildroot

* Mon Jan 06 2020 Sandro Mani <manisandro@gmail.com> - 0.03-1
- Initial package

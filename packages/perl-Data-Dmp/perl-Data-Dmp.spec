Name:           perl-Data-Dmp
Version:        0.23
Release:        7%{?dist}
Summary:        Dump Perl data structures as Perl code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Dmp
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Data-Dmp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Regexp::Stringify)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(B::Deparse)
Requires:       perl(Regexp::Stringify)

%description
This module is a Perl dumper like Data::Dumper. It's compact, starts fast
and does not use any non-core modules except Regexp::Stringify when dumping
regexes. It produces compact single-line output (similar to
Data::Dumper::Concise). It supports dumping objects, regexes, circular
structures, coderefs.

%prep
%setup -q -n Data-Dmp-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
chmod a-x devscripts/bench
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' devscripts/bench

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes devscripts README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- Initial release

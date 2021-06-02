# Filter unversioned module dependency
%global __requires_exclude ^perl\\(Scalar::Util\\)$

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Net-BGP

Summary:        Perl module for object-oriented API to the BGP protocol
Name:           perl-Net-BGP
Version:        0.17
Release:        1%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/S/SS/SSCHECK/%{pkgname}-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Scalar::Util) >= 1.01
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  make
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  perl(ExtUtils::MakeMaker), findutils
%else
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
%endif
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 0.95 
BuildArch:      noarch

%description
An implementation of the BGP-4 inter-domain routing protocol as Perl module.
It encapsulates all of the functionality needed to establish and maintain a
BGP peering session and exchange routing update information with the peer.
It aims to provide a simple API to the BGP protocol for the purposes of
automation, logging, monitoring, testing, and similar tasks using the power
and flexibility of Perl. The module does not implement the functionality of
a RIB (Routing Information Base) nor does it modify the kernel routing table
of the host system. However, such operations could be implemented using the
API provided by the module.

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove signature test (#1701810)
rm -f t/00-Signature.t

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Aug 06 2019 Robert Scheck <robert@fedoraproject.org> 0.17-1
- Upgrade to 0.17 (#1737397)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.30 rebuild

* Wed Apr 24 2019 Robert Scheck <robert@fedoraproject.org> 0.16-2
- Add corrections from package review (#1701810 #c1 and #c3)
 
* Mon Apr 22 2019 Robert Scheck <robert@fedoraproject.org> 0.16-1
- Upgrade to 0.16 (#1701810)
- Initial spec file for Fedora and Red Hat Enterprise Linux

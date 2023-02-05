Name:           perl-Future
Version:        0.41
Release:        2%{?dist}
Summary:        Perl object system to represent an operation awaiting completion
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Future
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.25
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Refcount)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.25

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp\\)$

%description
A Future object represents an operation that is currently in progress, or
has recently completed. It can be used in a variety of ways to manage the
flow of control, and data, through an asynchronous program.

%prep
%setup -q -n Future-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Future*
%{perl_vendorlib}/Test/Future*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.41-1
- Update to 0.41

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-2
- Perl 5.30 rebuild

* Sun May 05 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40-1
- Update to 0.40

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.39-1
- Update to 0.39

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.38-1
- Update to 0.38

* Thu Dec 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.37-1
- Update to 0.37

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.35-1
- Update to 0.35

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.34-1
- Update to 0.34

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Petr Šabata <contyk@redhat.com> - 0.33-2
- Prevent FTBFS by correcting the build tim dependency list

* Fri Jul 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.33-1
- Update to 0.33

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-2
- Perl 5.22 rebuild

* Sun Mar 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.32-1
- Update to 0.32

* Fri Nov 28 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.30-1
- Update to 0.30
- Use the %%license tag

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-2
- Perl 5.20 rebuild

* Sun Jul 20 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.29-1
- Update to 0.29

* Sun Jun 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.28-1
- Update to 0.28

* Sun Jun 08 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.27-1
- Update to 0.27

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25

* Sun Jan 26 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23

* Sun Jan 12 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Update to 0.22

* Sun Dec 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.21-1
- Update to 0.21

* Sun Nov 24 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Update to 0.20

* Sun Sep 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19

* Sun Sep 22 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.18-1
- Update to 0.18

* Sun Sep 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17

* Sun Sep 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.16-1
- Update to 0.16

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.15-1
- Update to 0.15

* Sun Jun 23 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.14-1
- Update to 0.14

* Fri Jun 14 2013 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.13-2
- Add perl(Test::Pod) as a BR, per review (#974559)

* Fri Jun 14 2013 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.13-1
- Specfile autogenerated by cpanspec 1.78.

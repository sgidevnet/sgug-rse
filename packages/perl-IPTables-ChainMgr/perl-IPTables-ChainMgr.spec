Name:           perl-IPTables-ChainMgr
Version:        1.6
Release:        11%{?dist}
Summary:        Perl extension for manipulating iptables policies
License:        Artistic 2.0
URL:            http://www.cipherdyne.org/modules/
Source0:        http://www.cipherdyne.org/modules/IPTables-ChainMgr-%{version}.tar.bz2
Source1:        http://www.cipherdyne.org/modules/IPTables-ChainMgr-%{version}.tar.bz2.asc
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPTables::Parse)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The IPTables::ChainMgr package provides an interface to manipulate iptables
policies on Linux systems through the direct execution of iptables
commands. Although making a perl extension of libiptc provided by the iptables
project is possible, it is easy to just execute iptables commands directly in
order to both parse and change the configuration of the policy. Further, this
simplifies installation since the only external requirement is (in the spirit
of scripting) to be able to point IPTables::ChainMgr at an installed iptables
binary instead of having to compile against a library.

%prep
%setup -q -n IPTables-ChainMgr-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6-5
- Adapt spec to latest guidelines

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 6 2016 Miloslav Trmač <mitr@redhat.com> - 1.6-1
- Update to IPTables-ChainMgr-1.6

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Miloslav Trmač <mitr@redhat.com> - 1.5-1
- Update to IPTables-ChainMgr-1.5
  Resolves: #1296157

* Wed Oct 14 2015 Miloslav Trmač <mitr@redhat.com> - 1.4-2
- Add Requires: perl(Test) needed with perl-4:5.22.0-352.fc24

* Tue Sep 29 2015 Miloslav Trmač <mitr@redhat.com> - 1.4-1
- Update to IPTables-ChainMgr-1.4
  Resolves: #1267304

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-2
- Perl 5.22 rebuild

* Wed Mar 4 2015 Miloslav Trmač <mitr@redhat.com> - 1.3-1
- Update to IPTables-ChainMgr-1.3

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.2-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.2-2
- Perl 5.16 rebuild

* Mon Mar 12 2012 Miloslav Trmač <mitr@redhat.com> - 1.2-1
- Update to IPTables-ChainMgr-1.2

* Mon Feb 27 2012 Miloslav Trmač <mitr@redhat.com> - 0.9.9-1
- Update to IPTables-ChainMgr-0.9.9

* Tue Jan 10 2012 Miloslav Trmač <mitr@redhat.com> - 0.9-9
- Avoid deprecated use of qw()
  Resolves: #771781

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com>
- Mass rebuild with perl-5.12.0

- Drop no longer required references to BuildRoot

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Miloslav Trmač <mitr@redhat.com> - 0.9-1
- Update to IPTables-ChainMgr-0.9.

* Tue Oct 21 2008 Miloslav Trmač <mitr@redhat.com> - 0.8-1
- Update to IPTables-ChainMgr-0.8.

* Wed Jul 30 2008 Miloslav Trmač <mitr@redhat.com> 0.7-1
- Initial package.

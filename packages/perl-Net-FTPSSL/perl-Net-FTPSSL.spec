Name:           perl-Net-FTPSSL
Version:        0.41
Release:        4%{?dist}
Summary:        Perl module for FTP over SSL/TLS
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Net-FTPSSL
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLEACH/Net-FTPSSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# According to Changes, v0.97 causes unspecified hang,
# but v1.08 is well tested. In el5 we have v1.01, dropping
# the v1.08 requirement that META.yml has.
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::SSLeay::Handle)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Net::FTPSSL is a class implementing a simple FTP client over a Secure
Sockets Layer (SSL) or Transport Layer Security (TLS) connection written in
Perl as described in RFC959 and RFC2228. It will use TLS by default.


%prep
%setup -q -n Net-FTPSSL-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*


%check
# "You can also perform a deeper test.
# Some information will be required for this test:
# A secure ftp server address, a user, a password and a directory
# where the user has permissions to read and write."
echo n |make test


%files
%doc Changes README
%{perl_vendorlib}/Net*
%{_mandir}/man3/Net*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.41-1
- Update to 0.41

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-2
- Perl 5.28 rebuild

* Thu Mar 01 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40-1
- Update to 0.40

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.39-1
- Update to 0.39

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.26 rebuild

* Sun Apr 02 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.38-1
- Update to 0.38

* Sun Mar 26 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.37-1
- Update to 0.37

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.35-1
- Update to 0.35

* Sun Aug 07 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.34-1
- Update to 0.34

* Sun Jul 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.33-1
- Update to 0.33

* Sat Jun 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.32-1
- Update to 0.32

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.24 rebuild

* Thu Apr 28 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.31-1
- Update to 0.31

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.30-1
- Update to 0.30

* Sun Jul 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.29-1
- Update to 0.29

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.22 rebuild

* Sun Mar 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.27-1
- Update to 0.27

* Sun Feb 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.26-1
- Update to 0.26
- Tighten file listing

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.20 rebuild

* Sat Sep 06 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-2
- Perl 5.20 rebuild

* Sun Jul 06 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.24-1
- Update to 0.24

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.22-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Upgrade to 0.22
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.15-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.15-6
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.15-5
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.15-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jul 02 2010 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
- Add missing BR, fix up some strings

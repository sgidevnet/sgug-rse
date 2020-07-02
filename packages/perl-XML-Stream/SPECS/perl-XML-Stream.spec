Name:           perl-XML-Stream
Version:        1.24
Release:        16%{?dist}
Summary:        XML::Stream - streaming XML library
License:        (GPL+ or Artistic) or LGPLv2+
URL:            https://metacpan.org/release/XML-Stream
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAPATRICK/XML-Stream-%{version}.tar.gz
Source1:        LICENSING.correspondance
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if 0%{?_with_network_tests}
# Runtime
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::ProxyAutoConfig)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
%endif
Requires:       perl(HTTP::ProxyAutoConfig)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Net::DNS)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%description
This module provides the user with methods to connect to a remote server, 
send a stream of XML to the server, and receive/parse an XML stream from 
the server.  It is primarily based work for the Etherx XML router 
developed by the Jabber Development Team.  For more information about this 
project visit http://etherx.jabber.org/stream/.  

XML::Stream gives the user the ability to define a central callback that 
will be used to handle the tags received from the server.  These tags are 
passed in the format defined at instantiation time.  the closing tag of an
object is seen, the tree is finished and passed to the call back function.  
What the user does with it from there is up to them.

For a detailed description of how this module works, and about the data 
structure that it returns, please view the source of Stream.pm and 
look at the detailed description at the end of the file.

%prep
%setup -q -n XML-Stream-%{version}
cp %{SOURCE1} .

%build
perl ./Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
%{?_with_network_tests: ./Build test}
rm -rf t/lib

%files
%license LICENSE LICENSING*
%doc CHANGES README INFO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-2
- Perl 5.22 rebuild

* Fri Jan 02 2015 Petr Šabata <contyk@redhat.com> - 1.24-1
- 1.24 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Petr Šabata <contyk@redhat.com> - 1.23-7
- Correct the source URL
- Fix the dependency list
- Modernize the spec a bit

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.23-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.23-2
- Perl 5.16 rebuild

* Mon Jan 23 2012 Petr Šabata <contyk@redhat.com> - 1.23-1
- 1.23 bump
- Spec cleanup
- Removing the unneeded tests patch
- We are noarch, removing optflags

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.22-16
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-14
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-13
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.22-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-9
- fix license tag (technically, it was correct before, but this change prevents
  rpmlint from flagging it as bad in a false positive)

* Mon Jul 14 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.22-8
- add IO::Socket::SSL as a BR/R (see BZ#455344)
- also add Net::DNS
- make tests run if --with network-tests
- misc spec touchups

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-7
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-6.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-6
- bump for mass rebuild

* Sat May 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-5
- bump release, to deal with cvs-import.sh being confused by .rpmmacros

* Thu May 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-4
- include license text, including generated ones
- include correspondance with the module's author

* Wed May 24 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-3
- update license to triple licensed, based on conversations with upstream

* Mon May 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-2
- add CHANGES, README, INFO to docs

* Fri May 12 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-1
- first f-e spec.
- patched the tests to try to connect to the gtalk jabber servers, since the
  default one seemed to be "non-funct"
  

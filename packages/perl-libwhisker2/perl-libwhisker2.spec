%define real_name libwhisker2
Name:           perl-%{real_name}
Obsoletes:      perl-libwhisker <= 1.8
Provides:       perl-libwhisker = %{version}-%{release}
Version:        2.5
Release:        25%{?dist}
Summary:        Perl module geared specifically for HTTP testing
License:        BSD
URL:            http://www.wiretrip.net/rfp/lw.asp
Source0:        http://downloads.sourceforge.net/whisker/%{real_name}-%{version}.tar.gz
#install to vendorlib, not sitelib
Patch0:         %{real_name}-2.4-vendorlib.patch
#include libwhisker1 compatibility bridge
Patch1:         %{real_name}-2.4-lw1bridge.patch
# Perl 5.18 compatibility
Patch2:         %{real_name}-2.5-Editing-iterated-hash-is-undefined.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Pod::Man)
# Run-time:
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
# Tests:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Test::Simple)
# All SSL and network related packages are optional at run time.
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Libwhisker is a Perl library useful for HTTP testing scripts.  It
contains a pure-Perl implementation of functionality found in the LWP,
URI, Digest::MD5, Digest::MD4, Data::Dumper, Authen::NTLM, HTML::Parser,
HTML::FormParser, CGI::Upload, MIME::Base64, and GetOpt::Std modules.
Libwhisker is designed to be portable (a single perl file), fast (general
benchmarks show libwhisker is faster than LWP), and flexible (great care
was taken to ensure the library does exactly what you want to do, even
if it means breaking the protocol).

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Examples how to use LW(2) Perl module.


%prep
%setup -qn %{real_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv compat/{lw,LW}.pm
# Fix EOLs
for F in CHANGES KNOWNBUGS LICENSE README docs/* scripts/*; do
    sed -e 's/\r$//' "$F" > "${F}.new"
    touch -r "$F"{,.new}
    mv "$F"{.new,}
done
# Fix interpreter path
for F in scripts/*.pl; do
    sed -e '1 s|^#!perl|#!/usr/bin/perl|' "$F" > "${F}.new"
    chmod a+x "${F}.new"
    touch -r "$F"{,.new}
    mv "$F"{.new,}
done

%build
make %{?_smp_mflags}

%install
# Create directories, not created by Makefile.pl
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3

make install DESTDIR=$RPM_BUILD_ROOT

# Install documentation
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a docs scripts $RPM_BUILD_ROOT%{_datadir}/%{name}

#fix permissions
chmod 0644 $RPM_BUILD_ROOT/%{perl_vendorlib}/*

%check
cd t 
perl ./test.pl

%files
%doc CHANGES KNOWNBUGS LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man?/*

%files doc
%{_datadir}/%{name}

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-24
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-21
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-13
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.5-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 2.5-9
- Perl 5.18 rebuild
- Perl 5.18 compatibility

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 2.5-6
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.5-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.5-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Aug 11 2010 Petr Pisar <ppisar@redhat.com> - 2.5-1
- 2.5 bump
- License changed from to 2-clause-BSD
- Remove optional Requires.
- Enable tests
- Distribute developer examples in `doc' subpackage

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.4-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4-4
Rebuild for new perl

* Wed May 23 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 2.4-3
- Fix patch to really include lw1 bridge
* Tue May 08 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 2.4-2
- Fix typo in Source0 url
- Update lw1bridge patch to not include License info
- Add explicit version to Provides and Obsoletes
- Added tests, commented out
- Cleaned up BuildRequires and Requires
* Fri May 04 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 2.4-1
- Initial build

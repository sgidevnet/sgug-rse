# require perl-net-sftp only on fedora
%if 0%{?fedora}
%global with_net_sftp        1
%endif

Name:		perl-Net-SFTP-Foreign
Version:	1.91
Release:	2%{?dist}
Summary:	SSH File Transfer Protocol client

License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Net-SFTP-Foreign
Source0:	http://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-SFTP-Foreign-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Dir)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(lib)
BuildRequires:	perl(Math::BigInt)
%{?with_net_sftp:BuildRequires:	perl(Net::SFTP)}
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tie::Handle)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)
BuildRequires:	perl(warnings::register)

Requires:	perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
#Requires:	perl(bytes) # Needed only in Perl <= 5.8.x
Requires:	perl(Encode)
Requires:	perl(IO::Dir)
Requires:	perl(IO::File)
Requires:	perl(IO::Pty)
Requires:	perl(Math::BigInt)
Requires:	perl(Sort::Key)
Requires:	openssh-clients


%{?perl_default_filter}


%description
Net::SFTP::Foreign is a Perl client for the SFTP version 3 as defined in the SSH
File Transfer Protocol IETF draft, draft-ietf-secsh-filexfer-02.txt, included on
this package distribution, on the rfc directory.

Net::SFTP::Foreign uses any compatible ssh command installed on the system (for
instance, OpenSSH ssh) to establish the secure connection to the remote server.

A wrapper module Net::SFTP::Foreign::Compat is also provided for compatibility
with Net::SFTP.


%prep
%setup -q -n Net-SFTP-Foreign-%{version}
rm lib/Net/SFTP/Foreign/Backend/Windows.pm
# Normalize end-of-lines
for F in rfc/draft-ietf-secsh-scp-sftp-ssh-uri-04.txt; do
    tr -d "\r" < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc Changes README debug.txt TODO rfc samples
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.91-2
- Perl 5.32 re-rebuild updated packages

* Wed Jun 24 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.91-1
- new  release 1.91

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.90-4
- put back missing parenthesis in perl-net-sftp buildrequires

* Sat Oct 12 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.90-3
- sync changes from epel7 branch specfile into master
- do not buildrequire perl-net-sftp on epel

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-1
- 1.90 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.89-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.89-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.89-2
- Perl 5.28 rebuild

* Tue Feb 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.89-1
- 1.89 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 24 2017 Paul Howarth <paul@city-fan.org> - 1.87-2
- Perl 5.26 rebuild

* Thu Apr 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.87-1
- 1.87 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Petr Pisar <ppisar@redhat.com> - 1.86-1
- 1.86 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-1
- 1.81 bump

* Thu Jul 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-1
- 1.77 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.75-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-6
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.75-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.75-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.75-1
- Updated to latest stable version

* Mon Mar 04 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.74.05-5
- Removed dependency that brakes builds

* Mon Mar 04 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.74.05-4
- Fixed dependency mistake

* Fri Mar 01 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.74.05-3
- Added missing runtime dependencies

* Sun Feb 24 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.74.05-2
- Fixed incorrect dependency line

* Mon Feb 18 2013 Normunds Neimanis <fedorapkg at rule.lv> 1.74.05-1
- Package for current Fedora

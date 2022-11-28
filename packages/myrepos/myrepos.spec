Name:           myrepos
Version:        1.20180726
Release:        4%{?dist}
Summary:        A multiple SCM repository management tool

License:        GPLv2+
URL:            https://github.com/joeyh/myrepos
Source0:        https://git.joeyh.name/index.cgi/myrepos.git/snapshot/myrepos-%{version}.tar.gz
Source1:        README.fedora
BuildArch:      noarch

Provides:       mr = %{version}-%{release}
Obsoletes:      mr < 1.15-6

BuildRequires:  perl-generators
BuildRequires:  perl-podlators

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Out off the box only git is supported. For additional details the 
# README.fedora lists the supported SCM tools. 
Requires:       git

%description
The mr command can checkout, update, or perform other actions on
a set of repositories as if they were one combined repository. It
supports any combination of subversion, git, cvs, mecurial, bzr and
darcs repositories, and support for other revision control systems
can easily be added.

%prep
%setup -q
cp %{SOURCE1} .

%build
make %{?_smp_mflags}

%install
install -Dp -m 0755 mr %{buildroot}%{_bindir}/mr
for file in mr.1 webcheckout.1; do
    install -Dp -m 0644 $file %{buildroot}%{_mandir}/man1/$file
done
for file in lib/git-fake-bare lib/git-svn lib/unison; do
    install -Dp -m 0644 $file %{buildroot}%{_datadir}/mr/$file
done

%files
%doc README mrconfig mrconfig.complex README.fedora
%license GPL
%{_mandir}/man1/*.*
%{_bindir}/mr
%{_datadir}/mr/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20180726-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180726-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.20180726-1
- Fixes for CVE-2018-7032 (rhbz#1383312, rhbz#1383313)
- Update to new upstream version 1.20180726

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171231-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.20171231-2
- Perl 5.28 rebuild

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.20171231-1
- Update to new upstream version 1.20171231

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160123-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160123-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20160123-4
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20160123-2
- Perl 5.24 rebuild

* Tue Feb 02 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.20160123-1
- Update to new upstream version 1.20160123

* Fri Nov 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.20151022-1
- Update to new upstream version 1.20151022 (rhbz#1278814)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20141024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20141024-2
- Perl 5.22 rebuild

* Sun Jan 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.20141024-1
- Update to new upstream version 1.20141024

* Wed Oct 08 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.20140831.1-2
- Add git
- Add README for Fedora

* Tue Oct 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.20140831.1-1
- Rename package accordig upstream
- Update to latest upstream release 1.20140831.1

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.15-2
- Perl 5.18 rebuild

* Sun Jun 16 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-1
- Update to new upstream version 1.15

* Sat Feb 23 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-3
- Update BR

* Tue Feb 19 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-2
- Fix bogus date entries

* Sun Feb 17 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-1
- Update to new upstream version 1.14

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to new upstream version 1.13

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.12-2
- Perl 5.16 rebuild

* Thu Jun 14 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Update to new upstream version 1.12

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.11-2
- Perl 5.16 rebuild

* Thu Apr 05 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.11-1
- Update to new upstream version 1.11

* Fri Feb 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-1
- Update to new upstream version 1.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.05-1
- Update to new upstream version 1.05

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.04-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.04-2
- Perl mass rebuild

* Sun Jul 03 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.04-1
- Update to new upstream version 1.04

* Sun Jun 19 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.03-1
- Update to new upstream version 1.03

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-3
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-2
- Perl 5.14 mass rebuild

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.02-1
- Update to new upstream version 1.02

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.51-2
- Rebuilt

* Wed Dec 29 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.51-1
- Update to new upstream version 0.51 

* Tue Nov 02 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.50-1
- Update to new upstream version 0.50 

* Fri Aug 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.49-1
- Update to new upstream version 0.49

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.48-2
- Mass rebuild with perl-5.12.0

* Fri Mar 05 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.48-1
- Update to new upstream version 0.48

* Fri Dec 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.46-1
- Update to new upstream version 0.46

* Mon Dec 07 2009 Stepan Kasal <skasal@redhat.com> - 0.43-2
- Rebuild against perl 5.10.1

* Thu Sep 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.43-1
- Update to new upstream version 0.43

* Sat Aug 22 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.42-1
- Add new man page
- Update to new upstream version 0.42

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.39-1
- Update to new upstream version 0.39

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.38-1
- Update to new upstream version 0.38

* Fri Jan 02 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.35-2
- Patch for the man pages

* Sat Dec 27 2008 Fabian Affolter <mail@fabian-affolter.ch> - 0.35-1
- Initial package for Fedora

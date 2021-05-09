Name:         stow
Version:      2.3.0
Release:      3%{?dist}

License:      GPLv3+
URL:          https://www.gnu.org/software/stow/stow.html
Summary:      Manage the installation of software packages from source
Source:       https://ftp.gnu.org/gnu/stow/stow-%{version}.tar.bz2
BuildArch:    noarch

BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# Run-time dependencies
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone::Choose)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test dependencies
# Data::Dumper no longer provided by base perl in F18+
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
GNU Stow is a program for managing the installation of software packages,
keeping them separate (/usr/local/stow/emacs vs. /usr/local/stow/perl, for
example) while making them appear to be installed in the same place
(/usr/local). Software to ease the keeping track of software built from
source, making it easy to install, delete, move etc.

%package doc
Summary:    Documentation for Stow
Requires:   %{name} = %{version}-%{release}

%description doc
This package contains the documentation for GNU Stow.

%if 0%{?fedora} >= 20
%global moredocs %{_defaultdocdir}/stow-doc
%else
%global moredocs %{_defaultdocdir}/stow-doc-%{version}
%endif

%prep
%autosetup

%build
%configure --docdir=%{moredocs} --with-pmdir=%{perl_vendorlib}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
# Remove info database, will be generated at install-time by scriptlets
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Remove unnecessary documentation
cd $RPM_BUILD_ROOT%{moredocs}/
rm -f ChangeLog* README.md INSTALL.md version.texi

%check
make check

%files
%doc README.md AUTHORS ChangeLog NEWS THANKS TODO
%doc %{_mandir}/man8/stow*
%doc %{_infodir}/stow*
%license COPYING
%{_bindir}/*
%{perl_vendorlib}/Stow.pm
%{perl_vendorlib}/Stow/

%files doc
%docdir %{moredocs}
%dir %{moredocs}
%{moredocs}/manual.pdf
%{moredocs}/manual-single.html
%{moredocs}/manual-split/


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.3.0-2
- Own stow-doc directory

* Sat Jun 29 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (#1725282)
- License updated to GPLv3+

* Wed Jun 12 2019 Petr Pisar <ppisar@redhat.com> - 2.2.2-8
- Install Perl files to a standard Perl path

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Robin Lee <cheeselee@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2
- BR: perl(IO::Scalar), perl(Carp), perl(IO::File), perl(Module::Build)
- Drop upstreamed avoid-precedence-warning.patch

* Wed Oct 28 2015 Robin Lee <cheeselee@fedoraproject.org> - 2.2.0-9
- Fix Perl 5.20 warning (BZ#1226473)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Michel Salim <salimma@fedoraproject.org> - 2.2.0-6
- Adjust documentation directory on Fedora >= 20
- spec clean-up: remove BuildRoot declaration and clean section

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 2.2.0-4
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Michel Salim <salimma@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.3.3-6
- fix license tag

* Thu Aug 31 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.3.3-5
- rebuild

* Tue Jun 20 2006 Aurelien Bompard <gauret[AT]free.fr> 1.3.3-4
- remove the _infodir/dir file in %%install

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 1.3.3-3
- rebuild for FC5

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat May 15 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.3.3-0.fdr.1
- initial RPM

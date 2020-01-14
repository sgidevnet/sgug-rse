Summary:        Internationalization library for Perl, compatible with gettext
Name:           perl-libintl-perl
Version:        1.31
Release:        4%{?dist}
# gettext_xs/gettext_xs.pm:     GPLv3+
# gettext_xs/Makefile.PL:       LGPLv2+
# lib/Locale/gettext_xs.pod:    LGPLv2+
# lib/Locale/RecodeData.pm:     GPLv3+
# lib/Locale/libintlFAQ.pod:    LGPLv2+
# COPYING:                      GPLv3+
License:        GPLv3+ and LGPLv2+
URL:            https://metacpan.org/release/libintl-perl
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/libintl-perl-%{version}.tar.gz
# this module was renamed in the f25 dev cycle
Provides:       perl-libintl = %{version}-%{release}
Obsoletes:      perl-libintl < 1.25

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
#BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
# Optional run-time:
#BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(I18N::Langinfo)
# Tests:
# Needed for tests/03bind_textdomain_codeset_pp.t
#BuildRequires:  glibc-langpack-de
# Needed for tests/04find_domain_bug.t
#BuildRequires:  glibc-langpack-en
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Encode::Alias)
Requires:       perl(POSIX)
Recommends:     perl(File::ShareDir)
Recommends:     perl(I18N::Langinfo)

%{?perl_default_filter}

%description
The package libintl-perl is an internationalization library for Perl that
aims to be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.


%prep
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export PERL=%{_bindir}/perl
%setup -q -n libintl-perl-%{version}
find -type f -exec chmod -x {} \;
find lib/Locale gettext_xs \( -name '*.pm' -o -name '*.pod' \) \
    -exec sed -i -e '/^#! \/bin\/false/d' {} \;
# Fix rpmlint errors and warnings
cd sample/simplecal
sed -i -e '1i#!%{_bindir}/perl' bin/simplecal.pl Makefile.PL
# A hack around non-functional iconv
#for file in po/*.po; do
#    %{_bindir}/iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
#    mv $file.new $file
#done
rm .gitignore MANIFEST


%build
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export PERL=%{_bindir}/perl
%{_bindir}/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export PERL=%{_bindir}/perl
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f \( -name .packlist -o \
                  -name '*.bs' -size 0 \) -delete
%{_fixperms} %{buildroot}

%check
export SHELL=%{_bindir}/sh
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export PERL=%{_bindir}/perl
make test

%files
%license COPYING
%doc Changes Credits FAQ NEWS README REFERENCES THANKS TODO
%doc sample
%{perl_vendorlib}/Locale/
%{perl_vendorarch}/auto/Locale/
%{_mandir}/man?/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.31-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.31-1
- Update to 1.31
- Whitelist known rpmlint errors

* Tue Nov 06 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.30-1
- Update to 1.30

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-4
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-3
- Run the tests with LANG=en_US to ensure we use the right dictionary

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.29-1
- Update to 1.29

* Sun Sep 03 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.28-1
- Update to 1.28

* Sun Aug 13 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.27-1
- Update to 1.27
- Drop upstreamed patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-4
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 1.26-3
- Fix building on Perl without "." in @INC (CPAN RT#120446)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.26-1
- Update to 1.26

* Wed May 25 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.25-2
- Take into account the re-review comments (#1339004)

* Sat May 21 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.25-1
- Update package to 1.25-1
- Rename package to perl-libintl-perl, the module's name on CPAN
- Trim changelog

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump
- License changed from (LGPLv2+) to (GPLv3+ and LGPLv2+)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-17
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-16
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.20-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Petr Šabata <contyk@redhat.com> - 1.20-10
- Add some missing BRs
- Modernize the spec
- Drop command macros

* Thu Oct 11 2012 Petr Pisar <ppisar@redhat.com> - 1.20-9
- Do not provide private library
- Drop unneeded build-time dependencies
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.20-7
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.20-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-2
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 1.20-1
- new upstream version
- better buildroot

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.16-11
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.16-8
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.16-7
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.16-6
- rebuild for new perl

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.16-5
- Rebuild for new BuildID feature.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.16-4
- Update License field.
- Add perl(ExtUtils::MakeMaker) build requirement.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.16-3
- FC6 rebuild.
- Change spec file back to my own liking...

* Sat Feb 11 2006 Ralf Corsépius <rc040203@freenet.de>  1.16-2
- Rework spec (PR 180767).

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.16-1
- Update to 1.16.

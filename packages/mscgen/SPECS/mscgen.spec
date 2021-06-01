Name:           mscgen
Version:        0.20
Release:        26%{?dist}
Summary:        Message Sequence Chart rendering program
License:        GPLv2+
URL:            http://www.mcternan.me.uk/mscgen/
Source0:        http://www.mcternan.me.uk/mscgen/software/%{name}-src-%{version}.tar.gz

# Removes unknown escape sequence '\-'
# Patch sent upstream.
# http://code.google.com/p/mscgen/issues/detail?id=72
Patch0:         %{name}-0.20-escape.patch

# Fixes 'ymax' variable initialization
# http://code.google.com/p/mscgen/issues/detail?id=73
Patch1:         %{name}-0.20-uninitialized-ymax.patch

# Fixes language.c:464:5: error: conflicting types for 'yyparse'
# https://code.google.com/p/mscgen/issues/detail?id=83
Patch2:         %{name}-0.20-language.patch

%global test_with_valgrind %{?_with_valgrind:1}%{!?_with_valgrind:0}


BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig
BuildRequires:  gd-devel
BuildRequires:  freetype-devel
BuildRequires:  urw-base35-fonts

%if %{test_with_valgrind}
BuildRequires:  valgrind
%endif

# Freetype based font rendering requires some fonts to be installed.
Requires:       urw-base35-fonts


%description
Mscgen is a small program that parses Message Sequence Chart descriptions
and produces PNG, SVG, EPS or server side image maps (ismaps) as the output.
Message Sequence Charts (MSCs) are a way of representing entities and
interactions over some time period and are often used in combination with SDL.
MSCs are popular in Telecoms to specify how protocols operate although MSCs
need not be complicated to create or use. Mscgen aims to provide a simple text
language that is clear to create, edit and understand, which can also be
transformed into common image formats for display or printing.


%prep
%setup -q
%patch0 -p1 -b .escape
%patch1 -p1 -b .initialization
%patch2 -p1 -b .language
#this ensures that they get regenerated
rm -f src/language.{c,h} src/lexer.c


%build
# Correct EOL.
sed 's/\r//' TODO >TODO.tmp && touch -r TODO TODO.tmp && mv TODO.tmp TODO
%configure \
    --with-freetype \
    --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}


%check
%if %{test_with_valgrind}
export VALGRIND="valgrind -v --track-origins=yes --tool=memcheck"
%endif
make check


%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
cp -p TODO %{buildroot}%{_defaultdocdir}/%{name}/


%files
# due to this entry, doc must not be used to add any other files
%{_defaultdocdir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.20-23
- Add missing BR (gcc)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 0.20-18
- Rebuild (libwebp)

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 0.20-17
- rebuild to drop libvpx dep

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 0.20-15
- rebuild for libvpx 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 0.20-13
- rebuild against libvpx 1.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.20-11
- Fixes FTBFS, rhbh#1106246.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.20-9
- changes for unversioned doc directory, fixes rhbz#993979,
- preserving timestamp during EOL conversion added.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0.20-7
- rebuild for new GD 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.20-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.20-4
- rebuild against new libjpeg

* Mon Aug 16 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.20-3
- use force option while removing files,
- install TODO file,
- use %%{name} macro on PatchX,
- preserve timestamps while installing files,
- add a comment about the uwr-fonts requirement,
- backport fix for variable initialization.

* Fri Jul 20 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.20-2
- remove superfluous spaces from the spec file,
- correct the Group,
- use consistently marcos,
- unknown escape sequence removal patch added,
- remove files which has to be regenerated,
- build with the free-type support,
- add a possibility to run tests under valgrind.

* Mon Jan 3 2011 Michael McTernan <Michael.McTernan.2001@cs.bris.ac.uk> 0.19-2
- Add comment in spec file warning of doc use.

* Wed Sep 15 2010 Michael McTernan <Michael.McTernan.2001@cs.bris.ac.uk> 0.19-1
- Version bump following upstream release.

* Tue Sep 07 2010 Michael McTernan <Michael.McTernan.2001@cs.bris.ac.uk> 0.18-3
- Further Fedora packaging fixes to remove duplicate doc (bug #630754#c4).

* Tue Sep 07 2010 Michael McTernan <Michael.McTernan.2001@cs.bris.ac.uk> 0.18-2
- Fixes from Fedora packaging review (bug #630754).

* Thu Aug 25 2010 Michael McTernan <Michael.McTernan.2001@cs.bris.ac.uk> 0.18-1
- Initial version.

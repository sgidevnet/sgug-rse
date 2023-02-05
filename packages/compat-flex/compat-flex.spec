Summary: Legacy version of flex, a tool for creating scanners
Name: compat-flex
Version: 2.5.4a
Release: 22%{?dist}
License: BSD
URL: http://www.gnu.org/software/flex/
Source: http://downloads.sourceforge.net/flex/flex-%{version}.tar.bz2
Source2: README.fedora
Patch0: flex-2.5.4a-skel.patch
Patch1: flex-2.5.4-glibc22.patch
Patch2: flex-2.5.4a-gcc3.patch
Patch3: flex-2.5.4a-gcc31.patch
Patch4: flex-2.5.4a2.patch
Patch5: flex-pic.patch
Patch6: flex-2.5.4a2-std.patch
Patch7: flex-2.5.4a2-warn.patch
Patch8: flex-2.5.4a2-shapwarn.patch
Patch9: flex-2.5.4a2-iniscan.patch
Patch10: flex-2.5.4a-Makefile.in.patch
Patch11: flex-2.5.4a-texinfo-section.patch
BuildRequires:  gcc
BuildRequires: autoconf byacc texinfo info

%description

This is legacy version of flex, a program that generates scanners.
Scanners are programs which can recognize lexical patterns in text.
Flex takes pairs of regular expressions and C code as input and
generates a C source file as output.  The output file is compiled and
linked with a library to produce an executable.  The executable
searches through its input for occurrences of the regular expressions.
When a match is found, it executes the corresponding C code.  Flex was
designed to work with both Yacc and Bison, and is used by many
programs as part of their build process.

You should install flex if you are going to use your system for
application development.

%prep
%setup -q -n flex-2.5.4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch9 -p1
%patch10 -p1
%patch11 -p1
cp %{SOURCE2} .

%build
autoconf
%configure
sed -i '/^START-INFO-DIR-ENTRY/,/^END-INFO-DIR-ENTRY/s/[Ff]lex/&-%{version}/g' ./MISC/texinfo/flex.texi
make FLEX=flex-%{version}
makeinfo MISC/texinfo/flex.texi -o MISC/texinfo/flex-%{version}.info

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} FLEX=flex-%{version} libdir=$RPM_BUILD_ROOT/%{_libdir}/flex-%{version} mandir=$RPM_BUILD_ROOT/%{_mandir}/man1
./mkinstalldirs $RPM_BUILD_ROOT/%{_infodir} $RPM_BUILD_ROOT/%{_includedir}/flex-%{version}
install -m 644 MISC/texinfo/flex-%{version}.info $RPM_BUILD_ROOT/%{_infodir}/flex-%{version}.info
mv ${RPM_BUILD_ROOT}/%{_includedir}/FlexLexer.h ${RPM_BUILD_ROOT}/%{_includedir}/flex-%{version}/FlexLexer.h
ln -s flex-%{version}.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/flex-%{version}++.1

%check
echo ============TESTING===============
make FLEX=flex-%{version} bigcheck
echo ============END TESTING===========

%files
%doc COPYING NEWS README README.fedora
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/flex-%{version}
%{_includedir}/flex-%{version}
%{_infodir}/flex-%{version}.info*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Petr Machata <pmachata@redhat.com> - 2.5.4a-11
- Fix "raising the section level of @section" bug that texinfo 5.0
  complains about (flex-2.5.4a-texinfo-section.patch)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.4a-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.5.4a-3
- Rebuild for selinux ppc32 issue.

* Fri Jul 06 2007 Florian La Roche <laroche@redhat.com> - 2.5.4a-2
- add install-info requirement for post/preun

* Wed Jan 18 2006 Petr Machata <pmachata@redhat.com> - 2.5.4a-1
- Initial build.

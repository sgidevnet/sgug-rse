Name:          par
Version:       1.52
Release:       26%{?dist}
Summary:       Paragraph reformatter, vaguely like fmt, but more elaborate
License:       Par
URL:           http://www.nicemice.net/par/
Source0:       http://www.nicemice.net/par/Par152.tar.gz
Patch0:        par.c.diff
BuildRequires: gcc

%description
par is a filter which copies its input to its output, changing all
white characters (except newlines) to spaces, and reformatting each
paragraph.  Paragraphs are separated by protected, blank, and bodiless
lines (see the man page Terminology section for definitions), and
optionally delimited by indentation (see the d option in the Options
section).  Each output paragraph is generated from the corresponding
input paragraph as follows:

  1) An optional prefix and/or suffix is removed from each input line.
  2) The remainder is divided into words (separated by spaces).
  3) The words are joined into lines to make an eye-pleasing paragraph.
  4) The prefixes and suffixes are reattached.

If there are suffixes, spaces are inserted before them so that they
all end in the same column.


%prep
%setup -q -n Par152
%patch0 -p 1


%build
make -f protoMakefile CC="gcc -c $RPM_OPT_FLAGS"


%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install par %{buildroot}/%{_bindir}
install -m 644 par.1 %{buildroot}/%{_mandir}/man1


%files
%{_bindir}/par
%{_mandir}/man1/par.1*
%doc par.doc releasenotes


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 David Levine <par.packager@gmail.com> - 1.52-23
- Added BuildRequires: gcc.
- Updated spec file preamble to conform to spec file reference.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 David Levine <par.packager@gmail.com> - 1.52-15
- Removed all par_1.52-i18n patches because they still have bugs [Bug 962221].

* Thu Dec 25 2014 David Levine <par.packager@gmail.com> - 1.52-14
- Added protection against null dereference to previous patch.

* Wed Dec 24 2014 David Levine <par.packager@gmail.com> - 1.52-14
- Added patch to fix segfault with multibyte characters [Bug 962221].

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.52-11
- Don't create unneeded doc dir in %%install.

* Sun May 05 2013 David Levine <par.packager@gmail.com> - 1.52-10
- Added patch to fix mixing byte string and wide string I/O [Bug 959794].

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 David Levine <par.packager@gmail.com> 1.52-7
- Removed -s from install of executable.  Changed summary to
  be less pretentious.

* Sun Jul 08 2012 David Levine <par.packager@gmail.com> 1.52-6
- Moved executable to /usr/bin/par because par2cmdline removed
  the conflict, as of Fedora 18.

* Tue May 15 2012 David Levine <par.packager@gmail.com> 1.52-5
- Moved executable to /usr/lib/par/.

* Tue Apr 17 2012 David Levine <par.packager@gmail.com> 1.52-4
- Addressed first round of comments on the spec.
- Restored -s in install of executable.  That is much more consistent
- with what is already in /usr/bin, and removes an rpmlint warning.

* Mon Apr 16 2012 David Levine <par.packager@gmail.com> 1.52-3
- In response to comments about packaging:  renamed binary to
- parr to avoid conflict with par2cmdline, and removed -s from
- install.

* Sun Apr 15 2012 David Levine <par.packager@gmail.com> 1.52-2
- Packaged for Fedora.  Borrowed from the Madriva spec of
- Thierry Vignaud <tvignaud@mandriva.com>.  Added the two patches.

* Tue Dec 30 2003 - Volker Kuhlmann <VolkerKuhlmann@gmx.de>
- Package available from: http://volker.dnsalias.net/soft/
- for SuSE 8.2
- initial package version

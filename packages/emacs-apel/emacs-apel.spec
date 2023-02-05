%global		pkg		apel
%global		pkgname		APEL

Name:		emacs-%{pkg}
Version:	10.8
Release:	17%{?dist}
Summary:	A Portable Emacs Library

License:	GPLv2+
URL:		http://cvs.m17n.org/elisp/APEL/index.en.html
Source0:	http://kanji.zinbun.kyoto-u.ac.jp/~tomo/lemi/dist/apel/%{pkg}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}
Provides:	apel = %{version}-%{release}
Obsoletes:	apel < 10.8-1
Provides:	emacs-apel-el <= 10.8-8
Obsoletes:	emacs-apel-el <= 10.8-8

Patch0:		APEL-CFG.patch
Patch1:		apel-10.4-missing-el.patch
Patch2:		%{name}-ikazuhiro.patch
Patch3:		%{name}-prevent-fontset-error.patch
Patch4:		%{name}-fix-old-backquote.patch
Patch5:		%{name}-escape-doc.patch

%description
%{pkgname} (A Portable Emacs Library) is a library to support
to write portable Emacs Lisp programs.

%prep
%autosetup -n %{pkg}-%{version} -p1

%build


%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} \
	INSTALL="install -p"  install

%files
%doc README.en ChangeLog
%lang(ja) %doc README.ja
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Akira TAGOH <tagoh@redhat.com> - 10.8-15
- Escape characters in doc.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Tue Jun 23 2015 Akira TAGOH <tagoh@redhat.com> - 10.8-9
- Merge -el sub-package into main (#1234536)
- Borrow some packages from Debian.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Akira TAGOH <tagoh@redhat.com> - 10.8-1
- New upstream release.
- Rename the package to meet the packaging guidelines.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  1 2008 Akira TAGOH <tagoh@redhat.com> - 10.7-2
- Update the spec file.

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 10.7-1
- New upstream release.
- Update License tag.

* Fri Sep 15 2006 Akira TAGOH <tagoh@redhat.com> - 10.6-9
- rebuilt

* Wed Jul 20 2005 Akira TAGOH <tagoh@redhat.com> - 10.6-8.fc5
- Disabled apel-xemacs package to avoid a chicken-egg problem.

* Tue Jul 19 2005 Akira TAGOH <tagoh@redhat.com> - 10.6-7.fc5
- Import into Extras.

* Tue Feb 22 2005 Elliot Lee <sopwith@redhat.com> 10.6-6
- Remove xemacs

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-5
- require emacs-common instead of emacs.

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-4
- require xemacs-common instead of xemacs. (#134479)

* Mon Sep 27 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jul 07 2003 Akira TAGOH <tagoh@redhat.com> 10.6-1
- New upstream release.

* Wed May 14 2003 Akira TAGOH <tagoh@redhat.com> 10.4-4
- apel-10.4-missing-el.patch: contains atype.el and file-detect.el (#90604)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan  3 2003 Jens Petersen <petersen@redhat.com> 10.4-2
- rebuild

* Wed Jan  1 2003 Jens Petersen <petersen@redhat.com> 10.4-1
- update to 10.4
- resurrect -xemacs subpackage, required by latest xemacs package
- install xemacs package under datadir
- own xemacs package lisp dir

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 10.3-8
- rebuild

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 10.3-7
- s/Copyright/License/
- add the owned directory.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Feb 24 2002 Tim Powers <timp@redhat.com>
- rebuilt in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- apel-xemacs removed because XEmacs already includes it.
- made "emu" modules installed in apel/ subdirectory

* Wed Jun 20 2001 SATO Satoru <ssato@redhat.com>
- initial release (separated from semi)

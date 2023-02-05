# $Id: rblcheck.spec,v 1.16 2005/07/01 10:41:31 oliver Exp $

Name:		rblcheck
Summary:	Command-line interface to RBL-style listings

Version:	1.5
Release:	34%{?dist}

Source0:	https://github.com/logic/rblcheck/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	rblcheckrc

License:	GPLv2+
URL:		https://github.com/logic/rblcheck


# Change the text "RBL filtered by" to "listed by"
# (RBL is a trademark of MAPS LLC.)
# 'listed by' is more accurate
Patch0:		rblcheck-texttweak.patch

# Fix broken code for looking up TXT records, code borrowed
# from Ian Gulliver's "firedns" library (GPL), which can be found at:
# http://firestuff.org/
Patch1:		rblcheck-txt.patch

# Comes from a post to the rblcheck users mailing list. See:
# http://sourceforge.net/mailarchive/forum.php?thread_id=1371771&forum_id=4256
Patch2:		rblcheck-names.patch

# Compile fix for x86_64 systems
Patch3:		rblcheck-1.5-res_query.patch

BuildRequires:	docbook-utils, gcc

%description
rblcheck is a very basic interface to RBL-style DNS listings such as those
operated by the MAPS (http://www.mail-abuse.org/) and ORBL
(http://www.orbl.org/) projects.

%prep
%setup -q

%patch0 -p1 -b .texttweak
%patch1 -p0 -b .txt
%patch2 -p0 -b .names
%patch3 -p1 -b .res_query

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%{__install} -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rblcheckrc

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%doc docs/rblcheck.ps docs/rblcheck.rtf docs/html/
%{_bindir}/rbl
%{_bindir}/rblcheck
%config(noreplace) %{_sysconfdir}/rblcheckrc

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Oliver Falk <oliver@linux-kernel.at> - 1.5-33
- Add gcc to BuildRequires
- Update URLs; rblcheck no lives on GitHub

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-30
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.5-15
- Bump-n-build for GCC 4.3

* Mon Oct 22 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.5-14
- Fixed URL
- Not rebuilding right now :-)

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.5-13
- Rebuild for BuildID
- License clarification

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.5-12
- Bump-n-build

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org>	- 1.5-11
- Bump for FC6 rebuild

* Fri Jul 01 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-10
- Add compile fix patch for x86_64

* Wed Jun 29 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-9
- Applied patch from Matthias (readability changes in specfile)

* Mon May 23 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-8
- Fix defattr (permissions)

* Sat May 21 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-7
- Even more changes that Paul suggested
- Remove the faulty lists
- Fix rpmlint warnings

* Fri May 20 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-6
- Integrate more changes from Paul:
- Changed URL for MAPS (only spec related change)
- Add BuildRequires: docbook-utils
- Remove INSTALL from %%doc section, as it is generic and not
  of any use to and end usser
- Remove duplicates from rblcheckrc (thanks Paul for mentioning!)
- Added xbl.spamhaus.org to the rblcheckrc
- Removed dead lists (dev.null.dk, monkeys.com, dorkslayers.com) from
  the rblcheckrc

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-5
- Move setting of default list from the patch to
  %%{_sysconfdir}/rblcheckrc, which is easier to maintain

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-4
- Integrated patches Paul Howarth suggested

* Fri Mar 25 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-3.2
- Fix rpmlint warnings

* Thu Mar 24 2005 Oliver Falk <oliver@linux-kernel.at>		- 1.5-3.1
- Rebuild

* Thu Sep 16 2004 Oliver Falk <oliver@linux-kernel.at>		- 1.5-3
- Name changed
- Added packager

* Wed Sep 08 2004 Oliver Pitzeier <oliver@linux-kernel.at>	- 1.5-2
- Cleanup

* Mon Apr  2 2001 Edward S. Marshall <esm@logic.net>
- Created this RPM spec.


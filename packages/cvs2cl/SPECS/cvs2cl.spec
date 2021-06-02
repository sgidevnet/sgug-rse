Name:           cvs2cl
Version:        2.73
Release:        18%{?dist}
Summary:        Generate ChangeLogs from CVS working copies

License:        GPLv2+
URL:            http://www.red-bean.com/cvs2cl/
# To update the sources:
# spectool -g -f cvs2cl.spec
# md5sum -c sources
# fedpkg upload (all the sources which don't match)
# (remove the old ones from 'sources')
Source0:        http://www.red-bean.com/cvs2cl/cvs2cl.pl
Source1:        http://www.red-bean.com/cvs2cl/changelog.dtd
Source2:        http://www.red-bean.com/cvs2cl/changelog-xml-schema.xdr
Source3:        http://www.red-bean.com/cvs2cl/cl2html.xslt
Source4:        http://www.red-bean.com/cvs2cl/cl2html-ciaglia.xslt
Source5:        http://www.red-bean.com/cvs2cl/filter-cvs2cl.xslt
Source6:        http://www.red-bean.com/cvs2cl/cvs2cl_ruether.xslt
Source7:        http://www.red-bean.com/cvs2cl/cl2html_rss-karaguezian.xslt
Source8:        http://www.red-bean.com/cvs2cl/ChangeLog.xsd
Patch0:         %{name}-2.69-perldeps.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/pod2man
# HACK: Pull-in perl-filter macros
BuildRequires:  perl-generators
BuildRequires:  perl-macros
Requires:       xml-common

%if 0%{?perl_default_filter_revision} > 2
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CVS::Utils::ChangeLog::.*\\)
%else
%{?filter_setup:
%filter_from_requires /^perl(CVS::Utils::ChangeLog::.*)/d
%{?perl_default_filter}
}
%endif

%description
cvs2cl generates GNU-style ChangeLogs for a CVS working copy using the
output of the "cvs log" command.  The script originally came from the
open source CVS book at http://cvsbook.red-bean.com/.


%prep
%setup -c -T
sed -e 's/cvs2cl\.pl/cvs2cl/' %{SOURCE0} > cvs2cl
%patch0


%build
%{_bindir}/pod2man \
  --section=1 \
  --release=%{version} \
  --center="CVS-log-message-to-ChangeLog conversion script" \
  cvs2cl > cvs2cl.1


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xml/cvs2cl,%{_mandir}/man1}
install -p -m 755 cvs2cl $RPM_BUILD_ROOT%{_bindir}/cvs2cl
install -p -m 644 \
  %{SOURCE1} \
  %{SOURCE2} \
  %{SOURCE3} \
  %{SOURCE4} \
  %{SOURCE5} \
  %{SOURCE6} \
  %{SOURCE7} \
  %{SOURCE8} \
  $RPM_BUILD_ROOT%{_datadir}/xml/cvs2cl
install -p -m 644 cvs2cl.1 $RPM_BUILD_ROOT%{_mandir}/man1



%files
%{_bindir}/cvs2cl
%{_datadir}/xml/cvs2cl/
%{_mandir}/man1/cvs2cl.1*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.73-13
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.73-9
- Fix for perl-macros layout change (#1106110)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.73-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.73-2
- Fix Requires filtering for Fedora ≥ 16 (perl_default_filter_revision 3)

* Sat Nov 12 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.73-1
- Update to 2.73 (#753407)

* Tue Mar 08 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.72-6
- Add %%{?dist} to release tag.

* Tue Mar 08 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.72-5
- Add perl-filter to filter out bogus R: perl(CVS::ChangeLog::*).
- BR: /etc/rpm/macros.perl.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 2.72-1
- 2.72.

* Sat May 17 2008 Ville Skyttä <ville.skytta at iki.fi> - 2.71-1
- 2.71, man page patch applied upstream.

* Sat May 17 2008 Ville Skyttä <ville.skytta at iki.fi> - 2.69-1
- 2.69.
- Drop disttag.

* Mon Aug 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 2.67-1
- 2.67 + man page fix.
- Fix spelling error in %%description.
- License: GPLv2+

* Tue Apr 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 2.62-1
- 2.62.

* Sat Mar 31 2007 Ville Skyttä <ville.skytta at iki.fi> - 2.60-1
- 2.60.
- Dependency fixups.

* Fri Dec 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.59-5
- Eliminate unnecessary file based dependencies.

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.59-4
- Add XSD from Yury Lebedev.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.59-3
- Don't own %%{_datadir}/xml, require it instead.
- Make docs and usage message refer to cvs2cl (sans .pl).

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.59-2
- 2.59.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.58-1
- rebuilt

* Sun Jan 16 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.58-1
- Updated to 2.58.

* Sat Jul 10 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.57-0.fdr.1
- Updated to 2.57.
- Moved XML and XSLT files from _datadir/sgml to _datadir/xml.
- Added cvs2cl_ruether.xslt.

* Fri Jun  4 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.55-0.fdr.1
- Updated to 2.55.
- Added cl2html_rss-karaguezian.xslt.

* Tue Mar 16 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:2.53-0.fdr.1
- Updated to 2.53.

* Sat Feb 28 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.52-0.fdr.2
- Generate and include a man page.
- Include a couple of new upstream XSLs (pretty HTML, RSS).

* Sun Jan 25 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.52-0.fdr.1
- Updated to 2.52.
- Converted spec file to UTF-8.

* Sat Dec 13 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.51-0.fdr.1
- Updated to 2.51.
- Removed build req perl.

* Tue Sep  9 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.50-0.fdr.4
- Minor editing of package description.

* Mon Sep  8 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.50-0.fdr.3
- Preserve timestamps of installed files (bug 673).
- Actually updating cvs2cl to version 2.50, also proved to be a good idea (bug 673).

* Mon Sep  8 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.50-0.fdr.2
- Added cl2html.xslt (bug 673).
- More template adjustments; use RPM_BUILD_ROOT instead of buildroot (bug 673).

* Wed Sep  3 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 0:2.50-0.fdr.1
- Updated to 2.50.
- Added epoch and edited to match current template.

* Mon Jul 21 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 2.49-0.fdr.3
- Moved DTD and XML schema to {_datadir}/sgml/cvs2cl.

* Sat Jul 19 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 2.49-0.fdr.2
- Make package own {_datadir}/cvs2cl.

* Fri Jul 18 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> 2.49-0.fdr.1
- Updated to 2.49.

* Wed Apr 23 2003 Marius Jøhndal <mariuslj at ifi.uio.no> 2.48-0.fdr.1
- Updated to 2.48.
- Requires: perl -> BuildRequires: perl.

* Wed Mar 26 2003 Marius Jøhndal <mariuslj at ifi.uio.no> 2.47-0.fdr.1
- Updated to 2.47.

* Thu Mar  6 2003 Marius Jøhndal <mariuslj at ifi.uio.no> 2.46-0.fdr.1
- Initial Fedora RPM release.

* Tue Feb 18 2003 Marius Jøhndal <mariuslj at ifi.uio.no>
- Updated to 2.46.

* Sat Nov  9 2002 Marius Jøhndal <mariuslj at ifi.uio.no>
- Initial version based on revision 2.40 from CVS.

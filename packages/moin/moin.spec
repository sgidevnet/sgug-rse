Summary: MoinMoin is a WikiEngine to collaborate on easily editable web pages
Name: moin
Version: 1.9.10
Release: 3%{?dist}
License: GPLv2+
URL: http://moinmo.in/
Source0: http://static.moinmo.in/files/moin-%{version}.tar.gz
Source1: README-rpm

%if 0%{?rhel}
BuildRequires: python-devel python-setuptools
%else
BuildRequires: python2-devel python2-setuptools
%endif

BuildArch: noarch

%description
MoinMoin is an advanced, easy to use and extensible WikiEngine with a large
community of users. Said in a few words, it is about collaboration on easily
editable web pages.


%prep
%setup -q
# Change the encoding to UTF-8, users are likely to edit this file
sed -i -e 's|coding: iso-8859-1|coding: utf-8|' wiki/config/wikiconfig.py
# Remove the leading comment from url_prefix_static. The Moin default assumes
# the wiki is served from the root of the site, change it to better suit the
# example in README-rpm, in which the wiki is served from
# example.tld/mywiki
sed -i -e 's|\(#\)\(url_prefix_static.*\)|\2|' wiki/config/wikiconfig.py
# Add the directory containing moin.wsgi to the Python search path, as
# in the README-rpm example these files will be in the same directory.
sed -i -e "s|#sys.path.insert(0, '/path/to/wikiconfigdir')|sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))|" wiki/server/moin.wsgi


%build
%py2_build


%install
%py2_install
%{__install} -p -m 0644 %{SOURCE1} README-rpm

#TODO: Recheck w/ moin 2.x (py3-based)
sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}/%{_datadir}/moin/server/*
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}/%{_datadir}/moin/server/*

%files
%doc README* docs/CHANGES* docs/INSTALL.html docs/README_FIRST docs/README.migration docs/UPDATE.html
%doc docs/licenses/
%{_bindir}/moin
%{python2_sitelib}/moin-*.egg-info
%{python2_sitelib}/MoinMoin/
%{python2_sitelib}/jabberbot/
%{_datadir}/moin/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.9.10-1
- Update to 1.9.10 (rhbz #1641242)
- Remove the backported patch
- Minor spec fix: README path and py2/env shebang

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.9.9-1
- Update to 1.9.9 (bugfix release for CVE-2016-7146, CVE-2016-7148)
- Add patch to fix wrong digestmod

* Sat Sep 17 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.9.8-2
- Fix EPEL build

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.9.8-1
- Update to 1.9.8 (RHBZ #1338003)
- Use versioned python macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.9.7-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Kevin Fenzi <kevin@scrye.com> 1.9.6-1
- Update to 1.9.6. Fixes CVE-2012-6495
- Fix changelog dates. 

* Mon Oct 08 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> 1.9.5-1
- New upstream release
- Drop integrated security patch

* Thu Sep 06 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.9.4-3
- Fix CVE-2012-4404

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.9.4-1
- New upstream release
- Drop integrated security patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 18 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.9.3-5
- Remove check for packaging egg-info if Fedora >= 9, breaks EL builds (rhbz#739311)

* Thu Feb 24 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.3-4
- Fixes CVE-2011-1058 (rhbz#679523)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 28 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.9.3-1
- Fixes multiple XSS vulnerabilities (rhbz#601399)
- http://hg.moinmo.in/moin/1.9/raw-file/1.9.3/docs/CHANGES
- Drop integrated security patch

* Sat Apr 03 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.2-2
- Fixes CVE-2010-0828 (rhbz#578801)

* Mon Mar 01 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.2-1
- Fixes CVE-2010-0668 and CVE-2010-0669 (rhbz#565604)
- http://hg.moinmo.in/moin/1.9/raw-file/1.9.2/docs/CHANGES

* Thu Jan 21 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.1-1
- 1.9.1
- Fixes rhbz#557298 -  moin information disclosure vulnerability

* Sat Dec 26 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.9.0-1
- 1.9.0
- Don't remove any FCKeditor directories, all known security issues in it
  should be fixed by now
- Updated README-rpm, only give an example on mod_wsgi configuration, Moin is
  a pure WSGI application now
- Change the Python magic encoding comment in wiki/config/wikiconfig.py to
  UTF-8
- Change url_prefix_static in wiki/config/wikiconfig.py to better suit the
  configuration example in README-rpm, where the wiki is served from 
  example.tld/mywiki
- wiki/server/moin.wsgi adds the directory it is in to the Python search path,
  as the wikiconfig.py file will be in the same directory as moin.wsgi if Moin
  is set up according to the example in README-rpm

* Tue Sep 15 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.8.5-1
- 1.8.5
- Includes multiple bug fixes, a new FCKeditor version and some new features
- http://hg.moinmo.in/moin/1.8/raw-file/1.8.5/docs/CHANGES

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.8.4-2
- Remove the filemanager directory from the embedded FCKeditor, it contains
  code with know security vulnerabilities, even though that code couldn't
  be invoked when moin was used with the default settings.
- Fixes rhbz #509924, related to CVE-2009-2265

* Sat Jun 13 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.8.4-1
- Update to 1.8.4, http://moinmo.in/MoinMoinRelease1.8 has a list of
  changes.
- Includes a security fix for hierarchical ACL (not the default mode),
  http://moinmo.in/SecurityFixes has the details.
- Drop previous security patches, those are not needed anymore.

* Wed Apr 22 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.8.2-2
- Fix CVE-2008-0781 (also known as CVE-2009-1482) with two patches from
  upstream

* Tue Apr 14 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.8.2-1
- Update to 1.8.2
- Update README-rpm to include mod_wsgi instructions
- Fixes CVE-2008-3381

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.3-2
- Rebuild for Python 2.6

* Thu Apr 24 2008 Matthias Saou <http://freshrpms.net/> 1.6.3-1
- Update to 1.6.3.

* Tue Mar 25 2008 Matthias Saou <http://freshrpms.net/> 1.6.2-1
- Update to 1.6.2.

* Mon Feb  4 2008 Matthias Saou <http://freshrpms.net/> 1.6.1-1
- Update to 1.6.1.

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 1.6.0-2
- Apparently, egg-info files are only installed on F-9+.

* Thu Jan 17 2008 Matthias Saou <http://freshrpms.net/> 1.6.0-1
- Update to 1.6.0.
- Update URL, source location, summary and description.
- Remove now included xml_newline patch.
- Remove no longer current config patch. It shouldn't be missed.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.5.8-2
- Update License field.

* Wed May 16 2007 Matthias Saou <http://freshrpms.net/> 1.5.8-1
- Update to 1.5.8, which includes most previous security fixes.
- Remove the (apparently) no longer needed dos2unix conversion for patch.
- Use %%{python_sitelib} macro.

* Mon May  7 2007 Matthias Saou <http://freshrpms.net/> 1.5.7-2
- Include security fixes from the Debian package (Jonas Smedegaard).
- FIX_use_ACL_in_include_directive (Alexander Schremmer).
- fix_MonthCalendar_respect_ACLs (Thomas Waldmann).
- FIX_XSS_in_AttachFile_do_parameter (Thomas Waldmann).
- CVE-2007-0857.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.5.7-1
- Update to 1.5.7.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 1.5.6-2
- Rebuild against python 2.5.
- Change python build requirement to python-devel, as it's needed now.

* Tue Oct 31 2006 Matthias Saou <http://freshrpms.net/> 1.5.6-1
- Update to 1.5.6.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 1.5.5-1
- Update to 1.5.5.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.5.4-3
- FC6 rebuild.

* Tue Aug  1 2006 Matthias Saou <http://freshrpms.net/> 1.5.4-2
- Don't assume we have a sane default umask... (#200833).

* Fri Jun  2 2006 Matthias Saou <http://freshrpms.net/> 1.5.4-1
- Update to 1.5.4.

* Tue Apr 18 2006 Matthias Saou <http://freshrpms.net/> 1.5.3-1
- Update to 1.5.3.

* Mon Feb  6 2006 Matthias Saou <http://freshrpms.net/> 1.5.2-1
- Update to 1.5.2.
- Update config patch.
- Update %%doc files.

* Sun Dec 18 2005 Tommy Reynolds <Tommy.Reynolds@MegaCoder.com> 1.3.5-3
- Remove extraneous '\' from XML output, so that <screen>..</screen>
  does not generate '\' 'n' outside of any markup.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.5-2
- Fix python modules path from _libdir to _prefix/lib so that build works on
  64bit systems too.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.5-1
- Update to 1.3.5.
- Update the config patch.
- Update %%doc section (many moved to docs/).

* Wed Jun 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.4-1
- Update to 1.3.4.
- Update the config patch.
- Move the README.redhat file out from the patch and rename it to README-rpm.

* Tue Apr 19 2005 Matthias Saou <http://freshrpms.net/> 1.3.3-2
- Adapted for inclusion into Extras.
- Merge relevant bits from Jeff's pyvault version.

* Wed Dec 22 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3.1

* Thu Dec 09 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3.0

* Sun Nov 07 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3beta4

* Fri Aug 06 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.2.3

* Wed May 19 2004 - Kai.Puolamaki@iki.fi
- Fix also directory permissions...

* Mon May 17 2004 - Kai.Puolamaki@iki.fi
- Fix file permissions

* Fri May 14 2004 - Kai.Puolamaki@iki.fi
- 1.2.1
- Home build


%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:           python-bugzilla
Version:        2.3.0
Release:        1%{?dist}
Summary:        Python library for interacting with Bugzilla

License:        GPLv2+
URL:            https://github.com/python-bugzilla/python-bugzilla
Source0:        https://github.com/python-bugzilla/python-bugzilla/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-requests
BuildRequires: python2-setuptools
BuildRequires: python2-pytest
%endif # with python2

%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-requests
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
%endif # if with_python3

%global _description\
python-bugzilla is a python library for interacting with bugzilla instances\
over XML-RPC.\

%description %_description


%if %{with python2}
%package -n python2-bugzilla
Summary: %summary
Requires: python2-requests
# This dep is for back compat, so that installing python-bugzilla continues
# to give the cli tool
Requires: python-bugzilla-cli
%{?python_provide:%python_provide python2-bugzilla}

%description -n python2-bugzilla %_description

%endif # with python2


%if %{with python3}
%package -n python3-bugzilla
Summary: %summary
Requires: python3-requests
%{?python_provide:%python_provide python3-bugzilla}

%if %{without python2}
Obsoletes:      python-bugzilla < %{version}-%{release}
Obsoletes:      python2-bugzilla < %{version}-%{release}
%endif # without python2

%description -n python3-bugzilla %_description
%endif # if with_python3


%package cli
Summary: Command line tool for interacting with Bugzilla
%if %{with python3}
Requires: python3-bugzilla = %{version}-%{release}
%else
Requires: python2-bugzilla = %{version}-%{release}
%endif

%description cli
This package includes the 'bugzilla' command-line tool for interacting with bugzilla. Uses the python-bugzilla API



%prep
%setup -q

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3



%build
%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%if %{with python2}
%{__python2} setup.py build
%endif # with python2



%install
%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%if %{with python2}
rm %{buildroot}/usr/bin/bugzilla
%endif

popd
%endif # with_python3

%if %{with python2}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%endif # with python2

# Replace '#!/usr/bin/env python' with '#!/usr/bin/python2'
# The format is ideal for upstream, but not a distro. See:
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
%if %{with python3}
%global python_env_path %{__python3}
%else
%global python_env_path %{__python2}
%endif
for f in $(find %{buildroot} -type f -executable -print); do
    sed -i "1 s|^#!/usr/bin/.*|#!%{python_env_path}|" $f || :
done



%check
%if %{with python2}
# py.test naming is needed for RHEL7 compat, works fine with Fedora
py.test
%endif # with python2
%if %{with python3}
pytest-3
%endif # with python3



%if %{with python2}
%files -n python2-bugzilla
%doc COPYING README.md NEWS.md
%{python2_sitelib}/*
%endif # with python2

%if %{with python3}
%files -n python3-bugzilla
%doc COPYING README.md NEWS.md
%{python3_sitelib}/*
%endif # with_python3

%files cli
%{_bindir}/bugzilla
%{_mandir}/man1/bugzilla.1.gz


%changelog
* Mon Aug 26 2019 Cole Robinson <crobinso@redhat.com> - 2.3.0-1
- Update to version 2.3.0
- restrict-login suppot (Viliam Krizan)
- cli: Add support for private attachments (Brian 'Redbeard' Harrington)
- Fix python3 deprecation warnings
- Drop python 3.3 support, minimum python3 is python 3.4 now

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Cole Robinson <crobinso@redhat.com> - 2.2.0-3
- Fix SafeConfigParser warnings

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Cole Robinson <crobinso@redhat.com> - 2.2.0-1
- Rebased to version 2.2.0
- Port tests to pytest
- cli: --cert Client side certificate support (Tobias Wolter)
- cli: add ability to post comment while sending attachment (Jeff Mahoney)
- cli: Add --comment-tag option
- cli: Add info --active-components
- Add a raw Product.get wrapper API
- Don't traceback on missing cli command (bz #1513819)
- Fix bug.get with sub_components (bz #1503491)
- Fix uploading binary attachments (bz #1496821)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Tomas Orsava <torsava@redhat.com> - 2.1.0-6
- Conditionalize the Python 2 subpackage

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-3
- Python 2 binary package renamed to python2-bugzilla
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Cole Robinson <crobinso@redhat.com> - 2.1.0-1
- Rebased to version 2.1.0
- Support for bugzilla 5 API Keys (Dustin J. Mitchell)
- bugzillarc can be used to set default URL for the cli tool
- Revive update_flags wrapper
- Bug fixes and minor improvements

* Wed Feb 08 2017 Cole Robinson <crobinso@redhat.com> - 2.0.0-1
- Rebased to version 2.0.0
- Several fixes for use with bugzilla 5
- This release contains several smallish API breaks:
- Bugzilla.bug_autorefresh now defaults to False
- Credentials are now cached in ~/.cache/python-bugzilla/
- bin/bugzilla was converted to argparse
- bugzilla query --boolean_chart option is removed
- Unify command line flags across sub commands

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.2.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Robert Kuska <rkuska@redhat.com> - 1.2.2-2
- Rebuilt for Python3.5 rebuild

* Tue Sep 22 2015 Cole Robinson <crobinso@redhat.com> - 1.2.2-1
- Rebased to version 1.2.2
- Fix requests usage when ndg-httpsclient is installed (bz #1247158)
- Fix errors with non-ascii usernames (bz #1264848)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Cole Robinson <crobinso@redhat.com> - 1.2.1-1
- Rebased to version 1.2.1
- bin/bugzilla: Add --ensure-logged-in option
- Fix get_products with bugzilla.redhat.com
- A few other minor improvements

* Wed Apr 08 2015 Cole Robinson <crobinso@redhat.com> - 1.2.0-1
- Rebased to version 1.2.0
- Add bugzilla new/query/modify --field flag (Arun Babu Neelicattu)
- API support for ExternalBugs (Arun Babu Neelicattu, Brian Bouterse)
- Add new/modify --alias support (Adam Williamson)
- Bugzilla.logged_in now returns live state (Arun Babu Neelicattu)
- Fix getbugs API with latest Bugzilla releases

* Wed Jun 18 2014 Cole Robinson <crobinso@redhat.com> - 1.1.0-2
- Fix tests on rawhide (bz #1106734)

* Sun Jun 01 2014 Cole Robinson <crobinso@redhat.com> - 1.1.0-1
- Rebased to version 1.1.0
- Support for bugzilla tokens (Arun Babu Nelicattu)
- bugzilla: Add query/modify --tags
- bugzilla --login: Allow to login and run a command in one shot
- bugzilla --no-cache-credentials: Don't use or save cached credentials
  when using the CLI
- Show bugzilla errors when login fails
- Don't pull down attachments in bug.refresh(), need to get
  bug.attachments manually
- Add Bugzilla bug_autorefresh parameter.

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 27 2014 Cole Robinson <crobinso@redhat.com> - 1.0.0-2
- /usr/bin/bugzilla should use python2 (bz #1081594)

* Tue Mar 25 2014 Cole Robinson <crobinso@redhat.com> - 1.0.0-1
- Rebased to version 1.0.0
- Python 3 support (Arun Babu Neelicattu)
- Port to python-requests (Arun Babu Neelicattu)
- bugzilla: new: Add --keywords, --assigned_to, --qa_contact (Lon
  Hohberger)
- bugzilla: query: Add --quicksearch, --savedsearch
- bugzilla: query: Support saved searches with --from-url
- bugzilla: --sub-component support for all relevant commands

* Tue Nov 05 2013 Cole Robinson <crobinso@redhat.com> - 0.9.0-3
- Drop unneeded setuptools dep

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Cole Robinson <crobinso@redhat.com> - 0.9.0-1
- Rebased to version 0.9.0
- bugzilla: modify: add --dependson (Don Zickus)
- bugzilla: new: add --groups option (Paul Frields)
- bugzilla: modify: Allow setting nearly every bug parameter
- NovellBugzilla implementation removed, can't get it to work
- Gracefully handle private bugs (bz #963979)
- Raise error if python-magic is needed (bz #951572)
- CVE-2013-2191: Add SSL host and cert validation (bz #975961, bz #951594)

* Mon Mar 04 2013 Cole Robinson <crobinso@redhat.com> - 0.8.0-2
- Don't upload scrambled attachments (bz #915318)

* Fri Feb 15 2013 Cole Robinson <crobinso@redhat.com> - 0.8.0-1
- Rebased to version 0.8.0
- Drop most usage of non-upstream RH Bugzilla API
- Test suite improvements, nearly complete code coverage
- Fix all open bug reports and RFEs

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Adam Jackson <ajax@redhat.com> 0.7.0-3
- Make closing bugs work, and allow closing as duplicate.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Cole Robinson <crobinso@redhat.com> - 0.7.0-1
- Rebased to version 0.7.0
- Fix querying with latest Red Hat bugzilla
- Bugzilla 4 API support
- Improve querying non-RH bugzilla instances

* Tue Apr  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.2-4
- Cleanup spec and actually rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 09 2011 Will Woods <wwoods@redhat.com> - 0.6.2-2
- Add "Requires: python-magic"

* Tue Jun 07 2011 Will Woods <wwoods@redhat.com> - 0.6.2-1
- add 'bugzilla attach' command (#707320)
- update CLI --help, improve manpage a bit
- fix --blocked and other boolean CLI options (#621601)
- use NamedTemporaryFile for temp. cookiefiles (#625019)
- fix openattachment() on non-ascii filenames (#663674 - thanks kklic)
- clean up handling of unknown product names (#659331)
- misc CLI fixes (--oneline, --qa_whiteboard), add 'modify --qa_contact'

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.1-3
- add compatibility patch for python 2.7 (bug 621298)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Apr 16 2010 Will Woods <wwoods@redhat.com> - 0.6.1-1
- CLI speedup: skip version autodetection for bugzilla.redhat.com
- CLI: fix bug 581670 - UnicodeEncodeError crash using --outputformat
- CLI: fix bug 549186 - parser failure/xmlrpc Fault on 'bugzilla query'
- Library: fix bug 577327 - crash changing assignee without --comment
- Library: fix bug 580711 - crash when bug has empty CC list
- Library: add new Bugzilla36 class
- Library: export and autodetect Bugzilla34 and Bugzilla36 classes

* Tue Mar 2 2010 Will Woods <wwoods@redhat.com> - 0.6.0-1
- New version 0.6, with lots of improvements and fixes.
- Library: add NovellBugzilla implementation
- Library: use standardized LWPCookieJar by default
- Library: implement unicode(bug), fix Bug.__str__ unicode handling
- Library: make Bug class pickle-friendly
- Library: add flag info helper methods to Bug class
- Library: handle problems with missing fields in User class
- CLI: --oneline formatting tweaks and dramatic speed improvements
- CLI: add support for modifying private, status, assignee, flags, cc, fixed_in
- CLI: improve query: allow multiple flags, flag negation, handle booleans
- CLI: make --cc work when creating bugs
- CLI: new --raw output style
- CLI: special output format fields for flag and whiteboard
- CLI: fix broken --cc and -p flags
- CLI: fix problem where bz comments default to being private
- CLI: improve 'info --product' output
- CLI: handle socket/network failure cleanly
- CLI: allow adding comments when updating whiteboards

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Will Woods <wwoods@redhat.com> - 0.5.1-2
- Fix missing util.py

* Thu Apr 9 2009 Will Woods <wwoods@redhat.com> - 0.5.1-1
- CLI: fix unicode handling
- CLI: add --from-url flag, which parses a bugzilla query.cgi URL
- CLI: fix showing aliases
- CLI: add --comment, --private, --status, --assignee, --flag, --cc for update
- CLI: fix --target_milestone

* Wed Mar 25 2009 Will Woods <wwoods@redhat.com> - 0.5-1
- Fix problem where login wasn't saving the cookies to a file 
- Fix openattachment (bug #487673)
- Update version number for 0.5 final

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Will Woods <wwoods@redhat.com> 0.5-0.rc1
- Improve cookie handling
- Add User class and associated Bugzilla methods (in Bugzilla 3.4)
- Add {add,edit,get}component methods
- Fix getbugs() so a single invalid bug ID won't abort the whole request
- CLI: fix -c <component>

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4-0.rc4.1
- Rebuild for Python 2.6

* Wed Oct 15 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc4
- CLI: fix traceback with --full (Don Zickus)
- CLI: add --oneline (Don Zickus)
- CLI: speedup when querying bugs by ID (Don Zickus)
- CLI: add --bztype
- CLI: --bug_status defaults to ALL
- Fix addcc()/deletecc()
- RHBugzilla3: raise useful error on getbug(unreadable_bug_id)
- Add adduser() (Jon Stanley)

* Wed Oct  8 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc3
- Add updateperms() - patch courtesy of Jon Stanley
- Fix attachfile() for RHBugzilla3
- Actually install man page. Whoops.

* Thu Sep 18 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc2
- Auto-generated man page with much more info
- Fix _attachfile()

* Thu Sep  4 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc1
- Update to python-bugzilla 0.4-rc1
- We now support upstream Bugzilla 3.x and Red Hat's Bugzilla 3.x instance
- library saves login cookie in ~/.bugzillacookies
- new 'bugzilla login' command to get a login cookie

* Sat Jan 12 2008 Will Woods <wwoods@redhat.com> 0.3-1
- Update to python-bugzilla 0.3 
- 'modify' works in the commandline-util
- add Bug.close() and Bug.setstatus()

* Thu Dec 13 2007 Will Woods <wwoods@redhat.com> 0.2-4
- use _bindir instead of /usr/bin and proper BR for setuptools

* Tue Dec 11 2007 Will Woods <wwoods@redhat.com> 0.2-3
- Fix a couple of things rpmlint complained about

* Tue Dec 11 2007 Will Woods <wwoods@redhat.com> 0.2-2
- Add docs

* Wed Oct 10 2007 Will Woods <wwoods@redhat.com> 0.2-1
- Initial packaging.

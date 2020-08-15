%global srcname docutils

Name:           python-%{srcname}
Version:        0.15.2
Release:        1%{?dist}
Summary:        System for processing plaintext documentation

# See COPYING.txt for information
License:        Public Domain and BSD and Python and GPLv3+
URL:            http://docutils.sourceforge.net
#Source0:        http://downloads.sourceforge.net/docutils/%%{srcname}-%%{version}.tar.gz
# Sometimes we need snapshots.  Instructions below:
# svn co -r 7687 svn://svn.code.sf.net/p/docutils/code/trunk/docutils
# cd docutils
# python setup.py sdist
# The tarball is in dist/docutils-VERSION.tar.gz
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:       noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
The Docutils project specifies a plaintext markup language, reStructuredText,
which is easy to read and quick to write.  The project includes a python
library to parse rST files and transform them into other useful formats such
as HTML, XML, and TeX as well as commandline tools that give the enduser
access to this functionality.

Currently, the library supports parsing rST that is in standalone files and
PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
Python inline documentation modules and packages.

%package -n python2-%{srcname}
Summary:        System for processing plaintext documentation for python2
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
The Docutils project specifies a plaintext markup language, reStructuredText,
which is easy to read and quick to write.  The project includes a python
library to parse rST files and transform them into other useful formats such
as HTML, XML, and TeX as well as commandline tools that give the enduser
access to this functionality.

Currently, the library supports parsing rST that is in standalone files and
PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
Python inline documentation modules and packages.

%package -n python3-%{srcname}
Summary:        System for processing plaintext documentation for python3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The Docutils project specifies a plaintext markup language, reStructuredText,
which is easy to read and quick to write.  The project includes a python
library to parse rST files and transform them into other useful formats such
as HTML, XML, and TeX as well as commandline tools that give the enduser
access to this functionality.

Currently, the library supports parsing rST that is in standalone files and
PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
Python inline documentation modules and packages.

This package contains the module, ported to run under python3.


%prep
%autosetup -c -n %{srcname}-%{version}

# Upstream needs separate python2 and 3 folders as it utilizes 2to3 in
# a custom hackish way
export PREV_WD=`pwd`
cd %{srcname}-%{version}

# Remove shebang from library files
for file in docutils/utils/{code_analyzer.py,punctuation_chars.py,error_reporting.py,smartquotes.py} docutils/utils/math/{latex2mathml.py,math2html.py} docutils/writers/xetex/__init__.py; do
sed -i -e '/#! *\/usr\/bin\/.*/{1D}' $file
done

iconv -f ISO-8859-2 -t UTF-8 tools/editors/emacs/IDEAS.rst > tmp
mv tmp tools/editors/emacs/IDEAS.rst

cd $PREV_WD

# Create the two folders mentioned above
mv %{srcname}-%{version} python3
cp -rp python3 python2

# Get the doc and license files out
cd python3
cp -rp COPYING.txt licenses BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt  THANKS.txt tools/editors ..
cd $PREV_WD

# We want the licenses but don't need this build file
rm -f licenses/docutils.conf

%if 0%{?python3_version_nodots} >= 38
# https://bugzilla.redhat.com/show_bug.cgi?id=1687377
rm python3/test/test_writers/test_odt.py
%endif

%build
export PREV_WD=`pwd`
cd python2
%py2_build
cd $PREV_WD

cd python3
%py3_build
cd $PREV_WD


%install
export PREV_WD=`pwd`
cd python2
%py2_install

# Flash file is used for testing docutils but shouldn't be in the installed package.
mv docs/user/rst/images/biohazard.swf ./biohazard.swf
cd $PREV_WD

rm -f %{buildroot}/%{_bindir}/*

cd python3
%py3_install
mv docs/user/rst/images/biohazard.swf ./biohazard.swf
cd $PREV_WD

# docutils setup.py runs 2to3 on a copy of the tests and puts it in sitelib.
rm -rf %{buildroot}%{python3_sitelib}/test


for file in %{buildroot}/%{_bindir}/*.py; do
  mv $file `dirname $file`/`basename $file .py`
done


%check
export PREV_WD=`pwd`
for PY in 2 3; do
  cd python${PY}
  mv  biohazard.swf docs/user/rst/images/biohazard.swf
  python${PY} test${PY/2/}/alltests.py
  rm docs/user/rst/images/biohazard.swf
  cd $PREV_WD
done


%files -n python2-%{srcname}
%license COPYING.txt licenses/*
%doc BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt 
%doc THANKS.txt python2/docs editors
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info


%files -n python3-%{srcname}
%license COPYING.txt licenses/*
%doc BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt
%doc THANKS.txt python3/docs editors
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/*


%changelog
* Fri Aug 02 2019 Kevin Fenzi <kevin@scrye.com> - 0.15.2-1
- Update to 0.15.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14-5
- Only ship one version of the rst2* executables
- Invoke python2 with python2 in %%check

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Oct 22 2017 Kevin Fenzi <kevin@scrye.com> - 0.14-1
- Update to 0.14

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.13.1-7
- Cleanup spec file conditionals

* Sun Jul 30 2017 Jan Beran <jberan@redhat.com> - 0.13.1-6
- Fix missing Python 3 version executables

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Orion Poplawski <orion@cora.nwra.com> - 0.13.1-3
- Fix broken python-docutils provides (bug #1399655)
- Use %%license, python build macro
- Spec cleanup

* Sun Jan 29 2017 Kevin Fenzi <kevin@scrye.com> - 0.13.1-2
- Rework packaging to make a python2 package and fix provides

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 0.13.1-1
- Update to 0.13.1. Fixes bug #1403399
- Provide python2 version. Fixes bug #1399655

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.12-0.8.20140510svn7747
- Rebuild for Python 3.6
- Fix failing tests
- Remove runtime requirement for python-imaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-0.7.20140510svn7747
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-0.6.20140510svn7747
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 0.12-0.5.20140510svn7747
- Rebuilt for Python3.5 rebuild

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 0.12-0.3.20140510svn7747
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-0.3.20140510svn7747
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-0.2.20140510svn7747
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.12-0.1.20140510svn7747
- Update to svn snapshot for Python 3.4 support
- Drop unneeded patch

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-2
- Rebuild for Python 3.4

* Thu Aug 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.11-1
- 0.11 final tarball.
- Remove flash file from the install (it was only used to run the unittests anyhow)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.2.20130715svn7687
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Matej Stuchlik <mstuchli@redhat.com> - 0.11-0.1.20130715svn7687
- Rebased to new snapshot
- Removed unnecessary patches

* Thu Mar 21 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-0.8.20120824svn7502
- Add python3-imaging support :-)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.7.20120824svn7502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-0.6.20120824svn7502
- Further fix of places in the code that use__import__

* Fri Aug 24 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-0.5.20120824svn7502
- Rebase to new snapshot with some fixes integrated
- Reenable one test that I can't replicate the failure with.

* Fri Aug 24 2012 David Malcolm <dmalcolm@redhat.com> - 0.10-0.4.20120730svn7490
- fix/disable failing tests with python 3.3

* Tue Aug 14 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-0.3.20120730svn7490
- PyXML patch from upstream
- Fix ability to disable python3 builds

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.10-0.2.20120730svn7490
- remove rhel logic from with_python3 conditional

* Mon Jul 30 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-0.1.20120730svn7490
- Update to snapshot that's supposed to take care of the date directive unicode
  problem in a different way
- Patch to fix PyXML conflict without using rpm conflicts

* Fri Jul 20 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.1-1
- New update from upstream
- Fixes for previous patches incorporated there
- roman.py has been moved into a docutils submodule
- docutils doesn't work with PyXML.  before I poke around for the bug in PyXML,
  seeing if we're going to go through with deprecating it or if we can sanitize
  our python stdlib's handling of it.
- Fix for traceback in https://bugzilla.redhat.com/show_bug.cgi?id=786867

* Mon Jan 30 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-2
- Fix a unicode traceback https://bugzilla.redhat.com/show_bug.cgi?id=785622

* Thu Jan 5 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-1
- Update to new upstream that has properly licensed files and a few bugfixes
- Add a patch to fix tracebacks when wrong values are given to CLI apps

* Wed Jul 20 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8-2
- Replace the Apache licensed files with BSD licensed versions from upstream

* Tue Jul 12 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8-1
- Upgrade to 0.8 final.
- Remove the two remaining Apache licensed files until their license is fixed.
- Patch regressions that we had already submitted upstream -- resubmit

* Tue May 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8-0.1.20110517svn7036
- Ship a snapshot of 0.8 so that we can build on python-3.2.1
- Unfortunately, 3.2.1 isn't out yet either.  So also apply a fix for building
  with 3.2.0 that we'll need to remove later.
- The new docutils.math module is licensed Apache.  Update the license to reflect this

* Wed Mar 16 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7-5
- Fix building with python-3.2 via a workaround.  Sent upstream awaiting
  feedback or a better fix.  Built in rawhide.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 1 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7-3
- Fix scripts so they're the python2 versions not the python3 versions

* Thu Dec 30 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7-2
- Build for python3

* Sun Aug 1 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7-1
- Update for 0.7 release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jan 19 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-1
- Update for 0.6 release.
- Switch from setuptools installed egg-info to distutils egg-info.  Note that
  this works because we're also changing docutils version.  To do this between
  0.5-4 and 0.5-5, for instance, we'd need to have %%preun scriptlet to get rid
  of the egg-info directory.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-2
- Rebuild for Python 2.6

* Wed Aug 6 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.5-1
- New upstream version.

* Mon Mar 3 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.4-8
- Use regular Requires syntax for python-imaging as missingok is just wrong.

* Thu Sep 27 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4-7
- Build egg info.

* Mon Aug 13 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4-6
- Last version had both the old and new rst.el.  Try again with only
  the new one.

* Sun Aug 12 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4-5
- Make License tag conform to the new Licensing Policy.
- Fix the rst emacs mode (RH BZ 250100)

* Sat Dec 09 2006 Toshio Kuratomi <toshio-tiki-lounge.com> 0.4-4
- Bump and rebuild for python 2.5 in devel.

* Tue Aug 29 2006 Toshio Kuratomi <toshio-tiki-lounge.com> 0.4-3
- Bump for FC6 rebuild.
- Remove python byte compilation as this is handled automatically in FC4+.
- No longer %%ghost .pyo files.
  
* Thu Feb 16 2006 Toshio Kuratomi <toshio-tiki-lounge.com> 0.4-2
- Bump and rebuild for FC5.
  
* Sun Jan 15 2006 Toshio Kuratomi <toshio-tiki-lounge.com> 0.4-1
- Update to 0.4.
- Scripted the listing of files in the python module.
- Add a missingok requirement on python-imaging as docutils can make use of
  it when converting to formats that have images.
  
* Tue Jun 7 2005 Toshio Kuratomi <toshio-tiki-lounge.com> 0.3.9-1
- Update to version 0.3.9.
- Use a dist tag as there aren't any differences between supported fc
  releases (FC3, FC4, devel.)

* Thu May 12 2005 Toshio Kuratomi <toshio-tiki-lounge.com> 0.3.7-7
- Bump version and rebuild to sync across architectures.

* Sun Mar 20 2005 Toshio Kuratomi <toshio-tiki-lounge.com> 0.3.7-6
- Rebuild for FC4t1

* Sat Mar 12 2005 Toshio Kuratomi <toshio.tiki-lounge.com> 0.3.7-5
- Add GPL as a license (mschwendt)
- Use versioned Obsoletes and Provides (mschwendt)

* Fri Mar 04 2005 Toshio Kuratomi <toshio.tiki-lounge.com> 0:0.3.7-4
- Rename to python-docutils per the new packaging guidelines.

* Wed Jan 12 2005 Toshio Kuratomi <toshio.tiki-lounge.com> 0:0.3.7-0.fdr.3
- Really install roman.py and build roman.py[co].  Needed to make sure I have
  docutils installed to test that it builds roman.py fine in that case.

* Tue Jan 11 2005 Toshio Kuratomi <toshio.tiki-lounge.com> 0:0.3.7-0.fdr.2
- Special case roman.py to always install.  This is the behaviour we want
  unless something else provides it.  Will need to watch out for this in
  future Core and Extras packages, but the auto detection code makes it
  possible that builds will not be reproducible if roman.py were installed
  from another package.... Lesser of two evils here.
- Provide python-docutils in case that package were preinstalled from
  another repository.
  
* Fri Dec 31 2004 Toshio Kuratomi <toshio.tiki-lounge.com> 0:0.3.7-0.fdr.1
- Update to 0.3.7
- Rename from python-docutils to docutils.
- Make roman.py optionally a part of the files list.  In FC2, this will be
  included.  In FC3, this won't.
- BuildConflict with self since the docutils build detects the presence
  of roman.py and doesn't reinstall itself.
  
* Mon Aug 9 2004 Toshio Kuratomi <toshio.tiki-lounge.com> 0:0.3.5-0.fdr.1
- Update to 0.3.5.
- Update spec style to latest fedora-rpmdevtools.
- Merge everything into a single package.  There isn't very much space
  advantage to having separate packages in a package this small and in
  this case, the documentation on using docutils as a library is also a
  good example of how to write in ReSructuredText.

* Sat Jan 10 2004 Michel Alexandre Salim <salimma[AT]users.sf.net> 0:0.3-0.fdr.1
- Initial RPM release.


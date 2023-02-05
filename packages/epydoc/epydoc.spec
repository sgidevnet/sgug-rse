Summary: Automatic API documentation generation tool for Python
Name: epydoc
Version: 3.0.1.20090203svn
Release: 12%{?dist}
License: MIT
URL: http://epydoc.sourceforge.net/
Source0: http://dl.sf.net/epydoc/epydoc-%{version}.tar.gz
Source1: epydocgui.desktop
Patch0: epydoc-3.0.1-nohashbang.patch
Patch1: epydoc-3.0.1svn1812-png-default.patch
Patch2: epydoc-3.0.1-new-docutils.patch
Patch3: epydoc-3.0.1svn1812-make-suppress-timestamp-the-default.patch
Patch4: epydoc-3.0.1svn1812-fix-relative-import.patch
# Needed for some outputs, like --pdf (#522249)
Recommends: tex(dvips)
Recommends: tex(latex)
BuildRequires: python2-devel
%if ! 0%{?_module_build}
BuildRequires: desktop-file-utils
%endif
BuildArch: noarch

%description
Epydoc  is a tool for generating API documentation for Python modules,
based  on their docstrings. For an example of epydoc's output, see the
API  documentation for epydoc itself (html, pdf). A lightweight markup
language  called  epytext can be used to format docstrings, and to add
information  about  specific  fields,  such as parameters and instance
variables.    Epydoc    also   understands   docstrings   written   in
ReStructuredText, Javadoc, and plaintext.

%package doc
Summary: Documentation for epydoc
Requires: %{name} = %{version}-%{release}
%description doc
epydoc-doc package contains documentation.

%package gui
Summary: Graphical user interfacefor epydoc
Requires: %{name} = %{version}-%{release}
Requires: python2-tkinter
%description gui
epydoc-gui package contains Graphical user interface for epydoc



%prep
%setup -q
# Clean scm files
rm -rf epydoc/doc/.cvsignore
%patch0 -p1 -d epydoc/src/ -b .nohashbang
%patch1 -p1 -b .default-png
%patch2 -p1 -d epydoc/src/ -b .new-docutils
%patch3 -p1 -b .no-timestamp
%patch4 -p0 -d epydoc/src/ -b .fix-relative-import


%build
cd epydoc/src/
%py2_build


%install
cd epydoc/src/
%py2_install

%if ! 0%{?_module_build}
desktop-file-install \
    --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications \
    --mode=0644 \
    %{SOURCE1}
%endif

# Prevent having *.pyc and *.pyo in _bindir
mv %{buildroot}%{_bindir}/apirst2html.py %{buildroot}%{_bindir}/apirst2html

# Also install the man pages
install -Dt %{buildroot}%{_mandir}/man1/ -p -m 0644 ../man/*.1

%files
%doc epydoc/src/README.txt
%license epydoc/src/LICENSE.txt
%{_bindir}/apirst2html
%{_bindir}/epydoc
%{python2_sitelib}/epydoc/
%{python2_sitelib}/epydoc-*.egg-info
%{_mandir}/man1/epydoc.1*

%files doc
%doc epydoc/doc

%files gui
%{_bindir}/epydocgui
%if ! 0%{?_module_build}
%{_datadir}/applications/epydocgui.desktop
%endif
%{_mandir}/man1/epydocgui.1*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.1.20090203svn-10
- Remove /usr/bin/python invocations and modernize a bit

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.1.20090203svn-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Karsten Hopp <karsten@redhat.com> - 3.0.1.20090203svn-6
- use new _module_build macro to limit dependencies for Modularity

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1.20090203svn-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> 3.0.1.20090203svn-3
- Use Recommends for tex dependencies
- Minor spec fixes
- Split gui sub-pkg

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015  Athmane Madjoudj <athmane@fedoraproject.org> 3.0.1.20090203svn-1
- Update to trunk
- Add patch to remove timestamp for reproducible builds (RHBZ #1122654)
- Rebase default img format patch
- Fix bugus date/time in the changelog
- Add patch to fix relative import parsing (RHBZ #1166283)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.1-12
- Requires: tex(dvips) tex(latex)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 Lubomir Rintel <lkundrak@v3.sk> 3.0.1-7
- Fix crash with newer docutils (#578920)

* Tue Dec  8 2009 Matthias Saou <http://freshrpms.net/> 3.0.1-6
- Add texlive-dvips and texlive-latex requirements (#522249).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 3.0.1-3
- Include patch to use png instead of gif for generated images (#459857).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.1-2
- Rebuild for Python 2.6

* Sat Mar 22 2008 Matthias Saou <http://freshrpms.net/> 3.0.1-1
- Update to 3.0.1.
- Update nohashbang patch.
- Include new apirst2html script, but remove .py extension to avoid .pyc/pyo.
- Include egg-info file.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.1-8
- Remove desktop file prefix and X-Fedora category.
- Include patch to remove #! python from files only meant to be included.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 2.1-7
- Rebuild against python 2.5.
- Remove no longer needed explicit python-abi requirement.
- Change python build requirement to python-devel, as it's needed now.

* Wed Sep  6 2006 Matthias Saou <http://freshrpms.net/> 2.1-6
- No longer ghost the .pyo files, as per new python guidelines (#205374).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.1-5
- FC6 rebuild.
- Add %%{?dist} tag.
- Update summary line.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Dec 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 2.1-3
- Change to noarch.
- Get Python site-packages dir from distutils, should fix x86_64 build.
- Require python-abi and tkinter.
- %%ghost'ify *.pyo.
- Fix man page permissions.
- Add menu entry for epydocgui.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.1-2
- Bump release to provide Extras upgrade path.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 2.1-1
- Picked up and rebuilt.
- Added doc and man pages.

* Fri May 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.1-0.fdr.1: Initial package

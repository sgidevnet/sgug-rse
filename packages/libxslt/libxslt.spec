Name:           libxslt
Summary:        Library providing the Gnome XSLT engine
Version:        1.1.34
Release:        1%{?dist}

License:        MIT
URL:            http://xmlsoft.org/XSLT
Source:         ftp://xmlsoft.org/XSLT/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  %{_bindir}/libgcrypt-config
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27

# Fedora specific patches
#Patch0:         multilib.patch
Patch1:         libxslt-1.1.26-utf8-docs.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1467435
#Patch2:         multilib2.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libgcrypt-devel%{?_isa}
Requires:       libgpg-error-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0
# Upstream package has not been ported to Python 3.  I have
# converted this section so it could be used to compile the
# Python 3 bindings one day once that has happened, but
# commented it out.  - RWMJ 2019-09-10
%package -n python3-libxslt
Summary:        Python 3 bindings for %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-libxml2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-libxml2
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-libxslt
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.
%endif

%prep
%autosetup -p1
chmod 644 python/tests/*

%build
autoreconf -vfi
#export PYTHON=%{__python3}
#%configure --disable-static --disable-silent-rules --with-python
%configure --disable-static --disable-silent-rules --with-python=no
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -print -delete
# multiarch crazyness on timestamp differences
touch -m --reference=%{buildroot}%{_includedir}/libxslt/xslt.h %{buildroot}%{_bindir}/xslt-config
rm -vrf %{buildroot}%{_docdir}

%check
%make_build tests

#%%ldconfig_scriptlets

%files
%license Copyright
%doc AUTHORS ChangeLog NEWS README FEATURES
%{_bindir}/xsltproc
%{_libdir}/libxslt.so.*
%{_libdir}/libexslt.so.*
%{_libdir}/libxslt-plugins/
%{_mandir}/man1/xsltproc.1*

%files devel
%doc doc/libxslt-api.xml
%doc doc/libxslt-refs.xml
%doc doc/EXSLT/libexslt-api.xml
%doc doc/EXSLT/libexslt-refs.xml
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/images
%doc doc/tutorial
%doc doc/tutorial2
%doc doc/EXSLT
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/xsltConf.sh
%{_datadir}/aclocal/libxslt.m4
%{_includedir}/libxslt/
%{_includedir}/libexslt/
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_bindir}/xslt-config

%if 0
%files -n python3-libxslt
%{python3_sitearch}/libxslt.py*
%{python3_sitearch}/libxsltmod.so
%{python3_sitearch}/__pycache__/nbd*.py*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl
%endif

%changelog
* Tue Aug 18 2020  HAL <notes2@gmx.de> - 
- update to the latest version

* Mon Mar 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.1.34-1
- 1.1.34

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.33-4
- Do not build python bindings even if the python is available
- Fix CVE-2019-13117 (#1728547)
- Fix CVE-2019-13118 (#1728542)

* Tue Sep 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.33-3
- Comment out Python bindings until upstream can convert them to Python 3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 David King <amigadave@amigadave.com> - 1.1.33-1
- Update to 1.1.33
- Fix CVE-2019-11068 (#1709698)

* Mon May 06 2019 Artem S. Tashkinov <artem@tashkinov.com> - 1.1.32-5
- Apply an extra patch to fix PR1467435 and make it possible to coinstall
  libxslt-devel.x64 and libxslt-devel.i686

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.32-2
- Fix typo in Requires

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.32-1
- Update to 1.1.32
- Cleanup spec
- Re-enable hardened build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.30-4
- Switch to %%ldconfig_scriptlets

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.30-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Oct 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.30-2
- Fix broken xslt-config binary

* Mon Sep  4 2017 Daniel Veillard <veillard@redhat.com> 1.1.30-1
- Update to 1.1.30

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.29-6
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.29-5
- Python 2 binary package renamed to python2-libxslt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Petr Pisar <ppisar@redhat.com> - 1.1.29-2
- Rebuild against glibc without xlocale.h (bug #1464640)

* Wed Mar 08 2017 Petr Šabata <contyk@redhat.com> - 1.1.29-1
- 1.1.29 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Daniel Veillard <veillard@redhat.com> 1.1.28-10
- desactivate the hardened build as it seems buggy #1199522

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.1.28-9
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomas Mraz <tmraz@redhat.com> - 1.1.28-6
- Rebuild for new libgcrypt

* Tue Aug  6 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.1.28-5
- Fix build with unversioned %%{_docdir_fmt}, ship Python examples only once.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1.1.28-3
- Don't ship api docs twice (they were included in both
  the main and the devel package, by accident (need to save
  space on the f19 live images)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Daniel Veillard <veillard@redhat.com> - 1.1.28-1
- upstream release of libxslt-1.1.28
- a few bug fixes and cleanups

* Tue Oct  9 2012 Daniel Veillard <veillard@redhat.com> - 1.1.27-2
- fix a regression in default namespace handling

* Wed Sep 12 2012 Daniel Veillard <veillard@redhat.com> - 1.1.27-1
- upstream release of libxslt-1.1.27
- a lot of bug fixes and improvements

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Michel Salim <salimma@fedoraproject.org> - 1.1.26-8
- ChangeLog: fix character encoding
- Restore timestamps for patched documentation files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Dan Horák <dan[at]danny.cz> - 1.1.26-6
- libexslt needs libgcrypt-devel via its pkgconfig file

* Mon Oct 25 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.1.26-5
- Patch from Paul Howarth for converting files to utf8 (#226088)

* Tue Oct 05 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.1.26-4
- Merge-review cleanup (#226088)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.26-2
- disable static libs

* Thu Sep 24 2009 Daniel Veillard <veillard@redhat.com> 1.1.26-1
- couple of bug fixes
- export a symbol needed by lxml

* Mon Sep 21 2009 Daniel Veillard <veillard@redhat.com> 1.1.25-2
- fix a locking bug in 1.1.25

* Thu Sep 17 2009 Daniel Veillard <veillard@redhat.com> 1.1.25-1
- release of 1.1.25
- Add API versioning  for libxslt shared library
- xsl:sort lang support using the locale
- many bug fixes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.24-3
- Rebuild for Python 2.6

* Wed Oct  8 2008 Daniel Veillard <veillard@redhat.com> 1.1.24-2.fc10
- CVE-2008-2935 fix

* Tue May 13 2008 Daniel Veillard <veillard@redhat.com> 1.1.24-1.fc10
- release of 1.1.24
- fixes a few bugs including the key initialization problem
- tentative fix for multiarch devel problems

* Mon Apr 28 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-3.fc10
- and the previous patch was incomplte breaking the python bindings
  see 444317 and 444455

* Tue Apr 22 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-2.fc10
- revert a key initialization patch from 1.1.23 which seems broken
  see rhbz#442097

* Tue Apr  8 2008 Daniel Veillard <veillard@redhat.com> 1.1.23-1.fc9
- upstream release 1.1.23
- bugfixes

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.22-2
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Daniel Veillard <veillard@redhat.com> 1.1.22-1
- upstream release 1.1.22 see http://xmlsoft.org/XSLT/news.html

* Tue Jun 12 2007 Daniel Veillard <veillard@redhat.com> 1.1.21-1
- upstream release 1.1.21 see http://xmlsoft.org/XSLT/news.html

* Thu Feb 15 2007 Adam Jackson <ajax@redhat.com>
- Add dist tag to Release to fix 6->7 upgrades.

* Wed Jan 17 2007 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.20 see http://xmlsoft.org/XSLT/news.html

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.1.19-2
- rebuild against python 2.5

* Wed Nov 29 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.19 see http://xmlsoft.org/XSLT/news.html

* Thu Oct 26 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.18 see http://xmlsoft.org/XSLT/news.html

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.17-1.1
- rebuild

* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 1.1.17 see http://xmlsoft.org/XSLT/news.html

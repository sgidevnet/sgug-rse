# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Name:           libxml2
Version:        2.9.9
Release:        3%{?dist}
Summary:        Library providing XML and HTML support

License:        MIT
URL:            http://xmlsoft.org/
Source:         ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch0:         libxml2-multilib.patch
# Patch from openSUSE.
# See:  https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch1:         libxml2-2.9.8-python3-unicode-errors.patch

BuildRequires:  gcc
BuildRequires:  make
#BuildRequires:  cmake-rpm-macros
BuildRequires:  zlib-devel
BuildRequires:  xz-devel

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary:        Libraries, includes, etc. to develop XML and HTML applications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}
Requires:       xz-devel%{?_isa}

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package static
Summary:        Static library for libxml2

%description static
Static library for libxml2 provided for specific uses or shaving a few
microseconds when parsing, do not link to them for generic purpose packages.

#%package -n python2-%{name}
#%{?python_provide:%python_provide python2-%{name}}
#Summary:        Python bindings for the libxml2 library
#BuildRequires:  python2-devel
#Requires:       %{name}%{?_isa} = %{version}-%{release}
#Obsoletes:      %{name}-python < %{version}-%{release}
#Provides:       %{name}-python = %{version}-%{release}

#%description -n python2-%{name}
#The libxml2-python package contains a Python 2 module that permits applications
#written in the Python programming language, version 2, to use the interface
#supplied by the libxml2 library to manipulate XML files.

#This library allows to manipulate XML files. It includes support
#to read, modify and write XML and HTML files. There is DTDs support
#this includes parsing and validation even with complex DTDs, either
#at parse time or later once the document has been modified.

#%package -n python3-%{name}
#Summary:        Python 3 bindings for the libxml2 library
#BuildRequires:  python3-devel
#Requires:       %{name}%{?_isa} = %{version}-%{release}
#Obsoletes:      %{name}-python3 < %{version}-%{release}
#Provides:       %{name}-python3 = %{version}-%{release}

#%description -n python3-%{name}
#The libxml2-python3 package contains a Python 3 module that permits
#applications written in the Python programming language, version 3, to use the
#interface supplied by the libxml2 library to manipulate XML files.

#This library allows to manipulate XML files. It includes support
#to read, modify and write XML and HTML files. There is DTDs support
#this includes parsing and validation even with complex DTDs, either
#at parse time or later once the document has been modified.

%prep

%autosetup -p1
find doc -type f -executable -print -exec chmod 0644 {} ';'

%build
# Rewrite the default catalogs to our intended paths
perl -pi -e "s|/etc/sgml/catalog|%{_prefix}/etc/sgml/catalog|g" catalog.c
perl -pi -e "s|/etc/sgml/catalog|%{_prefix}/etc/sgml/catalog|g" xmlcatalog.c

perl -pi -e "s|/etc/xml/catalog|%{_prefix}/etc/xml/catalog|g" catalog.c
perl -pi -e "s|/etc/xml/catalog|%{_prefix}/etc/xml/catalog|g" xmlcatalog.c

%global _configure_disable_silent_rules 1
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=%{buildroot}%{_includedir}/libxml2/libxml/parser.h %{buildroot}%{_bindir}/xml2-config

find %{buildroot} -type f -name '*.la' -print -delete
rm -vf %{buildroot}{%{python2_sitearch},%{python3_sitearch}}/*.a
rm -vrf %{buildroot}%{_datadir}/doc/
#(cd doc/examples ; make clean ; rm -rf .deps Makefile)
gzip -9 -c doc/libxml2-api.xml > doc/libxml2-api.xml.gz

%check
%make_build runtests -C py2
%make_build runtests -C py3

#%ldconfig_scriptlets

%files
%license Copyright
%doc AUTHORS NEWS README TODO
%{_libdir}/libxml2.so.2*
%{_mandir}/man3/libxml.3*
%{_bindir}/xmllint
%{_mandir}/man1/xmllint.1*
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmlcatalog.1*

%files devel
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxml2/
%{_libdir}/libxml2.so
%{_libdir}/xml2Conf.sh
%{_includedir}/libxml2/
%{_bindir}/xml2-config
%{_mandir}/man1/xml2-config.1*
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/

%files static
%license Copyright
%{_libdir}/libxml2.a

#%files -n python2-%{name}
#%doc python/TODO python/libxml2class.txt
#%doc doc/*.py doc/python.html
#%{python2_sitearch}/libxml2.py*
#%{python2_sitearch}/drv_libxml2.py*
#%{python2_sitearch}/libxml2mod.so

#%files -n python3-%{name}
#%doc python/TODO python/libxml2class.txt
#%doc doc/*.py doc/python.html
#%{python3_sitearch}/libxml2.py
#%{python3_sitearch}/__pycache__/libxml2.*
#%{python3_sitearch}/drv_libxml2.py
#%{python3_sitearch}/__pycache__/drv_libxml2.*
#%{python3_sitearch}/libxml2mod.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 David King <amigadave@amigadave.com> - 2.9.9-1
- Update to 2.9.9

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 2.9.8-5
- Add patch to fix crash: xmlParserPrintFileContextInternal mangles utf8

* Thu Aug 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.8-4
- Backport patches from upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.8-2
- Rebuilt for Python 3.7

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.8-1
- Update to 2.9.8

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 2.9.7-4
- Rebuild with new LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.7-2
- Switch to %%ldconfig_scriptlets

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.7-1
- Update to 2.9.7
- Cleanups in packaging

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.9.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Sep 22 2017 Petr Pisar <ppisar@redhat.com> - 2.9.5-2
- Fix reporting error about undefined XPath variables (bug #1493613)

* Mon Sep  4 2017 Daniel Veillard <veillard@redhat.com> - 2.9.5-1
- update to 2.9.5

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.9.4-5
- Python 2 binary package renamed to python2-libxml2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Kevin Fenzi <kevin@scrye.com> - 2.9.4-1
- Update to 2.9.4.
- Apply very hacky patch that removes the no longer in python-3.6 PyVerify_fd symbol.

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.9.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Kalev Lember <klember@redhat.com> - 2.9.3-2
- Fix obsoletes versions now that F22 has libxml2 2.9.3 (#1287262)

* Fri Nov 20 2015 Daniel Veillard <veillard@redhat.com> - 2.9.2-1
- upstream release of 2.9.3
- Fixes for CVE-2015-8035, CVE-2015-7942, CVE-2015-7941, CVE-2015-1819
  CVE-2015-7497, CVE-2015-7498, CVE-2015-5312, CVE-2015-7499, CVE-2015-7500
  and CVE-2015-8242
- many other bug fixes

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 2.9.2-9
- Rebuilt for Python3.5 rebuild
- Python3.5 has new naming convention for byte compiled files

* Tue Nov  3 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 2.9.2-8
- Remove executable permissions from documentation.  Complies with packaging
  guidelines and solves issue of libxml2-python3 package depending on python2

* Thu Aug 27 2015 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-7
- Remove dependency on python2 from python3 subpackage, rhbz#1250940

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 2.9.2-6
- Rename the Python 3 subpackage to python3-libxml2 as per guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.9.2-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 2.9.2-3
- Added Python 3 subpackage

* Thu Oct 16 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.9.2-2
- Avoid corrupting the xml catalogs

* Thu Oct 16 2014 Daniel Veillard <veillard@redhat.com> - 2.9.2-1
- upstream release of 2.9.2
- Fix for CVE-214-3660 billion laugh DOS
- many other bug fixes

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 2.9.1-4
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Daniel Veillard <veillard@redhat.com> - 2.9.1-1
- upstream release of 2.9.1
- a couple more API entry point
- compatibility with python3
- a lot of bug fixes

* Mon Feb 11 2013 Daniel Veillard <veillard@redhat.com> - 2.9.0-4
- fix --nocheck build which I broke in october rhbz#909767

* Mon Nov 19 2012 Jaroslav Reznik <jreznik@redhat.com> - 2.9.0-3
- workaround for crc/len check failure, rhbz#877567

* Thu Oct 11 2012 Daniel Veillard <veillard@redhat.com> - 2.9.0-2
- remaining cleanups from merge bug rhbz#226079
- do not put the docs in the main package, only in -devel rhbz#864731

* Tue Sep 11 2012 Daniel Veillard <veillard@redhat.com> - 2.9.0-1
- upstream release of 2.9.0
- A few new API entry points
- More resilient push parser mode
- A lot of portability improvement
- Faster XPath evaluation
- a lot of bug fixes and smaller improvement

* Fri Aug 10 2012 Daniel Veillard <veillard@redhat.com> - 2.9.0-0rc1
- upstream release candidate 1 of 2.9.0
- introduce a small API change, but ABI compatible, see
  https://mail.gnome.org/archives/xml/2012-August/msg00005.html
  patches for php, gcc/libjava and evolution-data-connector are upstream
  Grab me in cases of problems veillard@redhat.com
- many bug fixes including security aspects and small improvements

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Daniel Veillard <veillard@redhat.com> - 2.8.0-1
- upstream release of 2.8.0
- add lzma compression support
- many bug fixes and small improvements

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar  4 2011 Daniel Veillard <veillard@redhat.com> - 2.7.8-6
- fix a double free in XPath CVE-2010-4494 bug 665965

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  5 2010 Daniel Veillard <veillard@redhat.com> - 2.7.8-4
- reactivate shared libs versionning script

* Thu Nov  4 2010 Daniel Veillard <veillard@redhat.com> - 2.7.8-1
- Upstream release of 2.7.8
- various bug fixes, including potential crashes
- new non-destructive formatting option
- date parsing updated to RFC 5646

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar 15 2010 Daniel Veillard <veillard@redhat.com> - 2.7.7-1
- Upstream release of 2.7.7
- fix serious trouble with zlib >= 1.2.4
- xmllint new option --xpath
- various HTML parser improvements
- includes a number of nug fixes

* Tue Oct  6 2009 Daniel Veillard <veillard@redhat.com> - 2.7.6-1
- Upstream release of 2.7.6
- restore thread support off by default in 2.7.5

* Thu Sep 24 2009 Daniel Veillard <veillard@redhat.com> - 2.7.5-1
- Upstream release of 2.7.5
- fix a couple of Relax-NG validation problems
- couple more fixes

* Tue Sep 15 2009 Daniel Veillard <veillard@redhat.com> - 2.7.4-2
- fix a problem with little data at startup affecting inkscape #523002

* Thu Sep 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.4-1
- upstream release 2.7.4
- symbol versioning of libxml2 shared libs
- very large number of bug fixes

* Mon Aug 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-4
- two patches for parsing problems CVE-2009-2414 and CVE-2009-2416

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-1
- new release 2.7.3
- limit default max size of text nodes
- special parser mode for PHP
- bug fixes and more compiler checks

* Wed Dec  3 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-7
- Pull back into Python 2.6

* Wed Dec  3 2008 Caolán McNamara <caolanm@redhat.com> - 2.7.2-6
- AutoProvides requires BuildRequires pkgconfig

* Wed Dec  3 2008 Caolán McNamara <caolanm@redhat.com> - 2.7.2-5
- rebuild to get provides(libxml-2.0) into HEAD rawhide

* Mon Dec  1 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-4
- Rebuild for pkgconfig logic

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-3
- Rebuild for Python 2.6

* Wed Nov 12 2008 Daniel Veillard <veillard@redhat.com> - 2.7.2-2.fc11
- two patches for size overflows problems CVE-2008-4225 and CVE-2008-4226

* Fri Oct  3 2008 Daniel Veillard <veillard@redhat.com> 2.7.2-1.fc10
- new release 2.7.2
- Fixes the known problems in 2.7.1
- increase the set of options when saving documents

* Thu Oct  2 2008 Daniel Veillard <veillard@redhat.com> 2.7.1-2.fc10
- fix a nasty bug in 2.7.x, http://bugzilla.gnome.org/show_bug.cgi?id=554660

* Mon Sep  1 2008 Daniel Veillard <veillard@redhat.com> 2.7.1-1.fc10
- fix python serialization which was broken in 2.7.0
- Resolve: rhbz#460774

* Sat Aug 30 2008 Daniel Veillard <veillard@redhat.com> 2.7.0-1.fc10
- upstream release of 2.7.0
- switch to XML 1.0 5th edition
- switch to RFC 3986 for URI parsing
- better entity handling
- option to remove hardcoded limitations in the parser
- more testing
- a new API to allocate entity nodes
- and lot of fixes and clanups

* Mon Aug 25 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-4.fc10
- fix for entities recursion problem
- Resolve: rhbz#459714

* Fri May 30 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-3.fc10
- cleanup based on Fedora packaging guidelines, should fix #226079
- separate a -static package

* Thu May 15 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-2.fc10
- try to fix multiarch problems like #440206

* Tue Apr  8 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-1.fc9
- upstream release 2.6.32 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.31-2
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Daniel Veillard <veillard@redhat.com> 2.6.31-1.fc9
- upstream release 2.6.31 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Thu Aug 23 2007 Daniel Veillard <veillard@redhat.com> 2.6.30-1
- upstream release 2.6.30 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Tue Jun 12 2007 Daniel Veillard <veillard@redhat.com> 2.6.29-1
- upstream release 2.6.29 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Wed May 16 2007 Matthias Clasen <mclasen@redhat.com> 2.6.28-2
- Bump revision to fix N-V-R problem

* Tue Apr 17 2007 Daniel Veillard <veillard@redhat.com> 2.6.28-1
- upstream release 2.6.28 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.6.27-2
- rebuild against python 2.5

* Wed Oct 25 2006 Daniel Veillard <veillard@redhat.com> 2.6.27-1
- upstream release 2.6.27 see http://xmlsoft.org/news.html
- very large amount of bug fixes reported upstream

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.26-2.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.26-2.1
- rebuild

* Wed Jun  7 2006 Daniel Veillard <veillard@redhat.com> 2.6.26-2
- fix bug #192873
* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com> 2.6.26-1
- upstream release 2.6.26 see http://xmlsoft.org/news.html

* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 2.6.25 broken, do not ship !


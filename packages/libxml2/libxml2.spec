# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Name:           libxml2
Version:        2.9.9
Release:        7%{?dist}
Summary:        Library providing XML and HTML support

License:        MIT
URL:            http://xmlsoft.org/
Source:         ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch0:         libxml2-multilib.patch
# Patch from openSUSE.
# See:  https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch1:         libxml2-2.9.8-python3-unicode-errors.patch

Patch100:       libxml2.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake-rpm-macros
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

%package -n python2-%{name}
%{?python_provide:%python_provide python2-%{name}}
Summary:        Python bindings for the libxml2 library
BuildRequires:  python2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python < %{version}-%{release}
Provides:       %{name}-python = %{version}-%{release}

%description -n python2-%{name}
The libxml2-python package contains a Python 2 module that permits applications
written in the Python programming language, version 2, to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%package -n python3-%{name}
Summary:        Python 3 bindings for the libxml2 library
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
Provides:       %{name}-python3 = %{version}-%{release}

%description -n python3-%{name}
The libxml2-python3 package contains a Python 3 module that permits
applications written in the Python programming language, version 3, to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep

%autosetup -p1

# A place to regenerate the sgug patch
#exit 1

find doc -type f -executable -print -exec chmod 0644 {} ';'

%build
mkdir py2
mkdir py3
# Rewrite the default catalogs to our intended paths
perl -pi -e "s|/etc/sgml/catalog|%{_prefix}/etc/sgml/catalog|g" catalog.c
perl -pi -e "s|/etc/sgml/catalog|%{_prefix}/etc/sgml/catalog|g" xmlcatalog.c

perl -pi -e "s|/etc/xml/catalog|%{_prefix}/etc/xml/catalog|g" catalog.c
perl -pi -e "s|/etc/xml/catalog|%{_prefix}/etc/xml/catalog|g" xmlcatalog.c

%global _configure ../configure
%global _configure_disable_silent_rules 1
#%%configure --without-python
export PREV_WD=`pwd`
( cd py2 && %configure --with-python=%{__python2} )
cd $PREV_WD
%make_build -C py2
( cd py3 && %configure --with-python=%{__python3} )
%make_build -C py3

%install
%make_install -C py2
%make_install -C py3

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

#%%ldconfig_scriptlets

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

%files -n python2-%{name}
%doc python/TODO python/libxml2class.txt
%doc doc/*.py doc/python.html
%{python2_sitearch}/libxml2.py*
%{python2_sitearch}/drv_libxml2.py*
%{python2_sitearch}/libxml2mod.so

%files -n python3-%{name}
%doc python/TODO python/libxml2class.txt
%doc doc/*.py doc/python.html
%{python3_sitearch}/libxml2.py
%{python3_sitearch}/__pycache__/libxml2.*
%{python3_sitearch}/drv_libxml2.py
%{python3_sitearch}/__pycache__/drv_libxml2.*
%{python3_sitearch}/libxml2mod.so

%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 2.9.9-7
- Include python2 bindings generation

* Fri Jun 12 2020 Daniel Hams <daniel.hams@gmail.com> - 2.9.9-6
- Fix up broken xml2-config script

* Mon Jun 01 2020 Daniel Hams <daniel.hams@gmail.com> - 2.9.9-5
- Activate python3 bindings (but still a little bit broken as no autocompilation)

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 2.9.9-4
- Ensure no python pulled in

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 David King <amigadave@amigadave.com> - 2.9.9-1
- Update to 2.9.9

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 2.9.8-5
- Add patch to fix crash: xmlParserPrintFileContextInternal mangles utf8

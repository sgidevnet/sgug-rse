Name:           libxslt
Summary:        Library providing the Gnome XSLT engine
Version:        1.1.33
Release:        4%{?dist}

License:        MIT
URL:            http://xmlsoft.org/XSLT
Source:         ftp://xmlsoft.org/XSLT/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
#BuildRequires:  %{_bindir}/libgcrypt-config
#BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  libxml2-devel

# Fedora specific patches
Patch0:         multilib.patch
Patch1:         libxslt-1.1.26-utf8-docs.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1467435
Patch2:         multilib2.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1709698
Patch3:         CVE-2019-11068.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
#Requires:       libgcrypt-devel%{?_isa}
#Requires:       libgpg-error-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python2-libxslt
Summary:        Python 2 bindings for %{name}
BuildRequires:  python2-devel
BuildRequires:  python2-libxml2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python2-libxml2
%{?python_provide:%python_provide python2-libxslt}
# Remove before F30
Provides:       %{name}-python = %{version}-%{release}
Provides:       %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python < %{version}-%{release}
%description -n python2-libxslt
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.

%prep
%autosetup -p1
#chmod 644 python/tests/*

%build

autoreconf -vfi
export PYTHON=%{__python2}
#%%configure --disable-static --disable-silent-rules --with-python
%configure --disable-static --disable-silent-rules --with-python
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

%files -n python2-libxslt
%{python2_sitearch}/libxslt.py*
%{python2_sitearch}/libxsltmod.so
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 1.1.33-4
- Enable python2 library bindings

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 1.1.33-3
- Ensure no pulling in of python

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

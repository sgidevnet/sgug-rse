%if 0%{?rhel} == 8
%bcond_with python2
%bcond_with php
%else
%bcond_without python2
%bcond_without php
%endif

# Necessary conditionals
%ifarch %{mono_arches}
%global SHARP  1
%else
%global SHARP  0
%endif

%global OCAML  1

%global DEVIL  1
%global ARRRR  1

# Build with QT applications (currently only gvedit)
# Disabled until the package gets better structuring, see bug #447133
%global QTAPPS 0

%global GTS    1
%global LASI   1

# Not in Fedora yet.
%global MING   0

%if 0%{?rhel}
%global SHARP  0
%global ARRRR  0
%global DEVIL  0
%global GTS    0
%global LASI   0
%endif

%if %{with php}
%global PHP 1
%else
%global PHP 0
%endif

# Plugins version
%global pluginsver 6

%global php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

%if "%{php_version}" < "5.6"
%global ini_name     %{name}.ini
%else
%global ini_name     40-%{name}.ini
%endif

# Fix for the 387 extended precision (rhbz#772637)
%ifarch i386 i686
%global FFSTORE -ffloat-store
%endif

Name:			graphviz
Summary:		Graph Visualization Tools
Version:		2.40.1
Release:		56%{?dist}
License:		EPL-1.0
URL:			http://www.graphviz.org/
# A bit hacking needed due to: https://gitlab.com/graphviz/graphviz/issues/1371
Source0:		https://gitlab.com/graphviz/graphviz/-/archive/stable_release_%{version}/graphviz-stable_release_%{version}.tar.gz #/graphviz-2.40.1.tar.gz
Patch0:			graphviz-2.40.1-visio.patch
Patch1:			graphviz-2.40.1-python3.patch
# https://gitlab.com/graphviz/graphviz/issues/1367
Patch2:			graphviz-2.40.1-CVE-2018-10196.patch
# rhbz#1505230
Patch3:			graphviz-2.40.1-dotty-menu-fix.patch
Patch4:			graphviz-2.40.1-coverity-scan-fixes.patch
Patch5:			graphviz-2.40.1-CVE-2019-11023.patch
Patch6:			graphviz-2.40.1-swig4-updated-language-options.patch

BuildRequires:		zlib-devel, libpng-devel, libjpeg-devel, expat-devel, freetype-devel >= 2
#BuildRequires:		ksh, bison, m4, flex, tk-devel, tcl-devel >= 8.3, swig, sed
#BuildRequires:		fontconfig-devel, libtool-ltdl-devel, ruby-devel, ruby, guile-devel
%if %{with python2}
BuildRequires:		python2-devel
%endif
#BuildRequires:		python3-devel, libXaw-devel, libSM-devel, libXext-devel, java-devel
BuildRequires:		cairo-devel >= 1.1.10, pango-devel, gmp-devel, lua-devel, gtk2-devel
#BuildRequires:		gd-devel, perl-devel, swig >= 1.3.33, automake, autoconf, libtool, qpdf
BuildRequires:		gd-devel, perl-devel, swig >= 1.3.33, automake, autoconf, libtool
# Temporary workaound for perl(Carp) not pulled
BuildRequires:		perl-Carp
#%%if #%%{PHP}
#BuildRequires:		php-devel
#%%endif
#%%if #%%{SHARP}
#BuildRequires:		mono-core
#%%endif
#%%if #%%{DEVIL}
#BuildRequires:		DevIL-devel
#%%endif
#%%if #%%{ARRRR}
#BuildRequires:		R-devel
#%%endif
#%%if #%%{OCAML}
#BuildRequires:		ocaml
#%%endif
#%%if #%%{QTAPPS}
#BuildRequires:		qt-devel
#%%endif
#%%if #%%{GTS}
#BuildRequires:		gts-devel
#%%endif
#%%if #%%{LASI}
#BuildRequires:		lasi-devel
#%%endif
#BuildRequires:		urw-base35-fonts, perl-ExtUtils-Embed, perl-generators, librsvg2-devel
# for ps2pdf
#BuildRequires:		ghostscript
#BuildRequires:		libgs-devel
# ISO8859-1 fonts are required by lefty
#Requires:		urw-base35-fonts, xorg-x11-fonts-ISO8859-1-100dpi
#Requires(post):		/sbin/ldconfig
#Requires(postun):	/sbin/ldconfig

%description
A collection of tools for the manipulation and layout of graphs (as in nodes
and edges, not as in barcharts).

%package devel
Summary:		Development package for graphviz
Requires:		%{name} = %{version}-%{release}, pkgconfig
Requires:		%{name}-gd = %{version}-%{release}

%description devel
A collection of tools for the manipulation and layout of graphs (as in nodes
and edges, not as in barcharts). This package contains development files for
graphviz.

#%%if #%%{DEVIL}
#%%package devil
#Summary:		Graphviz plugin for renderers based on DevIL
#Requires:		#%%{name} = #%%{version}-#%%{release}

#%%description devil
#Graphviz plugin for renderers based on DevIL. (Unless you absolutely have
#to use BMP, TIF, or TGA, you are recommended to use the PNG format instead
#supported directly by the cairo+pango based renderer in the base graphviz rpm.)
#%%endif

#%%package doc
#Summary:		PDF and HTML documents for graphviz

#%%description doc
#Provides some additional PDF and HTML documentation for graphviz.

%package gd
Summary:		Graphviz plugin for renderers based on gd
Requires:		%{name} = %{version}-%{release}
#Requires(post):		#%%{_bindir}/dot /sbin/ldconfig
#Requires(postun):	#%%{_bindir}/dot /sbin/ldconfig

%description gd
Graphviz plugin for renderers based on gd.  (Unless you absolutely have to use
GIF, you are recommended to use the PNG format instead because of the better
quality anti-aliased lines provided by the cairo+pango based renderer.)

%package graphs
Summary:		Demo graphs for graphviz

%description graphs
Some demo graphs for graphviz.

#%%package guile
#Summary:		Guile extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}, guile

#%%description guile
#Guile extension for graphviz.

#%%package java
#Summary:		Java extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}

#%%description java
#Java extension for graphviz.

%package lua
Summary:		Lua extension for graphviz
Requires:		%{name} = %{version}-%{release}, lua

%description lua
Lua extension for graphviz.

#%%if #%%{MING}
#%%package ming
#Summary:		Graphviz plugin for flash renderer based on ming
#Requires:		#%%{name} = #%%{version}-#%%{release}

#%%description ming
#Graphviz plugin for -Tswf (flash) renderer based on ming.
#%%endif

#%%if #%%{OCAML}
#%%package ocaml
#Summary:		Ocaml extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}, ocaml

#%%description ocaml
#Ocaml extension for graphviz.
#%%endif

%package perl
Summary:		Perl extension for graphviz
Requires:		%{name} = %{version}-%{release}
#Requires:		perl(:MODULE_COMPAT_#%%(eval "`#%%{__perl} -V:version`"; echo $version))

%description perl
Perl extension for graphviz.

#%%if #%%{PHP}
#%%package php
#Summary:		PHP extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}
#Requires:	php(zend-abi) = #%%{?php_zend_api}#%%{?!php_zend_api:UNDEFINED}
#Requires:	php(api) = #%%{?php_core_api}#%%{?!php_core_api:UNDEFINED}

#%%description php
#PHP extension for graphviz.
#%%endif

%if %{with python2}
%package python2
Summary:		Python extension for graphviz
Requires:		%{name} = %{version}-%{release}
# Manually add provides that would be generated automatically if .egg-info was present
Provides: python2dist(gv) = %{version}
Provides: python%{python2_version}dist(gv) = %{version}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < 2.40.1-25
Obsoletes: python2-%{name} < 2.40.1-25

%description python2
Python extension for graphviz.
%endif

%package python3
Summary:		Python 3 extension for graphviz
Requires:		%{name} = %{version}-%{release}
# Manually add provides that would be generated automatically if .egg-info was present
Provides: python3dist(gv) = %{version}
Provides: python%{python3_version}dist(gv) = %{version}

%description python3
Python 3 extension for graphviz.

#%%if #%%{ARRRR}
#%%package R
#Summary:		R extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}, R-core

#%%description R
#R extension for graphviz.
#%%endif

#%%package ruby
#Summary:		Ruby extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}, ruby

#%%description ruby
#Ruby extension for graphviz.

#%%if #%%{SHARP}
#%%package sharp
#Summary:		C# extension for graphviz
#Requires:		#%%{name} = #%%{version}-#%%{release}, mono-core

#%%description sharp
#C# extension for graphviz.
#%%endif

%package tcl
Summary:		Tcl extension & tools for graphviz
Requires:		%{name} = %{version}-%{release}, tcl >= 8.3, tk

%description tcl
Various tcl packages (extensions) for the graphviz tools.

%prep
%setup -q -n graphviz-stable_release_%{version}
%patch0 -p1 -b .visio
%patch1 -p1 -b .python3
%patch2 -p1 -b .CVE-2018-10196
%patch3 -p1 -b .dotty-menu-fix
%patch4 -p1 -b .coverity-scan-fixes
%patch5 -p1 -b .CVE-2019-11023
%patch6 -p1 -b .swig4-updated-language-options

# Attempt to fix rpmlint warnings about executable sources
find -type f -regex '.*\.\(c\|h\)$' -exec chmod a-x {} ';'

%build

# Overwrite broken lua detection
export LUA_VERSION=`pkg-config --variable=V lua`
export LUA_INSTALL_DIR="%{_libdir}/lua/$LUA_VERSION"
export LUA_INCLUDES="%{_includedir}"
export LUA_LIBS=`pkg-config --libs lua`

perl -pi -e "s|LUA_INSTALL_DIR\=\"/usr/lib|LUA_INSTALL_DIR\=\"%{_prefix}/lib|g" configure.ac

# Ensure that configure is aware we are in lib32
export LIBPOSTFIX=32

# And fix up another hardcoded change of LDFLAGS that breaks linking
perl -pi -e "s|prefix\}\/lib\"|prefix\}\/lib${LIBPOSTFIX}\"|g" configure.ac
perl -pi -e "s|prefix\/lib\/pkgconfig|prefix\/lib${LIBPOSTFIX}\/pkgconfig|g" configure.ac

#exit 1

./autogen.sh
# Hack in the java includes we need
#sed -i '/JavaVM.framework/!s/JAVA_INCLUDES=/JAVA_INCLUDES=\"_MY_JAVA_INCLUDES_\"/g' configure
#sed -i 's|_MY_JAVA_INCLUDES_|-I%{java_home}/include/ -I%{java_home}/include/linux/|g' configure
# Rewrite config_ruby.rb to work with Ruby 2.2
#sed -i 's|expand(|expand(RbConfig::|' config/config_ruby.rb
#sed -i 's|sitearchdir|vendorarchdir|' config/config_ruby.rb

# get the path to search for ruby/config.h to CPPFLAGS, so that configure can find it

# We don't have ruby yet, so don't go looking for the include dir
#export CPPFLAGS=-I`ruby -e "puts File.join(RbConfig::CONFIG['includedir'], RbConfig::CONFIG['sitearch'])" || echo /dev/null`
# Be explicit about compilers
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
%configure --with-x --disable-static --disable-dependency-tracking \
	--without-mylibgd --with-ipsepcola --with-pangocairo \
	--with-gdk-pixbuf --with-visio --disable-silent-rules \
%if ! %{LASI}
	--without-lasi \
%endif
%if ! %{GTS}
	--without-gts \
%endif
%if ! %{SHARP}
	--disable-sharp \
%endif
%if ! %{OCAML}
	--disable-ocaml \
%endif
%if ! %{MING}
	--without-ming \
%endif
%if ! %{ARRRR}
	--disable-r \
%endif
%if ! %{DEVIL}
	--without-devil \
%endif
%if ! %{QTAPPS}
	--without-qt
%endif

# drop rpath (commented out for SGUG, we use RPATH)
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%if %{with python2}
cp -a tclpkg/gv tclpkg/gv.python2
%endif

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}" \
  CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}" \
  PYTHON_INCLUDES=`python3-config --includes` PYTHON_LIBS=`python3-config --libs` \
  PYTHON_INSTALL_DIR=%{python3_sitearch} PYTHON=%{__python3}

%if %{with python2}
#pushd 
PREVWD=`pwd`
cd tclpkg/gv.python2
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}" \
  CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow %{?FFSTORE}" \
  PYTHON_INCLUDES=-I/usr/sgug/include/python%{python2_version} PYTHON_LIBS="-lpython%{python2_version}" \
  PYTHON_INSTALL_DIR=%{python2_sitearch} libgv_python.la
cd $PREVWD
#popd
%endif

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} \
	docdir=%{buildroot}%{_docdir}/%{name} \
	pkgconfigdir=%{_libdir}/pkgconfig \
	PYTHON_LIBS=`python3-config --libs` \
	PYTHON_INSTALL_DIR=%{python3_sitearch} \
	install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
chmod -x %{buildroot}%{_datadir}/%{name}/lefty/*

# Move docs to the right place
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/doc/* %{buildroot}%{_docdir}/%{name}

# Install README
install -m0644 README %{buildroot}%{_docdir}/%{name}

#%%if %{PHP}
# PHP configuration file
#%%{__mkdir_p} #%%{buildroot}#%%{_sysconfdir}/php.d
#%%{__cat} << __EOF__ > %{buildroot}#%%{_sysconfdir}/php.d/#%%{ini_name}
#; Enable #%%{name} extension module
#extension=gv.so
#__EOF__
#%%endif

# Remove executable modes from demos
find %{buildroot}%{_datadir}/%{name}/demo -type f -exec chmod a-x {} ';'

# Move demos to doc
mv %{buildroot}%{_datadir}/%{name}/demo %{buildroot}%{_docdir}/%{name}/

# Rename python demos to prevent byte compilation
find %{buildroot}%{_docdir}/%{name}/demo -type f -name "*.py" -exec mv {} {}.demo ';'

# Remove dot_builtins, on demand loading should be sufficient
rm -f %{buildroot}%{_bindir}/dot_builtins

# Remove metadata from generated PDFs
#pushd 
#PREVWD=`pwd`
#cd #%%{buildroot}#%%{_docdir}/#%%{name}/pdf
#for f in prune lneato.1 lefty.1 gvgen.1 gc.1 dotty.1 dot.1 cluster.1
#do
#  if [ -f $f.pdf ]
#  then
# ugly, but there is probably no better solution
#    qpdf --empty --static-id --pages $f.pdf -- $f.pdf.$$
#    mv -f $f.pdf.$$ $f.pdf
#  fi
#done
#cd $PREVWD
#popd

%if %{with python2}
#pushd 
PREVWD=`pwd`
cd tclpkg/gv.python2
install -pD .libs/libgv_python.so %{buildroot}%{python2_sitearch}/_gv.so
install -p gv.py %{buildroot}%{python2_sitearch}/gv.py
cd $PREVWD
#popd
%endif

# python 3
#pushd 
PREVWD=`pwd`
cd tclpkg/gv
install -pD .libs/libgv_python.so %{buildroot}%{python3_sitearch}/_gv.so
install -p gv.py %{buildroot}%{python3_sitearch}/gv.py
cd $PREVWD
#popd

# remove the python module from the %%_libdir/graphviz/python, it's
# already installed in the python sitearch
rm -f %{buildroot}%{_libdir}/graphviz/python/*
rmdir %{buildroot}%{_libdir}/graphviz/python

# Ghost plugins config
touch %{buildroot}%{_libdir}/graphviz/config%{pluginsver}


#%%check
#%%if %{PHP}
# Minimal load test of php extension
#LD_LIBRARY_PATH=#%%{buildroot}#%%{_libdir} \
#php --no-php-ini \
#    --define extension_dir=#%%{buildroot}#%%{_libdir}/graphviz/php/ \
#    --define extension=libgv_php.so \
#    --modules | grep gv
#%%endif

# upstream test suite
# testsuite seems broken, disabling it for now
# cd rtest
# make rtest


%files
%doc %{_docdir}/%{name}
%{_bindir}/*
%dir %{_libdir}/graphviz
%{_libdir}/*.so.*
%{_libdir}/graphviz/*.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%dir %{_datadir}/graphviz
#%%exclude #%%{_docdir}/#%%{name}/html
#%%exclude #%%{_docdir}/#%%{name}/pdf
%exclude %{_docdir}/%{name}/demo
%{_datadir}/graphviz/lefty
%{_datadir}/graphviz/gvpr
%ghost %{_libdir}/graphviz/config%{pluginsver}

#%%if #%%{QTAPPS}
#%%{_datadir}/graphviz/gvedit
#%%endif

%exclude %{_libdir}/graphviz/*/*
%exclude %{_libdir}/graphviz/libgvplugin_gd.*
#%%if #%%{DEVIL}
#%%exclude #%%{_libdir}/graphviz/libgvplugin_devil.*
#%%endif
#%%if #%%{MING}
#%%exclude #%%{_libdir}/graphviz/libgvplugin_ming.*
#%%exclude #%%{_libdir}/graphviz/*fdb
#%%endif

%files devel
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/graphviz/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.gz

#%%files doc
#%%doc #%%{_docdir}/#%%{name}/html
#%%doc #%%{_docdir}/#%%{name}/pdf
#%%doc #%%{_docdir}/#%%{name}/demo

%files gd
%{_libdir}/graphviz/libgvplugin_gd.so.*

%files graphs
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/graphs

#%%files guile
#%%{_libdir}/graphviz/guile/
#%%{_mandir}/man3/gv.3guile*

%files lua
%{_libdir}/graphviz/lua/
%{_libdir}/lua*/*
%{_mandir}/man3/gv.3lua*

%files perl
%{_libdir}/graphviz/perl/
%{_libdir}/perl*/*
%{_mandir}/man3/gv.3perl*

#%%if #%%{PHP}
#%%files php
#%%config(noreplace) #%%{_sysconfdir}/php.d/#%%{ini_name}
#%%{_libdir}/graphviz/php/
#%%{php_extdir}/gv.so
#%%{_datadir}/php*/*
#%%{_mandir}/man3/gv.3php*3%%endif

%if %{with python2}
%files python2
%{python2_sitearch}/*
#%%{_mandir}/man3/gv.3python*
%endif

%files python3
#%%{python3_sitearch}/*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py
%{_mandir}/man3/gv.3python*

#%%if #%%{ARRRR}
#%%files R
#%%{_libdir}/graphviz/R/
#%%{_mandir}/man3/gv.3r.gz
#%%endif

#%%files ruby
#%%{_libdir}/graphviz/ruby/
#%%{_libdir}/*ruby*/*
#%%{_mandir}/man3/gv.3ruby*

#%%if #%%{SHARP}
#%%files sharp
#%%{_libdir}/graphviz/sharp/
#%%{_mandir}/man3/gv.3sharp*
#%%endif

%files tcl
%{_libdir}/graphviz/tcl/
%{_libdir}/tcl*/*
# hack to include gv.3tcl only if available
#  always includes tcldot.3tcl, gdtclft.3tcl
%{_mandir}/man3/*.3tcl*

%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.40.1-56
- Rebuild for jpegturbo

* Sun Sep 27 2020 Daniel Hams <daniel.hams@gmail.com> - 2.40.1-55
- Tweak to include tcl + lua bits + man pages

* Sat Jul 04 2020  HAL <notes2@gmx.de> - 2.40.1-54
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.40.1-54
- OCaml 4.08.1 (rc2) rebuild.

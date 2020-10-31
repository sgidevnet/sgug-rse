# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary:       Library of functions for manipulating TIFF format image files
Name:          libtiff
Version:       4.0.9
Release:       7%{?dist}
License:       libtiff
URL:           http://www.simplesystems.org/libtiff/

Source:        ftp://ftp.simplesystems.org/pub/libtiff/tiff-%{version}.tar.gz

Patch0:        libtiff-am-version.patch
Patch1:        libtiff-make-check.patch
Patch2:        libtiff-CVE-2019-6128.patch
Patch3:        libtiff-CVE-2018-12900_CVE-2019-7663.patch
Patch4:        libtiff-CVE-2018-19210.patch

Patch10:       libtiff.fastinstalltest.patch

BuildRequires: gcc, gcc-c++
#BuildRequires: zlib-devel libjpeg-devel jbigkit-devel
BuildRequires: zlib-devel libjpeg-devel
BuildRequires: libtool automake autoconf pkgconfig

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary:       Development tools for programs which will use the libtiff library
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig%{?_isa}

%description devel
This package contains the header files and documentation necessary for
developing programs which will manipulate TIFF format image files
using the libtiff library.

If you need to develop programs which will manipulate TIFF format
image files, you should install this package.  You'll also need to
install the libtiff package.

# Here's a terminator

%package static
Summary:     Static TIFF image format file library
Requires:    %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The libtiff-static package contains the statically linkable version of libtiff.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%package tools
Summary:    Command-line utility programs for manipulating TIFF files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line programs for manipulating TIFF format
image files using the libtiff library.

%prep
%setup -q -n tiff-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch10 -p1

# Use build system's libtool.m4, not the one in the package.
rm -f libtool.m4

libtoolize --force  --copy
aclocal -I . -I m4
automake --add-missing --copy
autoconf
autoheader

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --enable-ld-version-script
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# remove what we didn't want installed
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1
rm -f html/man/tiffgt.1.html
rm -f html/man/sgi2tiff.1.html
rm -f html/man/tiffsv.1.html

# multilib header hack
# we only apply this to known Red Hat multilib arches, per bug #233091
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv $RPM_BUILD_ROOT%{_includedir}/tiffconf.h \
     $RPM_BUILD_ROOT%{_includedir}/tiffconf-$wordsize.h

  cat >$RPM_BUILD_ROOT%{_includedir}/tiffconf.h <<EOF
#ifndef TIFFCONF_H_MULTILIB
#define TIFFCONF_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "tiffconf-32.h"
#elif __WORDSIZE == 64
# include "tiffconf-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

#%ldconfig_scriptlets

%check
LD_LIBRARYN32_PATH=$PWD:$LD_LIBRARYN32_PATH make check

# don't include documentation Makefiles, they are a multilib hazard
find html -name 'Makefile*' | xargs rm

%files
%license COPYRIGHT
#doc README.md RELEASE-DATE VERSION
%doc RELEASE-DATE VERSION
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*

%files devel
%doc TODO ChangeLog html
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%{_libdir}/pkgconfig/libtiff*.pc
%{_mandir}/man3/*

%files static
%{_libdir}/*.a

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Oct 26 2020 Daniel Hams <daniel.hams@gmail.com> - 4.0.9-7
- Rebuild for libjpegturbo switch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Nikola Forró <nforro@redhat.com> - 4.0.10-5
- Fix CVE-2018-19210 (#1649387)

* Fri Feb 15 2019 Nikola Forró <nforro@redhat.com> - 4.0.10-4
- Fix CVE-2019-7663 (#1677529)

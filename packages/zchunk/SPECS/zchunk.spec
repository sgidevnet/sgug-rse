Name:           zchunk
Version:        1.1.5
Release:        1%{?dist}
Summary:        Compressed file format that allows easy deltas
License:        BSD and MIT
URL:            https://github.com/zchunk/zchunk
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Provides:       bundled(buzhash-urlblock) = 0.1

Patch100:       zchunk.sgifixes.patch

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package libs
Summary: Zchunk library

%description libs
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the zchunk library, libzck.

%package devel
Summary: Headers for building against zchunk
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the headers necessary for building against the zchunk
library, libzck.

%prep
%setup -q

%patch100 -p1

# A place to generate the sgug patch
#exit 1

# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%build
# We need the endian.h from libdicl
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="-ldicl-0.1 -lgen $RPM_LD_FLAGS"
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
%meson -Dwith-openssl=enabled -Dwith-zstd=enabled
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_libexecdir}
install contrib/gen_xml_dictionary %{buildroot}%{_libexecdir}/zck_gen_xml_dictionary

%check
export LD_LIBRARYN32_PATH=`pwd`/mips-sgug-irix/src/lib:$LD_LIBRARYN32_PATH
%meson_test

#%%ldconfig_scriptlets libs

%files
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_libexecdir}/zck_gen_xml_dictionary

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libzck.so.*

%files devel
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

%changelog
* Mon Jul 27 2020 Daniel Hams <daniel.hams@gmail.com> - 1.1.5-1
- First pull into sgug

* Sat Jan 18 2020 Jonathan Dieter <jdieter@gmail.com> - 1.1.5-1
- Fix small bug in corner case when handling write failures

* Wed Nov 13 2019 Jonathan Dieter <jdieter@gmail.com> - 1.1.4-1
- Fix download failure when web server doesn''t include content-type with each
  range

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Jonathan Dieter <jdieter@gmail.com> - 1.1.2-2
- Fix multipart range handling to work with quotes, fixes #1706627
- Fix file creation permissions so they respect umask
- Actually push new sources

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.1-3
- Rebuild with Meson fix for #1699099

Name:           gf2x
Version:        1.2
Release:        6%{?dist}
Summary:        Polynomial multiplication over the binary field

License:        GPLv2+
URL:            http://gf2x.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/file/36934/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

%description
Gf2x is a C/C++ software package containing routines for fast arithmetic
in GF(2)[x] (multiplication, squaring, GCD) and searching for
irreducible/primitive trinomials.

%package devel
Summary:        Headers and library files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and library files for developing applications that use %{name}.

%prep
%setup -q

# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  touch -r $badfile.orig $badfile
  rm -f $badfile.orig
done

# Workaround broken configure macros
sed -e "s/GF2X_PCLMUL_AVAILABLE_TRUE=$/&'#'/" \
    -e "/GF2X_PCLMUL_AVAILABLE_FALSE/s/'#'//" \
    -i configure

%build
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Build the SSE2 version for x86, the native version for all other arches.
# Support for pclmul would be nice, but not all x86s support it.
%ifarch %{ix86} x86_64
%configure --disable-static --disable-hardware-specific-code --enable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul
# Workaround broken configure macros
sed -i.orig 's,/\* #undef \(GF2X_HAVE_SSE2_SUPPORT\) \*/,#define \1 1,' \
    gf2x/gf2x-config.h gf2x/gf2x-config-export.h
fixtimestamp gf2x/gf2x-config.h
fixtimestamp gf2x/gf2x-config-export.h
%else
# Workaround broken configure macros
sed -e "s/GF2X_SSE2_AVAILABLE_TRUE=$/&'#'/" \
    -e "/GF2X_SSE2_AVAILABLE_FALSE/s/'#'//" \
    -i configure
%configure --disable-static --disable-hardware-specific-code --disable-sse2 \
  --disable-sse3 --disable-ssse3 --disable-sse41 --disable-pclmul
%endif

# Eliminate hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool
make %{?_smp_mflags} --eval='.SECONDARY:'

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS README TODO
%license COPYING
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.1.*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 1.2-4
- Drop SSE2 build for 32-bit x86, now default

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 1.2-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Jerry James <loganjerry@gmail.com> - 1.1-6
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 1.1-1
- New upstream release

* Fri May  4 2012 Jerry James <loganjerry@gmail.com> - 1.0-1
- Initial RPM

# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

# Recent so-version, so we do not bump accidentally.
%global nettle_so_ver 6
%global hogweed_so_ver 4

# Set to 1 when building a bootstrap for a bumped so-name.
%global bootstrap 1

%if 0%{?bootstrap}
%global version_old 3.4.1rc1
%global nettle_so_ver_old 6
%global hogweed_so_ver_old 4
%endif

%bcond_with fips

Name:           nettle
Version:        3.4
Release:        4%{?dist}
Summary:        A low-level cryptographic library

License:        LGPLv3+ or GPLv2+
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:	%{name}-%{version}.tar.gz
#Source0:        http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
#if 0%{?bootstrap}
#Source1:	%{name}-%{version_old}-hobbled.tar.xz
#Source2:	nettle-3.3-remove-ecc-testsuite.patch
#endif
#Patch0:		nettle-3.5-remove-ecc-testsuite.patch
#Patch1:		nettle-3.4-annocheck.patch

Patch10:        nettle.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel, m4
BuildRequires:	libtool, automake, autoconf, gettext-devel
%if %{with fips}
BuildRequires:  fipscheck
%endif

%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.


%prep
%autosetup -Tb 0 -p1

#if 0%{?bootstrap}
#mkdir -p bootstrap_ver
#cd bootstrap_ver
#tar --strip-components=1 -xf %{SOURCE1}
#patch -p1 < %{SOURCE2}
#
## Disable -ggdb3 which makes debugedit unhappy
#sed s/ggdb3/g/ -i configure
#sed 's/ecc-192.c//g' -i Makefile.in
#sed 's/ecc-224.c//g' -i Makefile.in
#cd ..
#endif

## Disable -ggdb3 which makes debugedit unhappy
#sed s/ggdb3/g/ -i configure
#sed 's/ecc-192.c//g' -i Makefile.in
#sed 's/ecc-224.c//g' -i Makefile.in

%build
autoreconf -ifv
%configure --enable-shared --enable-fat
make %{?_smp_mflags}

#if 0%{?bootstrap}
#cd bootstrap_ver
#autoconf
#configure --with-tests
#make_build
#cd ..
#endif

%if %{with fips}
%define fipshmac() \
	fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%1.* \
	file=`basename $RPM_BUILD_ROOT%{_libdir}/%1.*.hmac` && \
	mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
	ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.%1.hmac

#if 0%{?bootstrap}
#define bootstrap_fips 1
#endif

%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	%fipshmac libnettle.so.%{nettle_so_ver} \
	%fipshmac libhogweed.so.%{hogweed_so_ver} \
	%{?bootstrap_fips:%fipshmac libnettle.so.%{nettle_so_ver_old}} \
	%{?bootstrap_fips:%fipshmac libhogweed.so.%{hogweed_so_ver_old}} \
%{nil}
%endif


%install
#if 0%{?bootstrap}
#make -C bootstrap_ver install-shared-nettle DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
#make -C bootstrap_ver install-shared-hogweed DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
#
#chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver_old}.*
#chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}.*
#endif

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -p -m 644 nettle.info $RPM_BUILD_ROOT%{_infodir}/
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2

chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*

%check
make check

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_infodir}/nettle.info.*
%{_libdir}/libnettle.so.%{nettle_so_ver}
%{_libdir}/libnettle.so.%{nettle_so_ver}.*
%{_libdir}/libhogweed.so.%{hogweed_so_ver}
%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*
#if 0%{?bootstrap}
#%{_libdir}/libnettle.so.%{nettle_so_ver_old}
#%{_libdir}/libnettle.so.%{nettle_so_ver_old}.*
#%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}
#%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}.*
#endif
%if %{with fips}
%{_libdir}/.libhogweed.so.*.hmac
%{_libdir}/.libnettle.so.*.hmac
%endif

%files devel
%doc descore.README nettle.html nettle.pdf
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

#%ldconfig_scriptlets


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Daiki Ueno <dueno@redhat.com> - 3.5.1-2
- Rebuild with bootstrap enabled

* Mon Jul 15 2019 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.5.1-1
- New upstream release

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 3.4.1rc1-3
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.4.1rc1-1
- New upstream release; provides API for constant memory access RSA operations

* Tue Oct 16 2018 Tomáš Mráz <tmraz@redhat.com> - 3.4-7
- Generate the .hmac checksums unless --without fips is used

* Tue Oct 16 2018 Tomáš Mráz <tmraz@redhat.com> - 3.4-6
- Cover the gaps in annotation coverage for assembler sources

* Fri Aug 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.4-5
- update libary versions used for fips

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4-4
- Replace obsolete scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.4-1
- New upstream release

* Wed Aug 09 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.3-5
- Removed executables from the library to allow parallel installation
  of x86-64 and x86 packages. The executables had testing purpose, and
  may be re-introduced in a separate package if needed.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.3-1
- New upstream release
- Allow arm neon instructions (they are enabled via fat builds)

* Tue Jul 19 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.2-3
- Backported a fix for more cache silence on RSA and DSA.

* Thu Feb 18 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.2-2
- Enabled fat builds by default

* Wed Feb  3 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.2-1
- updated to 3.2 (#1301310)
- Fixed CVE-2015-8803 secp256r1 calculation bug (#1304305)

* Wed Dec  9 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.1.1-6
- Made version.h architecture independent (#1289938)

* Wed Dec  2 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.1.1-5
- Disabled arm-neon unconditionally (#1287298)

* Thu Oct 22 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.1.1-4
- Fixed SHA3 implementation to conform to published version (#1252935)

* Sun Aug  2 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.1-3
- No need to ship license in devel too
- Drop ChangeLog as details are in NEWS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 3.1.1-1
- Updated to nettle 3.1.1

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.7.1-6
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 2.7.1-3
- Corrected bug number in previous comment.

* Fri Dec 13 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 2.7.1-2
- Added patch nettle-tmpalloc.patch to solve #1051455

* Mon Nov 25 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 2.7.1-1
- Updated to nettle 2.7.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb  6 2013 Tomáš Mráz <tmraz@redhat.com> - 2.6-2
- nettle includes use gmp.h

* Tue Feb  5 2013 Tomáš Mráz <tmraz@redhat.com> - 2.6-1
- New upstream release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 David Woodhouse <dwmw2@infradead.org> - 2.4-3
- Remove explicit buildroot handling and defattr.

* Wed Jul 04 2012 David Woodhouse <dwmw2@infradead.org> - 2.4-2
- Review feedback

* Mon Jun 18 2012 David Woodhouse <dwmw2@infradead.org> - 2.4-1
- Revive package (GnuTLS needs it), disable static, update to current release 2.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 10 2008 Ian Weller <ianweller@gmail.com> 1.15-5
- Moved static lib to -static

* Mon Mar 24 2008 Ian Weller <ianweller@gmail.com> 1.15-4
- Added libraries and ldconfig

* Mon Feb 18 2008 Ian Weller <ianweller@gmail.com> 1.15-3
- Added provides -static to -devel

* Sun Feb 17 2008 Ian Weller <ianweller@gmail.com> 1.15-2
- Removed redundant requires
- Removed redundant documentation between packages
- Fixed license tag
- Fixed -devel description
- Added the static library back to -devel
- Added make clean

* Fri Feb 08 2008 Ian Weller <ianweller@gmail.com> 1.15-1
- First package build.

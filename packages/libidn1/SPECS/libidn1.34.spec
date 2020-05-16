Summary: Internationalized Domain Name support library
Name: libidn1.34
Version: 1.34
Release: 3%{?dist}
URL: http://www.gnu.org/software/libidn/
License: LGPLv2+ and GPLv3+ and GFDL
Source0: http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
# Allow disabling Emacs support
Patch0: libidn-1.33-Allow-disabling-Emacs-support.patch
# Fix ABI compatibility with libidn-1.33 and earlier
Patch1: libidn-tablesize-revert.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: gettext gettext-devel
BuildRequires: pkgconfig
# gnulib is a copylib, bundling is allowed
Provides: bundled(gnulib)

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%prep
%setup -q -n libidn-%{version}
%patch0 -p1
%patch1 -p1 -b .tablesize-revert
autoreconf -vif
# Prevent from regenerating sources by gengetopt because it's broken.
touch src/idn_cmd.c src/idn_cmd.h

# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

%build
%configure --disable-csharp --disable-static \
    --disable-doc \
    --disable-emacs \
    --disable-java

# remove RPATH hardcoding
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%check
# without RPATH this needs to be set to test the compiled library
export LD_LIBRARY_PATH=$(pwd)/lib/.libs
make %{?_smp_mflags} -C tests check VALGRIND=env

%install
make install DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_libdir}/pkgconfig \
    ;

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la \
      $RPM_BUILD_ROOT%{_libdir}/libidn.so \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libidn.pc \
      $RPM_BUILD_ROOT%{_bindir}/idn \
      $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/libidn.mo \
      $RPM_BUILD_ROOT%{_includedir}/*.h \

#%%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS NEWS FAQ README THANKS
%{_libdir}/libidn.so.11*

%changelog
* Wed May 13 2020  Alexander Tafarte <notes2@gmx.de> -1.34.4 
- compiles on Irix 6.5 with sgug-rse gcc 9.2 , 84/87 tests pass (1 skipped).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.34-1
- compat library for F29+

%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

# This package is able to use optimised linker flags.
%if !(0%{debug})
%global build_ldflags %{sgug_optimised_ldflags}
%endif

%bcond_with bootstrap

%global multilib_arches %{ix86} ppc ppc64 ppc64p7 s390 s390x x86_64

Name:		libffi
Version:	3.2.1
Release:	25%{?dist}
Summary:	A portable foreign function interface library
License:	MIT
URL:		http://sourceware.org/libffi

Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
Source1:	ffi-multilib.h
Source2:	ffitarget-multilib.h
Patch0:		libffi-3.1-fix-include-path.patch
#Patch1:		libffi-3.1-fix-exec-stack.patch
Patch2:		libffi-aarch64-rhbz1174037.patch
Patch3:		libffi-3.1-aarch64-fix-exec-stack.patch

Patch100:        libffi.sgifixes.patch

BuildRequires: gcc
%if %{without bootstrap}
BuildRequires: gcc-c++
BuildRequires: dejagnu
%endif

%description
Compilers for high level languages generate code that follow certain
conventions.  These conventions are necessary, in part, for separate
compilation to work.  One such convention is the "calling convention".
The calling convention is a set of assumptions made by the compiler
about where function arguments will be found on entry to a function.  A
calling convention also specifies where the return value for a function
is found.  

Some programs may not know at the time of compilation what arguments
are to be passed to a function.  For instance, an interpreter may be
told at run-time about the number and types of arguments used to call a
given function.  'Libffi' can be used in such programs to provide a
bridge from the interpreter program to compiled code.

The 'libffi' library provides a portable, high level programming
interface to various calling conventions.  This allows a programmer to
call any function specified by a call interface description at run time.

FFI stands for Foreign Function Interface.  A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language.  The
'libffi' library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface.  A layer must
exist above 'libffi' that handles type conversions for values passed
between the two languages.  


%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .fixpath
#%patch1 -p1 -b .execstack
%patch2 -p1 -b .aarch64
%patch3 -p1 -b .aarch64execstack

%patch100 -p1 -b .sgifixes

#exit 1

%build
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif
%configure --disable-static
make %{?_smp_mflags}

%check
%if %{without bootstrap}
%make_build check
%endif

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Determine generic arch target name for multilib wrapper
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif

mkdir -p $RPM_BUILD_ROOT%{_includedir}
%ifarch %{multilib_arches}
# Do header file switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, and they each need
# their own correct-but-different versions of the headers to be usable.
for i in ffi ffitarget; do
  mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/$i.h $RPM_BUILD_ROOT%{_includedir}/$i-${basearch}.h
done
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/ffi.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/ffitarget.h
%else
mv $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}/include/{ffi,ffitarget}.h $RPM_BUILD_ROOT%{_includedir}
%endif
rm -rf $RPM_BUILD_ROOT%{_libdir}/libffi-%{version}


#%ldconfig_scriptlets

%files
%license LICENSE
%doc README
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ffi*.h
%{_libdir}/*.so
%{_mandir}/man3/*.gz
%{_infodir}/libffi.info.*

%changelog
* Sat Nov 14 2020 Daniel Hams <daniel.hams@gmail.com> - 3.2.1-25
- Bug fix when returning pointers/32bit values directly

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 3.2.1-24
- Remove hard coded shell paths

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Florian Weimer <fweimer@redhat.com> - 3.1-22
- Run test suite during build (#1727088)

* Wed Jun 19 2019 Anthony Green <green@redhat.com> - 3.1-21
- Fix license tag

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 3.1-20
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 3.1-28
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-15
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul  5 2017 Jens Petersen <petersen@redhat.com> - 3.1-12
- protect install-info in the rpm scriptlets
  https://fedoraproject.org/wiki/Packaging:Scriptlets#Texinfo

* Tue Jun 20 2017 Anthony Green <green@redhat.com> - 3.1-11
- fix exec stack problem on aarch64 build

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.1-7
- Add patch to fix issues on aarch64 (rhbz 1174037)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Tom Callaway <spot@fedoraproject.org> - 3.1-5
- fix license handling

* Sun Jun 29 2014 Anthony Green <green@redhat.com> - 3.1-4
- fix exec stack problem on 32-bit build

* Thu Jun 12 2014 Dan Horák <dan[at]danny.cz> - 3.1-3
- fix header path in pkgconfig file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Anthony Green <green@redhat.com> - 3.1-1
- fix non-multiarch builds (arm).

* Mon May 19 2014 Anthony Green <green@redhat.com> - 3.1-0
- update to 3.1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Tom Callaway <spot@fedoraproject.org> - 3.0.13-4
- fix typos in wrapper headers

* Mon May 27 2013 Tom Callaway <spot@fedoraproject.org> - 3.0.13-3
- make header files multilib safe

* Sat May 25 2013 Tom Callaway <spot@fedoraproject.org> - 3.0.13-2
- fix incorrect header pathing (and .pc file)

* Wed Mar 20 2013 Anthony Green <green@redhat.com> - 3.0.13-1
- update to 3.0.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Dennis Gilmore <dennis@ausil.us> - 3.0.11-1
- update to 3.0.11

* Fri Nov 02 2012 Deepak Bhole <dbhole@redhat.com> - 3.0.10-4
- Fixed source location

* Fri Aug 10 2012 Dennis Gilmore <dennis@ausil.us> - 3.0.10-3
- drop back to 3.0.10, 3.0.11 was never pushed anywhere as the soname bump broke buildroots
- as 3.0.11 never went out no epoch needed.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Anthony Green <green@redhat.com> - 3.0.11-1
- Upgrade to 3.0.11.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Anthony Green <green@redhat.com> - 3.0.10-1
- Upgrade to 3.0.10. 

* Fri Mar 18 2011 Dan Horák <dan[at]danny.cz> - 3.0.9-3
- added patch for being careful when defining relatively generic symbols

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 29 2009 Anthony Green <green@redhat.com> - 3.0.9-1
- Upgrade

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 08 2008 Anthony Green <green@redhat.com> 3.0.5-1
- Upgrade to 3.0.5

* Fri Feb 15 2008 Anthony Green <green@redhat.com> 3.0.1-1
- Upgrade to 3.0.1

* Fri Feb 15 2008 Anthony Green <green@redhat.com> 2.99.9-1
- Upgrade to 2.99.9
- Require pkgconfig for the devel package.
- Update summary.

* Fri Feb 15 2008 Anthony Green <green@redhat.com> 2.99.8-1
- Upgrade to 2.99.8

* Thu Feb 14 2008 Anthony Green <green@redhat.com> 2.99.7-1
- Upgrade to 2.99.7

* Thu Feb 14 2008 Anthony Green <green@redhat.com> 2.99.6-1
- Upgrade to 2.99.6

* Thu Feb 14 2008 Anthony Green <green@redhat.com> 2.99.4-1
- Upgrade to 2.99.4

* Thu Feb 14 2008 Anthony Green <green@redhat.com> 2.99.3-1
- Upgrade to 2.99.3

* Thu Feb 14 2008 Anthony Green <green@redhat.com> 2.99.2-1
- Created.

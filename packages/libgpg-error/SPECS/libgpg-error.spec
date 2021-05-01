Name: libgpg-error
Version: 1.36
Release: 2%{?dist}
Summary: Library for error values used by GnuPG components
URL: https://www.gnupg.org/related_software/libgpg-error/
License: LGPLv2+

Source0: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
Patch1: libgpg-error-1.29-multilib.patch
Patch2: libgpg-error-1.36-gawk.patch

BuildRequires: gcc
BuildRequires: gawk, gettext, autoconf, automake, gettext-devel, libtool
BuildRequires: texinfo
BuildRequires: gettext-autopoint

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep
export SHELL="%{_bindir}/bash"
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
%setup -q
%patch1 -p1 -b .multilib
%patch2 -p1 -b .gawk

perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" autogen.sh
# The gpgrt-config script is _really_ slow with anything other than
# bash - and it's still quite slow with that, too.
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" src/gpgrt-config
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" src/gpg-error-config.in
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" src/gpg-error-config-test.sh

autoreconf -f

# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g;s|@GPG_ERROR_CONFIG_HOST@|none|g' src/gpg-error-config.in

# Modify configure to drop rpath for /usr/lib64
#sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure

%build
export SHELL="%{_bindir}/bash"
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
#%%configure --disable-static --disable-rpath --disable-languages
%configure --disable-static --disable-languages
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%find_lang %{name}

%check
make check

#%%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README NEWS
%{_bindir}/gpg-error
%{_libdir}/libgpg-error.so.0*
%{_datadir}/libgpg-error

%files devel
%{_bindir}/gpg-error-config
%{_bindir}/gpgrt-config
%{_bindir}/yat2m
%{_libdir}/libgpg-error.so
%{_libdir}/pkgconfig/gpg-error.pc
%{_includedir}/gpg-error.h
%{_includedir}/gpgrt.h
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/aclocal/gpgrt.m4
%{_infodir}/gpgrt.info*
%{_mandir}/man1/gpgrt-config.*

%changelog
* Wed Aug 14 2019 Tomáš Mráz <tmraz@redhat.com> 1.36-2
- fix FTBFS in rawhide due to new gawk

* Sat Aug  3 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.36-1
- new upstream release 1.36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Tomáš Mráz <tmraz@redhat.com> 1.33-1
- new upstream release 1.33
- dropped obsolete install-info scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Tomáš Mráz <tmraz@redhat.com> 1.31-1
- new upstream release 1.31

* Wed Apr 11 2018 Tomáš Mráz <tmraz@redhat.com> 1.29-1
- new upstream release 1.29

* Wed Feb 28 2018 Richard W.M. Jones <rjones@redhat.com> - 1.27-6
- Backport patch which adds riscv64 support.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.27-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Tomáš Mráz <tmraz@redhat.com> 1.27-1
- new upstream release 1.27

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Tomáš Mráz <tmraz@redhat.com> 1.25-1
- new upstream release 1.25

* Thu Jul 14 2016 Tomáš Mráz <tmraz@redhat.com> 1.24-1
- new upstream release

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.21-3
- drop explicit /sbin/ldconfig scriptlet deps (#1319144)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Tomáš Mráz <tmraz@redhat.com> 1.21-1
- new upstream release

* Tue Sep  1 2015 Tomáš Mráz <tmraz@redhat.com> 1.20-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Tomáš Mráz <tmraz@redhat.com> 1.19-1
- new upstream release

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.17-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Jan 30 2015 Tomáš Mráz <tmraz@redhat.com> 1.17-2
- do not conflict on header file between architectures (#1180857)

* Thu Jan 29 2015 Tomáš Mráz <tmraz@redhat.com> 1.17-1
- new upstream release

* Fri Sep 19 2014 Tomáš Mráz <tmraz@redhat.com> 1.16-1
- new upstream release
- move from /lib to /usr/lib

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> 1.13-2
- fix license handling

* Wed Jun 25 2014 Tomáš Mráz <tmraz@redhat.com> 1.13-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Tomáš Mráz <tmraz@redhat.com> 1.12-1
- new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr  5 2013 Tomáš Mráz <tmraz@redhat.com> 1.11-1
- new upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Tomáš Mráz <tmraz@redhat.com> 1.10-1
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Rex Dieter <rdieter@fedoraproject.org> 1.9-1
- libgpg-error-1.9

* Thu Feb 25 2010 Nalin Dahyabhai <nalin@redhat.com> - 1.7-3
- turn off common lisp bindings the right way
- drop finger output
- recode the changelog into UTF-8 if it isn't UTF-8 (rpmlint)

* Mon Jan 11 2010 Nalin Dahyabhai <nalin@redhat.com> - 1.7-2
- fix use of macro in changelog (rpmlint)
- build with --disable-rpath (rpmlint)
- build with %%{?_smp_mflags}

* Thu Oct 15 2009 Nalin Dahyabhai <nalin@redhat.com> - 1.7-1
- long-overdue update to 1.7
- add a disttag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6-2
- Autorebuild for GCC 4.3

* Fri Dec  7 2007 Nalin Dahyabhai <nalin@redhat.com>
- remove the generic install docs (#226021)

* Fri Dec  7 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.6-1
- update to 1.6
- add suggested summary, buildrequires, and modify install call as suggested
  by package review (#226021)

* Mon Oct 15 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-6
- use ldconfig to make the soname symlink so that it gets packaged (#331241)

* Wed Aug 22 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-5
- add missing gawk buildrequirement

* Thu Aug 16 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-4
- clarify license

* Mon Jul 30 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-3
- disable static libraries (part of #249815)

* Fri Jul 27 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-2
- move libgpg-error shared library to /%%{_lib} (#249816)

* Thu Jul 19 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.5-1
- update to 1.5

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.4-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Bill Nottngham <notting@redhat.com> - 1.4-1
- update to 1.4
- don't ship lisp bindings

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.3-3.1
- rebuild

* Mon Jun  5 2006 Nalin Dahyabhai <nalin@redhat.com> 1.3-3
- give gpg-error-config libdir=@exec_prefix@/lib instead of @libdir@, so that
  it agrees on 32- and 64-bit arches (it suppresses the -L argument if @libdir@
  is /usr/lib, so this should be cleaner than adding a non-standard .pc file
  which upstream developers might inadvertently think they can depend to be on
  every system which provides this library)

* Mon May 15 2006 Karsten Hopp <karsten@redhat.de> 1.3-2
- switch to pkgconfig so that gpg-error-config can be the same on 
  32bit and 64bit archs

* Tue May  2 2006 Nalin Dahyabhai <nalin@redhat.com> - 1.3-1
- update to version 1.3

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Karsten Hopp <karsten@redhat.de> 1.1-1
- update

* Wed Mar  2 2005 Bill Nottingham <notting@redhat.com> - 1.0-2
- we can rebuild it. we have the technology.

* Tue Aug 31 2004 Bill Nottingham <notting@redhat.com> - 1.0-1
- update to 1.0

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 16 2004 Bill Nottingham <notting@redhat.com> - 0.7-1
- adapt upstream specfile

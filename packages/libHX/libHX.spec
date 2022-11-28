Name:           libHX
Version:        3.22
Release:        11%{?dist}
Summary:        Useful collection of routines for C and C++ programming

License:        LGPLv2 or LGPLv3
URL:            http://sourceforge.net/projects/libhx/
Source0:        http://downloads.sourceforge.net/libhx/libHX-%{version}.tar.xz
Source1:        http://downloads.sourceforge.net/libhx/libHX-%{version}.tar.asc
Source2:        gpgkey-B56B8B9D9915AA8796EDC013DFFF2CDB19FC338D.gpg

BuildRequires:  perl-interpreter gcc-c++
# For source verification with gpgv
BuildRequires:  gpg xz


%description
libHX is a C library (with some C++ bindings available) that provides data
structures and functions commonly needed, such as maps, deques, linked lists,
string formatting and autoresizing, option and config file parsing, type
checking casts and more.

libHX aids in quickly writing up C and C++ data processing programs, by
consolidating tasks that often happen to be open-coded, such as (simple) config
file reading, option parsing, directory traversal, and others, into a library.
The focus is on reducing the amount of time (and secondarily, the amount of
code) a developer has to spend for otherwise implementing such.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
xzcat %{SOURCE0} | gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} -
%setup -q


%build
# Without --docdir=.. package installs docs into ../libhx
%configure --disable-static --disable-silent-rules  \
  --with-pkgconfigdir=%{_libdir}/pkgconfig \
  --docdir=%{_pkgdocdir}
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Install additional docs
install -m 644 README.txt \
  doc/api.txt \
  doc/assorted.txt \
  doc/changelog.txt \
  doc/ux-*.txt \
  $RPM_BUILD_ROOT%{_pkgdocdir}


%ldconfig_scriptlets


%files
%license LICENSE.LGPL2 LICENSE.LGPL3 LICENSE.GPL3
%{_libdir}/libHX_rtcheck.so
%{_libdir}/libHX.so.28
%{_libdir}/libHX.so.28.3.0


%files devel
%{_pkgdocdir}

%dir %{_includedir}/libHX
%{_includedir}/libHX.h
%{_includedir}/libHX/ctype_helper.h
%{_includedir}/libHX/defs.h
%{_includedir}/libHX/deque.h
%{_includedir}/libHX/init.h
%{_includedir}/libHX/io.h
%{_includedir}/libHX/libxml_helper.h
%{_includedir}/libHX/list.h
%{_includedir}/libHX/map.h
%{_includedir}/libHX/misc.h
%{_includedir}/libHX/option.h
%{_includedir}/libHX/proc.h
%{_includedir}/libHX/string.h
%{_includedir}/libHX/wx_helper.hpp
%{_libdir}/libHX.so
%{_libdir}/pkgconfig/libHX.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.22-4
- Rework doc installation (F24FTBFS, RHBZ#1307712).
- Modernize spec.
- Add %%license.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Till Maas <opensource@till.name> - 3.22-1
- Update to latest release
- Add source code verification
- Harden build

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Till Maas <opensource@till.name> - 3.18-1
- Update to new release

* Mon Oct 07 2013 Till Maas <opensource@till.name> - 3.16-1
- Update to new release

* Mon Aug 05 2013 Till Maas <opensource@till.name> - 3.15-3
- Use %%{_pkgdocdir}

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Till Maas <opensource@till.name> - 3.15-1
- Update to new release
- Move library to /usr, since /lib etc are symlinks to their /usr counterparts

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Till Maas <opensource@till.name> - 3.14.1-1
- Update to new release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Till Maas <opensource@till.name> - 3.12.1-1
- Update to new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Till Maas <opensource@till.name> - 3.6-3
- Add %%{?_isa}

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Till Maas <opensource@till.name> - 3.6-1
- really update to latest release

* Mon Aug 16 2010 Till Maas <opensource@till.name> - 3.5-1
- Update to latest release
- remove devel %%files %%{_includedir} globbing
- Update soname

* Sat Aug 07 2010 Till Maas <opensource@till.name> - 3.4-2
- Use less globbing in %%files to detect changes

* Sun May 16 2010 Till Maas <opensource@till.name> - 3.4-1
- Update to new release

* Thu Sep 24 2009 Till Maas <opensource@till.name> - 3.1-1
- Update to new release

* Thu Aug 27 2009 Till Maas <opensource@till.name> - 3.0-1
- Update to new release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Till Maas <opensource@till.name> - 2.8-1
- Update to new release
- Define docdir for %%configure, because of installed PDF documentation

* Tue Mar 03 2009 Till Maas <opensource@till.name> - 2.5-1
- Update to new release
- Update URL/Source0 to SF.net webpage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Till Maas <opensource@till.name> - 2.3-1
- Update to new release

* Mon Dec 29 2008 Till Maas <opensource@till.name> - 2.1-1
- Update to new release

* Sat Dec 20 2008 Till Maas <opensource@till.name> - 1.25-3
- Fix .so symlink

* Thu Nov 27 2008 Till Maas <opensource@till.name> - 1.25-2
- Move libHX.so.* to /%%{_lib} because of /sbin/mount.crypt from pam_mount

* Thu Sep 11 2008 Till Maas <opensource@till.name> - 1.25-1
- Update to latest version

* Fri Sep 05 2008 Till Maas <opensource@till.name> - 1.23-1
- Update to latest version

* Wed Jun 11 2008 Till Maas <opensource till name> - 1.18-2
- Set variable V for make: displays full compiler commandline

* Wed Jun 11 2008 Till Maas <opensource till name> - 1.18-1
- Update to latest version

* Tue May 27 2008 Till Maas <opensource till name> - 1.17-1
- Update to latest version

* Mon May 05 2008 Till Maas <opensource till name> - 1.15-1
- Update to latest version
- Update description

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.2-2
- Autorebuild for GCC 4.3

* Wed Dec 26 2007 Till Maas <opensource till name> - 1.10.2-1
- update to latest version
- fixed bug: https://sourceforge.net/tracker/?func=detail&atid=430593&aid=1845721&group_id=41452

* Thu Sep 27 2007 Till Maas <opensource till name> - 1.10.1-2
- add tests as examples to devel documentation

* Wed Sep 26 2007 Till Maas <opensource till name> - 1.10.1-1
- initial spec for Fedora

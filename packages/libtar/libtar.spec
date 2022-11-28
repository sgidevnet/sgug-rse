Summary:        Tar file manipulation API
Name:           libtar
Version:        1.2.20
Release:        18%{?dist}
License:        MIT
URL:            http://repo.or.cz/libtar.git
Source:         http://repo.or.cz/libtar.git/snapshot/refs/tags/v1.2.20.tar.gz#/libtar-v1.2.20.tar.gz
Patch1:         libtar-1.2.11-missing-protos.patch
Patch4:         libtar-1.2.11-mem-deref.patch
Patch5:         libtar-1.2.20-fix-resource-leaks.patch
Patch6:         libtar-1.2.11-bz729009.patch
Patch7:         libtar-1.2.20-no-static-buffer.patch

# fix programming mistakes detected by static analysis
Patch8:         libtar-1.2.20-static-analysis.patch

BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
libtar is a C library for manipulating tar archives. It supports both
the strict POSIX tar format and many of the commonly-used GNU
extensions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n libtar-v%{version} -p1

# set correct version for .so build
%global ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in

autoreconf -iv


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# Without this we get no debuginfo and stripping
chmod +x $RPM_BUILD_ROOT%{_libdir}/libtar.so.%{version}
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%doc COPYRIGHT TODO README ChangeLog*
%{_bindir}/%{name}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libtar.h
%{_includedir}/libtar_listhash.h
%{_libdir}/lib*.so
%{_mandir}/man3/*.3*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Kamil Dudka <kdudka@redhat.com> - 1.2.20-16
- fix programming mistakes detected by static analysis

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Kamil Dudka <kdudka@redhat.com> - 1.2.20-14
- fix source URL and re-download the upstream tarball

* Wed May 30 2018 Kamil Dudka <kdudka@redhat.com> - 1.2.20-13
- drop obsolete Group tags
- replace dead project URL

* Thu Feb 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.20-12
- Switch to %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.2.20-6
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Kamil Dudka <kdudka@redhat.com> - 1.2.20-3
- avoid using a static buffer in th_get_pathname()

* Wed Oct 16 2013 Kamil Dudka <kdudka@redhat.com> - 1.2.20-2
- use the upstream version of resource leak patches

* Thu Oct 10 2013 Kamil Dudka <kdudka@redhat.com> - 1.2.20-1
- update to 1.2.20 (latest upstream release)

* Thu Oct 10 2013 Kamil Dudka <kdudka@redhat.com> - 1.2.11-28
- fix CVE-2013-4397: buffer overflows by expanding a specially-crafted archive

* Fri Oct 04 2013 Kamil Dudka <kdudka@redhat.com> - 1.2.11-27
- fix file descriptor leaks reported by cppcheck (#785760)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Kamil Dudka <kdudka@redhat.com> - 1.2.11-24
- fix specfile issues reported by the fedora-review script

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Kamil Dudka <kdudka@redhat.com> - 1.2.11-21
- Allow to extract debug-info from /usr/bin/libtar (#729009)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 27 2010 Kamil Dudka <kdudka@redhat.com> - 1.2.11-19
- Completed review of memory leaks related patches (#589056)

* Mon May 3 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.11-18
- Fix more memory leaks

* Mon May 3 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.11-17
- Fix lot of memory leaks

* Thu Dec 31 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.11-16
- Fix invalid memory de-reference issue in BZ #551415

* Fri Nov 20 2009 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.2.11-15
- Fix buffer overflow in BZ #538770

* Tue Sep 22 2009 Stepan Kasal <skasal@redhat.com> - 1.2.11-14
- fix up so that it builds again (#511566)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.11-11
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.11-10
- Autorebuild for GCC 4.3

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.11-9
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.11-8
- FE6 Rebuild

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.11-7
- Taking over as maintainer since Anvil has other priorities
- Add a bunch of patches from Debian, which build a .so instead of a .a
  and fix a bunch of memory leaks.
- Reinstate a proper devel package as we now build a .so

* Thu Mar 16 2006 Dams <anvil[AT]livna.org> - 1.2.11-6.fc5
- Modified URL and added one in Source0

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.2.11-5
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Aug 16 2003 Dams <anvil[AT]livna.org> 0:1.2.11-0.fdr.3
- Merged devel and main packages
- Package provide now libtar-devel

* Tue Jul  8 2003 Dams <anvil[AT]livna.org>
- Initial build.

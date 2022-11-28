Name:           npth
Version:        1.6
Release:        3%{?dist}
Summary:        The New GNU Portable Threads library
License:        LGPLv2+
URL:            https://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source:         https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2
#Source1:        ftp://ftp.gnupg.org/gcrypt/npth/npth-%{version}.tar.bz2.sig
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source2:        npth-config.1

BuildRequires:  make
BuildRequires:  gcc

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 %{S:2}
find %{buildroot} -name '*.la' -delete -print

%check
make check

#%%ldconfig_scriptlets

%files
%license COPYING.LIB
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_mandir}/man1/%{name}-config.1*
%{_datadir}/aclocal/%{name}.m4

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6-1
- Update to 1.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5-1
- Update to 1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3-1
- Update to 1.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Christopher Meng <rpm@cicku.me> - 1.2-1
- Update to 1.2

* Sat Nov 15 2014 Christopher Meng <rpm@cicku.me> - 1.1-1
- Update to 1.1

* Sat Sep 20 2014 Christopher Meng <rpm@cicku.me> - 1.0-1
- Update to 1.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar  7 2013 Milan Bartos <mbartos@redhat.com> - 0.91-5
- fixed license tag

* Wed Mar  6 2013 Milan Bartos <mbartos@redhat.com> - 0.91-4
- fixed license tag
- added comment to license and manual page
- removed defattr

* Tue Mar  5 2013 Milan Bartos <mbartos@redhat.com> - 0.91-3
- added npth-config man page

* Tue Mar  5 2013 Milan Bartos <mbartos@redhat.com> - 0.91-2
- fixed license tag
- added COPYING.LESSER to package

* Tue Feb 26 2013 Milan Bartos <mbartos@redhat.com> - 0.91-1
- initial port


%global mainver 5.0
%global datever 20160131

Name:           cdk
Version:        %{mainver}.%{datever}
Release:        9%{?dist}
Summary:        Curses Development Kit
License:        BSD with advertising
URL:            http://invisible-island.net/cdk/
Source0:        ftp://invisible-island.net/cdk-%{mainver}-%{datever}.tgz
BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
CDK stands for "Curses Development Kit". It contains a large number of ready
to use widgets which facilitate the speedy development of full screen curses
programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{mainver}-%{datever}

%build
%configure --with-ncurses --enable-const
make cdkshlib %{?_smp_mflags}

%install
make install installCDKSHLibrary DESTDIR=%{buildroot} INSTALL="install -pD"

# fixes rpmlint unstripped-binary-or-object
chmod +x %{buildroot}%{_libdir}/*.so

find %{buildroot} -name '*.a' -delete -print

rm -vrf %{buildroot}%{_docdir}

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGES EXPANDING INSTALL NOTES README TODO VERSION examples demos
%{_libdir}/libcdk.so.*
%{_mandir}/man3/*.3*

%files devel
%{_bindir}/cdk5-config
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libcdk.so

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 5.0.%{datever}-7
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20160131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 5.0.20160131-1
- Rebuilt for new upstream 5.0.20160131
- Fix FTBFS in rawhide rhbz #1307369 plus spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.20141106-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20141106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Christopher Meng <rpm@cicku.me> - 5.0.20141106-1
- Update to 5.0-20141106

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20140118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20140118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Christopher Meng <rpm@cicku.me> - 5.0.20140118-1
- Update to 5.0-20140118

* Sat Nov 16 2013 Christopher Meng <rpm@cicku.me> - 5.0.20131107-1
- Update to 5.0-20131107

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.20081105-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 4 2009 Marek Mahut <mmahut@fedoraproject.org> - 5.0.20081105-1
- Initial build

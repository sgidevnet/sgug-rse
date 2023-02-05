Name:           enet
Version:        1.3.14
Release:        2%{?dist}
Summary:        Thin, simple and robust network layer on top of UDP

License:        MIT
URL:            http://enet.bespin.org
Source0:        %{url}/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
ENet is a relatively thin, simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking library
that handles authentication, lobbying, server discovery, compression,
encryption and other high level, often application level or dependent tasks.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog README
%{_libdir}/lib%{name}.so.*

%files devel
%doc docs/*.dox
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.14-1
- Update to 1.3.14

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.13-8
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 26 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.3.13-4
- Modernize spec

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Hans de Goede <hdegoede@redhat.com> - 1.3.13-1
- New upstream release 1.3.13 (rhbz#1217661)

* Mon Jan 05 2015 Michal Schmidt <mschmidt@redhat.com> - 1.3.12-4
- Ship pkgconfig file.
- Spec file cleanup and modernization.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 François Cami <fcami@fedoraproject.org> - 1.3.12-1
- Update to latest upstream (1.3.12).

* Sun Dec 29 2013 François Cami <fcami@fedoraproject.org> - 1.3.11-1
- Update to latest upstream (1.3.11).

* Thu Dec 19 2013 François Cami <fcami@fedoraproject.org> - 1.3.10-1
- Update to latest upstream (1.3.10).

* Wed Aug 21 2013 François Cami <fcami@fedoraproject.org> - 1.3.9-1
- Update to latest upstream (1.3.9).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 François Cami <fcami@fedoraproject.org> - 1.3.8-3
- Fix spurious-executable-perm errors in docs/*dox.
- Remove 'manual' hardening, use Fedora's _hardened_build instead.

* Tue Jun 18 2013 François Cami <fcami@fedoraproject.org> - 1.3.8-2
- Use upstream's shared library generation (and retire our own).

* Fri Jun 14 2013 François Cami <fcami@fedoraproject.org> - 1.3.8-1
- Update to latest upstream version

* Fri Apr 26 2013 Marcel Wysocki <maci@satgnu.net> - 1.3.7-1
- Update to latest upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Bruno Wolff III <bruno@wolff.to> - 1.3.3-1
- Update to upstream 1.3.3
- This is mostly bugfixes, but also some new compression support

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.1-1
- Updated to 1.2.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.2-1
- Updated to 1.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-3
- Autorebuild for GCC 4.3

* Sun Oct  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-2
- Add tutorial.txt design.txt to -devel docs

* Sat Oct  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-1
- Initial Fedora package

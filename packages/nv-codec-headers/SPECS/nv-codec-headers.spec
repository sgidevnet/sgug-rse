Name:           nv-codec-headers
Version:        9.1.23.1
Release:        1%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        %url/archive/n%{version}/%{name}-n%{version}.tar.gz

BuildArch:      noarch
       

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
%autosetup -n %{name}-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share


%install
%make_install PREFIX=%{_prefix} LIBDIR=/share


%files
%doc README
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc


%changelog
* Mon Dec 16 2019 Leigh Scott <leigh123linux@gmail.com> - 9.1.23.1-1
- Update to 9.1.23.1

* Tue Sep 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 9.1.23.0-1
- Update to 9.1.23.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Leigh Scott <leigh123linux@googlemail.com> - 9.0.18.1-2
- Use correct path for pkg-config file

* Sat May 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 9.0.18.1-1
- Update to 9.0.18.1

* Fri Mar 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 9.0.18.0-1
- Update to 9.0.18.0

* Sun Feb 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 8.2.15.7-1
- Update to 8.2.15.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 8.2.15.6-1
- Update to 8.2.15.6

* Tue Nov 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.2.15.5-1
- Update to 8.2.15.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.1.24.2-1
- Update to 8.1.24.2

* Sun Apr 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.1.24.1-1
- Update to 8.1.24.1

* Tue Feb 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 8.0.14.1-1
- First build

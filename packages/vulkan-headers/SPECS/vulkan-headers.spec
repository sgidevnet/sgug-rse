%global __python %{__python3}
Name:           vulkan-headers
Version:        1.1.114.0
Release:        2%{?dist}
Summary:        Vulkan Header files and API registry

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-Headers-sdk-%{version}.tar.gz

BuildRequires:  cmake3
BuildArch:      noarch       

%description
Vulkan Header files and API registry

%prep
%autosetup -n Vulkan-Headers-sdk-%{version}


%build
%cmake3 -DCMAKE_INSTALL_LIBDIR=%{_libdir} .
%make_build


%install
%make_install


%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/


%changelog
* Mon Jul 29 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-2
- Update to 1.1.114.0 headers

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Dave Airlie <airlied@redhat.com> - 1.1.108.0-1
- Update to 1.1.108.0 headers

* Thu Apr 18 2019 Dave Airlie <airlied@redhat.com> - 1.1.106.0-1
- Update to 1.1.106.0 headers

* Wed Mar 06 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update to 1.1.101.0 headers

* Wed Feb 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.97.0-1
- Update to 1.1.97.0 headers

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Dave Airlie <airlied@redhat.com> - 1.1.92.0-1
- Update to 1.1.92.0

* Sat Oct 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.85.0-1
- Update to 1.1.85.0

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package

Name:           sdlhack
Version:        1.4
Release:        9%{?dist}
Summary:        Force full-screen games to minimize
License:        LGPLv2+
URL:            http://www.jspenguin.org/software/sdlhack/
Source0:        http://jspenguin.org:81/software/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.1
BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
SDLHack is a wrapper for SDL which lets you force full-screen games to minimize.
It also allows you to disable joystick detection. 

%prep
%autosetup
# Change the path of the library since we install it in a private libdir
sed -i 's|lib%{name}.so|%{_libdir}/%{name}/lib%{name}.so|g' sdlhack

sed -i 's|lib%{name}-i386.so|lib%{name}.so|g;s|lig%{name}-x86_64.so|lib%{name}.so|g' build

# Remove any prebuilt lib
rm -f *.so

%build
export CFLAGS="-v %{optflags}"
bash build

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_mandir}/man1}
install -Dpm 755 %{name} $RPM_BUILD_ROOT%{_bindir}
# Install libsdlhack.so in a privatelib rather than system wide one since it is gonna
# be used only with this program
install -Dpm 755 lib%{name}.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%{_mandir}/man1/%{name}.1.gz

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.4-6
- added gcc as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.4-1
- Rebuilt for new upstream release 1.4

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2-10
- Spec clean up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 31 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.2-1
- Update to 1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.1-1
- Initial package for Fedora

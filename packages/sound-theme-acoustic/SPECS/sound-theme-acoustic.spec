Name: sound-theme-acoustic
Version: 1.0
Release: 14%{?dist}
Summary: Sound theme made on an acoustic guitar
Source0: http://anujmore.fedorapeople.org/sounds/sound-theme-acoustic-%{version}.tar.xz
License: Public Domain
URL: https://fedoraproject.org/wiki/SIGs/Sound
BuildArch: noarch

%description
Sound theme by the Fedora Sound SIG, 
recorded on an acoustic guitar.

%prep
%setup -q

%build
%{nil}

%install
rm -rf $RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_datadir}/sounds/acoustic/stereo/
install -pm 644 index.theme $RPM_BUILD_ROOT%{_datadir}/sounds/acoustic/
cd stereo
install -pm 644 *.oga $RPM_BUILD_ROOT%{_datadir}/sounds/acoustic/stereo/


%post
/bin/touch --no-create %{_datadir}/sounds/acoustic %{_datadir}/sounds

%postun
/bin/touch --no-create %{_datadir}/sounds/acoustic %{_datadir}/sounds

%files
%dir %{_datadir}/sounds/acoustic
%dir %{_datadir}/sounds/acoustic/stereo
%{_datadir}/sounds/acoustic/index.theme
%{_datadir}/sounds/acoustic/stereo/*.oga

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 11 2011 Anuj More <anujmore@fedoraproject.org> - 1.0-1
- Initial build


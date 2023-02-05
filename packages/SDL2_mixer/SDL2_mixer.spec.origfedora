Name:           SDL2_mixer
Version:        2.0.4
Release:        4%{?dist}
Summary:        Simple DirectMedia Layer - Sample Mixer Library

License:        zlib
URL:            https://www.libsdl.org/projects/SDL_mixer/
Source0:        https://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz

BuildRequires:  SDL2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel
BuildRequires:  chrpath
BuildRequires:  pkgconfig(libmodplug) >= 0.8.8
BuildRequires:  fluidsynth-devel
BuildRequires:  libmikmod-devel
BuildRequires:  mpg123-devel
BuildRequires:  opusfile-devel

%description
SDL_mixer is a sample multi-channel audio mixer library.
It supports any number of simultaneously playing channels of 16 bit stereo
audio, plus a single channel of music, mixed by the popular FLAC,
MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries. 

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
sed -i -e 's/\r//g' README.txt CHANGES.txt COPYING.txt
rm -vrf external/

%build
%configure --disable-dependency-tracking \
           --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install install-bin
for i in playmus playwave
do
  chrpath -d %{buildroot}%{_bindir}/${i}
  mv %{buildroot}%{_bindir}/${i} %{buildroot}%{_bindir}/${i}2
done

find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%license COPYING.txt
%doc CHANGES.txt
%{_bindir}/playmus2
%{_bindir}/playwave2
%{_libdir}/libSDL2_mixer-2.0.so.*

%files devel
%doc README.txt
%{_libdir}/libSDL2_mixer.so
%{_libdir}/pkgconfig/SDL2_mixer.pc
%{_includedir}/SDL2/SDL_mixer.h

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-2
- Enable opus support (#1650399)

* Tue Nov 06 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-3
- Switch to %%ldconfig_scriptlets

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-2
- Enable mp3 support

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.1-1
- Update to 2.0.1 (RHBZ #1296752)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-5
- Fix FTBFS with autoreconf

* Thu May 01 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-4
- Add patch for properly include modplug (RHBZ #1093378)

* Wed Nov 20 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-3
- Add some BuildRequires (cicku)
- Delete pkgconfig from -devel subpackage (cicku)
- Removing external folder in prep section (ignatenkobrain)
- Fix license to correct zlib (cicku & ignatenkobrain)

* Mon Nov 18 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-2
- Update for review

* Sat Sep  7 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.0-1
- Based on SDL_mixer

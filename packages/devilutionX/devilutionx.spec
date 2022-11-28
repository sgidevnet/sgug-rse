%global debug 1

%if 0%{debug}
%global __strip /bin/true
%endif


Summary:        A reverse engineered Diablo1 client
Name:           devilutionX
Version:        1.0 
Release:        2%{?dist}
URL:            https://github.com/diasurgical/devilutionX
Source:         devilutionX-1.0.tar.gz 
Source1:        devilutionx.desktop
Patch100:       devilutionX.sgifixes.patch

License:        MIT

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL_mixer-devel

%description


%prep
%setup -q  
%patch100 -p1 -b devilutionX.sgifixes

%build
#export CFLAGS="-I%{_includedir} -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
#export CXXFLAGS="$CFLAGS -std=gnu++11"
#export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%if 0%{debug}
export CFLAGS="-g2 -Og"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
export CXXFLAGS="$CFLAGS -D__BIG_ENDIAN__"
%endif


mv build/CMake ./
mv build/CMakeLists.txt ./
cd build/
%{cmake3} -DNONET=ON -DUSE_SDL1=ON -DHELLFIRE=NO -DDEBUG=OFF -DASAN=OFF -DUBSAN=OFF ..
make %{?_smp_mflags}

%install
cd build
make INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/truetype
cp CharisSILB.ttf %{buildroot}%{_datadir}/fonts/truetype/
cd ..
mkdir -p %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/
install -p -D -m644 Packaging/resources/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

install -m 755 build/devilutionx %{buildroot}%{_bindir}/%{name}
desktop-file-install --remove-category="Qt" --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
# %doc AUTHORS ChangeLog COPYING README doc/*.png doc/*.html
# don't include contents of doc/ directory as it is mostly obsolete
%{_bindir}/%{name}
%{_datadir}/applications/devilutionx.desktop
%{_datadir}/fonts/truetype/CharisSILB.ttf
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%changelog
* Sun Feb 14 2021  HAL <notes2@gmx.de> - 1.0
- 1st commit get's you past cmake configure on Irix 6.5 with sgug-rse gcc 9.2.


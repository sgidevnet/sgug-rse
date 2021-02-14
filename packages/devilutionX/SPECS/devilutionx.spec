Summary:        A reverse engineered Diablo1 client
Name:           devilutionX
Version:        1.0 
Release:        0%{?dist}
URL:            https://github.com/diasurgical/devilutionX
Source:         devilutionX-1.0.tar.gz 
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
export CFLAGS="-I%{_includedir} -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS $RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS -std=gnu++11"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"

mv Packaging/ build/
mv SourceX/ build/
mv 3rdParty/ build/
mv SourceS/ build/
mv Source/ build/
cd build/
%{cmake} -DNONET=ON -DUSE_SDL1=ON -DHELLFIRE=ON .
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README doc/*.png doc/*.html
# don't include contents of doc/ directory as it is mostly obsolete


%changelog
* Sun Feb 14 2021  HAL <notes2@gmx.de> - 1.0
- 1st commit get's you past cmake configure on Irix 6.5 with sgug-rse gcc 9.2.


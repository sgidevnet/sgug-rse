Summary: SDL2 graphics drawing primitives and other support functions
Name: SDL2_gfx
Version: 1.0.3
Release: 5%{?dist}
License: zlib
URL: http://www.ferzkopp.net/Software/SDL2_gfx-2.0/
Source: http://www.ferzkopp.net/Software/SDL2_gfx/%{name}-%{version}.tar.gz
# Requires --batch support not currently in SDL2_test
#Patch0: 0001-test-Add-batch-switch.patch
Patch1: 0002-test-format-security.patch

BuildRequires:  gcc
BuildRequires: SDL2-devel
# for -lSDL2_test
BuildRequires: SDL2-static
#BuildRequires: doxygen

%description
Library providing graphics drawing primitives and other support functions
wrapped up in an addon library for the Simple Direct Media version 2 (SDL2)
cross-platform API layer.

%package devel
Summary: Development files for SDL2_gfx
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: SDL2-devel%{?_isa}

%description devel
This package contains the files required to develop programs which use SDL2_gfx.

%package docs
Summary: API Documentation for SDL2_gfx
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description docs
This package contains the API documentation for SDL2_gfx library.

%prep
%autosetup -p1
find -name '*.[ch]' |xargs chmod -x
sed 's/\r//' README

%build
%configure \
%ifnarch %{ix86} x86_64
    --disable-mmx \
%endif
    --disable-static
%make_build

# API documentation
#cd Docs
#rm -rf html
#doxygen html.doxyfile
#cd ..

# Examples & test suite
#pushd
PREVWD=`pwd`
cd test
  # test/Makefile.in does not respect LDFLAGS
  export CFLAGS='%{optflags} -I.. -L../.libs'
  %configure
  %make_build
cd $PREVWD
#popd

%install
%make_install

# Missing from Makefile.am
install -pm644 SDL2_gfxPrimitives_font.h %{buildroot}%{_includedir}/SDL2/

# API documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a Docs/html %{buildroot}%{_pkgdocdir}/

# This might be useful for live tests; ship it in the devel package
install -d %{buildroot}%{_libdir}/%{name}
install test/testgfx %{buildroot}%{_libdir}/%{name}
install -Dpm0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

find %{buildroot} -type f -name '*.la' -delete

%check
export SDL_VIDEODRIVER=dummy
#export LD_LIBRARY_PATH="$PWD/.libs"
export LD_LIBRARYN32_PATH=/usr/people/*user*/rpmbuild/BUILDROOT/SDL2_gfx-1.0.3-5.sgug.mips/usr/sgug/lib32/:$LD_LIBRARYN32_PATH
cd test
#./testgfx --info all --log all --batch
#./testrotozoom --info all --log all --batch
./testimagefilter

#%%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README AUTHORS
%{_libdir}/*.so.*

%files devel
%{_includedir}/SDL2/*.h
%{_libdir}/*.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files docs
%{_pkgdocdir}/html

%changelog
* Sun Apr 18 2021  HAL <notes2@gmx.de> - 1.0.3-5
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.0.3-1
- Update to version 1.0.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.1-4
- Fix build of testsuite (#1307300)
- Disable tests which require --batch support not in SDL2_test

* Thu Feb 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-3
- Cleanup spec
- Install pkgconfig file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 30 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- 1.0.1 (RHBZ #1111891)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-6
- Depend on arch specific -devel package (Dorin Lazar, #1136066)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-4
- -docs: Version the main package dependency

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-3
- -docs: Don't depend on arch-specific main package
- -devel: Drop pkgconfig dependency

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-2
- Drop old changelog
- Use version macro
- Build and package tests
- Build and package the API documentation
- Fix modes and line breaks for some files

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.0.0-1
- Port SDL_gfx package to SDL2_gfx

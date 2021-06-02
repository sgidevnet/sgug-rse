%define        libname lib%{name}.so

Name:          snes_ntsc
Version:       0.2.2
Release:       21%{?dist}
Summary:       Provides a SNES NTSC video filtering library

License:       LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:       http://blargg.fileave.com/libs/%{name}-%{version}.zip
BuildRequires:  gcc
BuildRequires: SDL-devel

%description
Super NES NTSC video filter. The main benefit is color mixing, as composite
video artifacts are less noticeable than on the NES. Accepts pixels in 16-bit
RGB or 15-bit BGR (native SNES format).


%package devel
Summary:        Development files for snes_ntsc
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for snes_ntsc


%package demos
Summary:        Examples using snes_ntsc

%description demos
Examples using snes_ntsc


%prep
%setup -q
# Some location cleanups
%{__sed} -i 's/\"SDL.h\"/\<SDL\/SDL.h\>/' demo_impl.h
%{__sed} -i 's/\"test.bmp\"/\"\/usr\/share\/snes_ntsc\/test.bmp\"/' demo.c

#Fix EOL encoding
%{__sed} -i 's/\r//' *.txt


%build
# Compile library, link and give it an soname
gcc -c %{optflags} -fPIC %{name}.c
gcc %{optflags} -shared -Wl,-soname,%{libname}.0 -Wl,-lm -o %{libname}.%{version} %{name}.o

# Make symlinks now as they are needed
ln -s %{libname}.%{version} %{libname}.0
ln -s %{libname}.%{version} %{libname}

# Compile demos
gcc %{optflags} benchmark.c -o snes_ntsc_benchmark -L. -lsnes_ntsc
gcc %{optflags} demo.c -o snes_ntsc_demo -L. -lsnes_ntsc -lSDL


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} \
         %{buildroot}%{_includedir} %{buildroot}%{_datadir}/%{name}

# Install include
install -pm 0644 %{name}.h %{buildroot}%{_includedir}
install -pm 0644 %{name}_config.h %{buildroot}%{_includedir}

# Install example
install -pm 0644 test.bmp %{buildroot}%{_datadir}/%{name}

# Install lib and symlinks
install -pm 0755 %{libname}.%{version} %{buildroot}%{_libdir}
mv %{libname}.0 %{buildroot}%{_libdir}
mv %{libname} %{buildroot}%{_libdir}

# Install demos
install -m0755 snes_ntsc_benchmark %{buildroot}%{_bindir}
install -m0755 snes_ntsc_demo %{buildroot}%{_bindir}


%ldconfig_scriptlets



%files
%{_libdir}/%{libname}.0
%{_libdir}/%{libname}.%{version}
%doc changes.txt license.txt


%files devel
%{_libdir}/%{libname}
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%doc snes_ntsc.txt readme.txt


%files demos
%{_datadir}/%{name}
%{_bindir}/snes_ntsc_benchmark
%{_bindir}/snes_ntsc_demo


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 David Timms <iinet.net.au@dtimms> 0.2.2-3
- Initial import into fedora and release bump

* Mon Jun 11 2007 Ian Chapman <packages@amiga-hardware.com> 0.2.2-2
- Fix undefined-non-weak-symbol warnings

* Sun Feb 25 2007 Ian Chapman <packages@amiga-hardware.com> 0.2.2-1
- Upgrade to 0.2.2
- Increased use of macros

* Sun Oct 29 2006 Ian Chapman <packages@amiga-hardware.com> 0.2.1-1
- Initial Release

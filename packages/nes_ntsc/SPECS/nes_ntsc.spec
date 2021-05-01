%define         libname lib%{name}.so

Name:          nes_ntsc
Version:       0.2.2
Release:       19%{?dist}
Summary:       Provides a NES NTSC video filtering library

License:       LGPLv2+
URL:           http://www.slack.net/~ant/libs/ntsc.html
Source0:       http://blargg.fileave.com/libs/%{name}-%{version}.zip
BuildRequires:  gcc
BuildRequires: SDL-devel

%description
NES NTSC video filter library. Pixel artifacts and color mixing play an 
important role in NES games console graphics. Accepts pixels in native 6-bit
NES palette format, or a 9-bit format that includes the three color emphasis
bits in PPU register $2001. Can also output an RGB palette for use in a 
regular blitter


%package devel
Summary:        Development files for nes_ntsc
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for nes_ntsc


%package demos
Summary:        Examples using nes_ntsc

%description demos
Examples using nes_ntsc


%prep
%setup -q
# Some location cleanups
sed -i 's/\"SDL.h\"/\<SDL\/SDL.h\>/' demo_impl.h
sed -i 's/\"test.bmp\"/\"\/usr\/share\/nes_ntsc\/test.bmp\"/' demo.c
# mod EOL{dos}->EOL{unix}
%{__sed} -i 's/\r//' *.txt

#%{__sed} -i 's/\r//' changes.txt
#%{__sed} -i 's/\r//' license.txt
#%{__sed} -i 's/\r//' nes_ntsc.txt
#%{__sed} -i 's/\r//' readme.txt


%build
# Compile library, link and give it an soname
gcc -c $RPM_OPT_FLAGS -fPIC %{name}.c
gcc $RPM_OPT_FLAGS -shared -Wl,-soname,%{libname}.0 -o %{libname}.0.2.2 %{name}.o

# Make symlinks now as they are needed
ln -s %{libname}.0.2.2 %{libname}.0
ln -s %{libname}.0.2.2 %{libname}.0.2.0
ln -s %{libname}.0.2.2 %{libname}

# Compile demos
gcc $RPM_OPT_FLAGS benchmark.c -o nes_ntsc_benchmark -L. -lnes_ntsc -lm
gcc $RPM_OPT_FLAGS demo.c -o nes_ntsc_demo -L. -lnes_ntsc -lm -lSDL


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir} \
         %{buildroot}%{_includedir} %{buildroot}%{_datadir}/%{name}

# Install include
install -pm 0644 %{name}.h %{buildroot}%{_includedir}

# Install test roms and examples
cp -a tests %{buildroot}%{_datadir}/%{name}
install -pm 0644 test.bmp %{buildroot}%{_datadir}/%{name}

# Install lib and symlinks
install -pm 0755 %{libname}.0.2.2 %{buildroot}%{_libdir}
mv %{libname}.0 %{buildroot}%{_libdir}
mv %{libname}.0.2.0 %{buildroot}%{_libdir}
mv %{libname} %{buildroot}%{_libdir}

# Install demos
install -p -m0755 nes_ntsc_benchmark %{buildroot}%{_bindir}
install -p -m0755 nes_ntsc_demo %{buildroot}%{_bindir}


%ldconfig_scriptlets



%files
%{_libdir}/%{libname}.0
%{_libdir}/%{libname}.0.2.0
%{_libdir}/%{libname}.0.2.2
%doc changes.txt license.txt


%files devel
%{_libdir}/%{libname}
%{_includedir}/%{name}.h
%doc nes_ntsc.txt readme.txt


%files demos
%{_datadir}/%{name}
%{_bindir}/nes_ntsc_benchmark
%{_bindir}/nes_ntsc_demo


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug  6 2008 David Timms <iinet.net.au@dtimms> 0.2.2-1
- update ex dribble spec to new release @ new url
- meet fedora license guidelines
- mod sed patches to suit new source filenames

* Sun Oct 29 2006 Ian Chapman <packages@amiga-hardware.com> 0.2.0-1
- Initial Release

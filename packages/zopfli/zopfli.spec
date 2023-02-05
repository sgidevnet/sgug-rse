%global so_ver 1.0.3

Name:           zopfli
Version:        %{so_ver}
Release:        1%{?dist}
Summary:        Zlib compatible better compressor

License:        ASL 2.0
URL:            https://github.com/google/%{name}
Source0:        %{URL}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5%) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

%package        devel
Requires:       %{name} = %{version}-%{release}
Summary:        Development files for zopfli and zopflipng.

%description    devel
Devolopment files for zopfli and zopflipng.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
mkdir build && cd build
%cmake -DZOPFLI_BUILD_SHARED=ON ..
%make_build

%install
cd build
%make_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc CONTRIBUTORS README README.zopflipng
%{_bindir}/%{name}
%{_bindir}/%{name}png

%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{so_ver}

%{_libdir}/lib%{name}png.so.1
%{_libdir}/lib%{name}png.so.%{so_ver}

%files          devel
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}png.so

%{_includedir}/%{name}.h
%{_includedir}/%{name}png_lib.h
%{_libdir}/cmake/Zopfli/*.cmake


%changelog
* Thu Nov 28 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.3-1
- New upstream release 1.0.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.ef109ddgit-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.0.2.ef109ddgit-1
- Update to 1.0.2
- Create devel subpackage

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar  2 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-2
- Ship zopflipng

* Wed Feb 10 2016 Ville Skyttä <ville.skytta@iki.fi> - 1.0.1-1
- Update to 1.0.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.0-1
- upstream release 1.0.0

* Sun Mar 03 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.20130303gitacc035
- initial spec

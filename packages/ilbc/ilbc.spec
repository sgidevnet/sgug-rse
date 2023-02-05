%global commit 88cd1613a1db8d5dee0910a9a0c3e676e31bc529
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		ilbc
Summary:	Internet Low Bitrate Codec
Version:	1.1.1
Release:	17%{?dist}
License:	BSD
URL:            https://github.com/TimothyGu/libilbc
Source0:	%{url}/archive/%{commit}/libilbc-%{shortcommit}.tar.gz
# Fedora/EPEL-specific
Patch1:		%{name}-0001-Don-t-build-silently.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:  gcc
BuildRequires:  make

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.


%package	devel
Summary:	development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig


%description devel
Additional header files for development with %{name}.


%prep
%autosetup -n libilbc-%{commit} -p1


%build
autoreconf -ivf
%configure --disable-static --with-pic
%make_build


%install
%make_install

rm -f %{buildroot}%{_libdir}/libilbc.la
# Required for compatibility with a very old apps
cd %{buildroot}%{_libdir}/pkgconfig && ln -s libilbc.pc ilbc.pc

# Make compat symlinks
cd %{buildroot}%{_includedir}
ln -s ilbc.h iLBC_decode.h
ln -s ilbc.h iLBC_define.h
ln -s ilbc.h iLBC_encode.h



%ldconfig_scriptlets


%files
%doc README
%license COPYING
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/ilbc.h
# Compat symlinks
%{_includedir}/iLBC_decode.h
%{_includedir}/iLBC_define.h
%{_includedir}/iLBC_encode.h
%{_libdir}/pkgconfig/ilbc.pc
%{_libdir}/pkgconfig/libilbc.pc
%{_libdir}/lib%{name}.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Neal Gompa <ngompa13@gmail.com> - 1.1.1-16
- Modernize spec
- Drop EL5 specific stuff

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-3
- Added licensing info

* Wed Aug 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-2
- Add compat symlinks for old apps

* Wed May  9 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-1
- Ver. 1.1.1

* Thu Oct 20 2011 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1
- Initial package

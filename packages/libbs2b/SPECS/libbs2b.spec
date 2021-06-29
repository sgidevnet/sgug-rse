Name:		libbs2b
Version:	3.1.0
Release:	23%{?dist}
Summary:	Bauer stereophonic-to-binaural DSP library

License:	Copyright only
URL:		http://bs2b.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/bs2b/libbs2b/%{version}/%{name}-%{version}.tar.lzma
Patch0:		libbs2b-security.patch

BuildRequires:  gcc-c++
BuildRequires:	autoconf automake libtool
BuildRequires:	libsndfile-devel
# the dependency (required for bs2bconvert) gets added automatically
#Requires:	libsndfile


%package devel
Summary:	Development files for libbs2b
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed
to improve headphone listening of stereo audio records. Recommended for
headphone prolonged listening to disable superstereo fatigue without essential
distortions.


%description devel
This package contains the development files for the Bauer
stereophonic-to-binaural (bs2b) DSP effect library.


%prep
%setup -q
%patch0 -p1

# automake 1.12 removes support for lzma, it has been replaced by xz
# it is safe to substitute xz for lzma to get rid of autoreconf errors,
# we don't build the dist archive anyways
sed -i -e 's/lzma/xz/g' configure.ac
# reconf to support aarch64 (bug #925677)
autoreconf -vif

%build
%configure --disable-static
# disable rpath as suggested in
# https://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.la


%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_libdir}/%{name}.so.*


%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%ldconfig_scriptlets


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.0-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-12
- Fix -Werror=format-security build error 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Karel Volný <kvolny@redhat.com> 3.1.0-10
- cleanup after the change to autoreconf
- fix source URL

* Sat Jan 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-9
- Modernise spec
- Fix autoreconf

* Mon Aug 26 2013 Karel Volný <kvolny@redhat.com> 3.1.0-8
- run autoreconf to support aarch64 (bug #925677)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 31 2009 Karel Volný <kvolny@redhat.com> 3.1.0-2
- specfile cleanup as per review (bug #519138 comment #1)

* Tue Aug 25 2009 Karel Volný <kvolny@redhat.com> 3.1.0-1
- initial Fedora package version

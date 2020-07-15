Name:           libxnm
Version:        0.1.3
Release:        22%{?dist}
Summary:        A library for parsing the XNM format

License:        GPLv2+
URL:            http://xnm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/xnm/%{name}-%{version}.tar.gz

BuildRequires:  gcc
# BuildRequires:  glib2-devel
    
%description
XNM is a simple recursively defined serialization syntax for storing
and communicating of complex data structures

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --enable-static=no
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -rf %{buildroot}/usr/sgug/doc/libxnm/
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#%%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib*.so.*

%files devel
%doc doxygen-doc/*
%{_includedir}/xnm/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
- Mon May 1 2020 HAL <hal@null.not> - 1.16.0-6
* disabled docs and Linux specific settings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-13
- Specfile updated

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-10
- Specfile updated
- Fix FTBFS (#992133)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-4
- Rebuilt

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Updated to new upstream version 0.1.3
- Fixed Source URL, directory ownership, doc for devel subpackage

* Tue Dec 30 2008 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora

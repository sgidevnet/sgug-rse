Name:           flxmlrpc
Version:        0.1.4
Release:        11%{?dist}
Summary:        An xmlrpc library for the NBEMS suite of programs

License:        LGPLv3+
URL:            http://www.w1hkj.com
Source0:        http://www.w1hkj.com/xmlrpc-mods/%{name}-%{version}.tar.gz

# Only needed if building from git checkout.
#BuildRequires:  autoconf automake libtool
BuildRequires:  gcc-c++

%description
This is version %{version} of flxmlrpc, an implementation of the XmlRpc protocol
written in C++, based upon XmlRpc++0.7 and modified to provide additional XmlRpc
Variable types.  It is used in fldigi, flrig, flnet, flmsg, flarq, flamp, fllog;
a suite of programs written for amateur radio emergency communications.

flxmlrpc is designed to make it easy to incorporate xmlrpc client and server
support into C++ applications. Or use both client and server objects in your 
application for easy peer-to-peer support.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
if [ ! -f configure ]
then autoreconf -fi
fi
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -exec rm -f {} \;


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 0.1.4-1
- Update to latest upstream release.

* Thu Apr 23 2015 Richard Shaw <hobbes1069@gmail.com> - 0.1.3-1
- Upstream moved headers into a named subdirectory.

* Mon Apr 20 2015 Richard Shaw <hobbes1069@gmail.com> - 0.1.2-1
- Initial packaging.

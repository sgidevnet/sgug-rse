%global maintainer andikleen
%global commit cbaaa1e91b4b8c45dcdf8c9d1efaaef6d65758a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		spooky-c
Version:	1.0.0
Release:	15%{?dist}
Summary:	C port of Bob Jenkins' spooky hash

License:	BSD
URL:		https://github.com/%{maintainer}/%{name}
Source0:	https://github.com/%{maintainer}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:	autoconf automake libtool

%description
This is a C version of Bob Jenkins' spooky hash. The only advantage over
Bob's original version is that it is in C, not C++ and comes with some
test and benchmark code.

This is a very competitive hash function, but is somewhat non-portable.
It should work on both big and little endian architectures, but will
generate different hashes on them. It's also optimized for 64-bit
architectures. It will work on 32-bit architectures as well, but is much
slower there.

%package devel
Summary:	The development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Additional header files and manpages for development with %{name}.

%prep
%setup -q -n %{name}-%{commit}

%build
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libspooky-c.la

%ldconfig_scriptlets

%files
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-6
- move base package to System Environment/Libraries

* Tue May 26 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-5
- switch to BSD license, update to latest upstream HEAD

* Wed Apr 01 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-4
- add comment pointing out pull request for manpage patch

* Wed Apr 01 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-3
- use github-specific tarball generation

* Mon Mar 30 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-2
- specfile cleanups
- disable static library
- add manpage

* Tue Mar 24 2015 Jeff Layton <jeff.layton@primarydata.com> 1.0.0-1
- initial package build

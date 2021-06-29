# Upstream changed its licensing to ASL 2.0 after releasing 0.9.18.
# This package uses the relicensed sources, which are as close to 0.9.18 as
# possible. Debian uses the exact same revision.
%global commit0 0fa48dbacfe39509577ae6741054be7c05a19aac
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshotdate 20150613

%global libname libfoma

Name:           foma
Version:        0.9.18
Release:        0.4.%{snapshotdate}git%{shortcommit0}%{?dist}
Summary:        Xerox-compatible finite-state compiler

License:        ASL 2.0
URL:            https://github.com/mhulden/foma
Source0:        https://github.com/mhulden/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:         foma-harden-build.patch

BuildRequires:  gcc zlib-devel readline-devel flex bison
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma command line tools.


%package -n     %{libname}
Summary:        The foma C library

%description -n %{libname}
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma C library.


%package -n     %{libname}-devel
Summary:        Development files for %{libname}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
The libfoma-devel package contains libraries and header files for
developing applications that use libfoma.

%prep
%autosetup -n %{name}-%{commit0} -p1


%build
sed -i '/^CFLAGS/c\CFLAGS = %{optflags} -Wl,--as-needed -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC' foma/Makefile
sed -i '/^LDFLAGS/c\LDFLAGS = -lreadline -lz -ltermcap %{build_ldflags}' foma/Makefile
sed -i '/^FLOOKUPLDFLAGS/c\FLOOKUPLDFLAGS = libfoma.a -lz %{build_ldflags}' foma/Makefile

cd foma
%make_build


%install
sed -i '/^prefix/c\prefix = %{buildroot}%{_prefix}' foma/Makefile
sed -i '/^libdir/c\libdir = %{buildroot}%{_libdir}' foma/Makefile
cd foma
%make_install
# Remove static archive
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%files
%{_bindir}/cgflookup
%{_bindir}/flookup
%{_bindir}/foma

%files -n %{libname}
%license foma/COPYING
%doc foma/README
%{_libdir}/%{libname}.so.0
%{_libdir}/%{libname}.so.0.9.18

%files -n %{libname}-devel
%{_includedir}/*.h
%{_libdir}/%{libname}.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.4.20150613git0fa48db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.18-0.3.20150613git0fa48db
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-0.2.20150613git0fa48db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Ville-Pekka Vainio <vpvainio AT iki.fi> 0.9.18-0.1.20150613git0fa48db
- Initial package.

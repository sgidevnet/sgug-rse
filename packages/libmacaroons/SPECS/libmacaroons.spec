Name:		libmacaroons
Version:	0.3.0
Release:	6%{?dist}
Summary:	C library supporting generation and use of macaroons

License:	BSD
URL:		https://github.com/rescrv/libmacaroons
Source0:	%url/archive/releases/%{version}/%{name}-%{version}.tar.gz
# Fix for the inspect() method triggering an assert on newer versions of libsodium.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/52
Patch0:		libmacaroons-hex-encoding.patch

# Fix for the memory leak when the deserialize routine succeeds.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/56
Patch1:		libmacaroons-deserialize-memleak.patch

BuildRequires:	libsodium-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python3

%description
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{name}-releases-%{version}
%patch0 -p 1
%patch1 -p 1

%build
autoreconf -i
export PYTHON=%{__python3}
%configure --disable-python-bindings
%make_build

%ldconfig_scriptlets

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la
rm -f %{buildroot}%{_libdir}/%{name}.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.la

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/macaroons.h

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Brian Bockelman <brian.bockelman@cern.ch> - 0.3.0-2
- Fix memory leak when deserializing a macaroon.

* Mon Mar 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Subpackage python2-macaroons has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Brian Bockelman <bbockelm@cse.unl.edu> - 0.3.0-1
- Initial packaging of libmacaroons.



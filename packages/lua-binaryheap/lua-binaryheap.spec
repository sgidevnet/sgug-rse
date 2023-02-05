%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global majorversion 0
%global minorversion 4
%global tagname version_%{majorversion}v%{minorversion}

%global luapkgname binaryheap

Name:           lua-%{luapkgname}
Version:        %{majorversion}.%{minorversion}
Release:        2%{?dist}
Summary:        Binary heap implementation for Lua

License:        MIT
URL:            https://github.com/Tieske/%{luapkgname}.lua
Source0:        https://github.com/Tieske/%{luapkgname}.lua/archive/%{tagname}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library implementing binary heap algorithm.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Binary heap implementation for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library implementing binary heap algorithm.
%endif

%prep
%setup -q -n binaryheap.lua-%{tagname}

%install
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 src/binaryheap.lua %{buildroot}/%{luacompatpkgdir}/binaryheap.lua
%endif

%files
%doc docs/*
%doc examples
%{luapkgdir}/binaryheap.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc docs/*
%doc examples
%{luacompatpkgdir}/binaryheap.lua
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.4-1
- Initial package for Fedora 28+ and EPEL 7

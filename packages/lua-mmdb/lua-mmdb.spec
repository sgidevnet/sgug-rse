%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname mmdb

Name:           lua-%{luapkgname}
Version:        0.2
Release:        2%{?dist}
Summary:        MaxMind database parser for Lua

License:        MIT
URL:            https://github.com/daurnimator/mmdblua
Source0:        https://github.com/daurnimator/mmdblua/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library for reading MaxMind's Geolocation database format.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        MaxMind database parser for Lua %{luacompatver}
Requires:       lua%{luacompatver}-compat53

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library for reading MaxMind's Geolocation database format.
%endif

%prep
%setup -q -n mmdblua-%{version}

%install
install -d -m 0755 %{buildroot}/%{luapkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/init.lua %{buildroot}/%{luapkgdir}/%{luapkgname}/init.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}/%{luacompatpkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/init.lua %{buildroot}/%{luacompatpkgdir}/%{luapkgname}/init.lua
%endif

%files
%doc example.lua
%license LICENSE.md
%{luapkgdir}/%{luapkgname}

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc example.lua
%license LICENSE.md
%{luacompatpkgdir}/%{luapkgname}
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.2-1
- Initial package for Fedora 28+ and EPEL 7

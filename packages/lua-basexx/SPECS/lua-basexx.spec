%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname basexx

Name:           lua-%{luapkgname}
Version:        0.4.0
Release:        3%{?dist}
Summary:        BaseXX encoding and decoding library for Lua

License:        MIT
URL:            https://github.com/aiq/%{luapkgname}/
Source0:        https://github.com/aiq/%{luapkgname}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua

%description
A Lua library for base2, base16, base32, base64, base85 decoding and encoding
of data strings.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        BaseXX encoding and decoding library for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A Lua library for base2, base16, base32, base64, base85 decoding and encoding
of data strings.
%endif

%prep
%setup -q -n basexx-%{version}

%install
install -D -p -m 0644 lib/basexx.lua %{buildroot}/%{luapkgdir}/basexx.lua

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 lib/basexx.lua %{buildroot}/%{luacompatpkgdir}/basexx.lua
%endif

%files
%doc README.adoc
%license LICENSE
%{luapkgdir}/basexx.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc README.adoc
%license LICENSE
%{luacompatpkgdir}/basexx.lua
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.4.0-2
- Use lua5.1 package naming convention
  https://pagure.io/packaging-committee/issue/878

* Tue Apr 02 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.4.0-1
- Initial package for Fedora 28+ and EPEL 7

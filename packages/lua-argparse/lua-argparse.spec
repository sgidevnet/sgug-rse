%{!?_licensedir:%global license %%doc}
#%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global luaver 5.3
%global luapkgdir %{_datadir}/lua/%{luaver}

%global commit a40458fdc1507e44b6a829b6c6b969b500e1c337
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global pkg_name argparse

# Proper naming for the tarball from github.
%global gittar %{name}-%{version}.tar.gz

Name:           lua-%{pkg_name}
Version:        0.5.0
Release:        9%{?dist}
Summary:        Feature-rich command line parser for Lua

License:        MIT
URL:            https://github.com/mpeterv/%{pkg_name}
Source0:        %{url}/archive/%{commit}/%{gittar}

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?fedora}
Requires:       lua(abi) = %{luaver}
%else
Requires:       lua >= %{luaver}
%endif

%description
Argparse is a feature-rich command line parser for Lua inspired by argparse
for Python.

Argparse supports positional arguments, options, flags, optional arguments,
subcommands and more. Argparse automatically generates usage, help and error
messages.

# Sphinx is currently not available for EPEL, so only build the docs for
# Fedora.
%if 0%{?fedora}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  dos2unix
Requires:       python3-sphinx_rtd_theme

%description    doc
This package contains documentation for %{name}.
%endif

%prep
%setup -qn %{pkg_name}-%{commit}
rm -rf doc

%if 0%{?fedora}
%build
sphinx-build-3 -b html -d build/doctree docsrc doc
# Remove fonts so that we don't package them..
rm -rf doc/_static/fonts
# Additional cleanup...
rm -rf doc/.buildinfo
dos2unix doc/_static/jquery.js
%endif

%install
install -m 644 -D -p src/%{pkg_name}.lua %{buildroot}%{luapkgdir}/%{pkg_name}.lua

%files
%if 0%{?fedora}
%license LICENSE
%else
%doc LICENSE
%endif
%doc README.md
%{luapkgdir}/%{pkg_name}.lua

%if 0%{?fedora}
%files doc
%license LICENSE
%doc doc
%endif

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Hard-coded Lua version to address build issues

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 9 2015 Jeff Backus <jeff.backus@gmail.com> - 0.5.0-1
- Updated to latest version / address bug #1289954

* Thu Sep 10 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.1-2
- Fixed build issue on EPEL

* Tue Aug 4 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.1-1
- Updated to latest version
- Removed extraneous patch

* Tue Aug 4 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-3
- Changed license handling to more readable form
- Modified to rebuild sphinx documentation and remove fonts
- Added patch to put license at head of argparse.lua

* Mon Jul 27 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-2
- Fixed permissions on argparse.lua
- Added proper handling of license for EPEL6
- Removed commented-out macros

* Wed Jul 22 2015 Jeff Backus <jeff.backus@gmail.com> - 0.4.0-1
- Initial release

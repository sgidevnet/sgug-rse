Name:    rofi
Version: 1.5.4
Release: 1%{?dist}
Summary: A window switcher, application launcher and dmenu replacement

# lexer/theme-parser.[ch]:
# These files are generated from lexer/theme-parser.y and licensed with GPLv3+
# with Bison exception.
# As the source file is licensed with MIT, according to the Bison exception,
# the shipped files are considered to be MIT-licensed.
# See also
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/C4VVT54Z4WFGJPPD5X54ILKRF6X2IFLZ/
License: MIT
URL:     https://github.com/DaveDavenport/rofi
Source0: https://github.com/DaveDavenport/rofi/releases/download/%{version}/rofi-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: gcc-c++
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

# https://github.com/sardemff7/libgwater
Provides: bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides: bundled(libnkutils)

Requires:      %{name}-themes = %{version}-%{release}


%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains documentation files for developing
applications that use %{name}.

%package        themes
Summary:        Themes for %{name}
BuildArch:      noarch

%description    themes
The %{name}-themes package contains themes for %{name}.

%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}

make doxy
find doc/html/html -name "*.map" -delete
find doc/html/html -name "*.md5" -delete


%install
%make_install


%check
make check || (cat ./test-suite.log; false)


%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%files themes
%license COPYING
%{_datarootdir}/rofi

%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc

%files devel-doc
%license COPYING
%doc doc/html/html/*



%changelog
* Thu Aug 01 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.5.1-7
- Add patch to fix undefined behavior of char* initialization

* Sun Nov 11 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-6
- Do not package .md5 or .map files
- Remove scriptlet to modify shebang, rely on mangler instead

* Sat Nov 10 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-5
- Replace BR pkconfig(xcb-util) -> pkgconfig(xcb-aux)
- Clarify license of bison-generated files

* Thu Nov 08 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-4
- Rename doc sub-package to devel-doc

* Tue Nov 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-3
- Install license file to all independently installable packages

* Tue Nov 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-2
- Move themes into a separate noarch sub-package
- Make doc sub-package noarch

* Mon Nov 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Run tests
- Remove upstreamed patch
- Add missing BR: doxygen
- Add missing BR: graphviz

* Tue Oct 24 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.4.2-1
- Initial package

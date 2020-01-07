Name:           neofetch
Version:        6.0.0
Release:        4%{?dist}
Summary:        CLI system information tool written in Bash

License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source0:        https://github.com/dylanaraps/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         neofetch.sgirpmfixes.patch

BuildArch:      noarch
Requires:       bash >= 3.2
#Requires:       bind-utils
Requires:       coreutils
Requires:       gawk
Requires:       grep
#Requires:       pciutils
Recommends:     caca-utils
Recommends:     catimg
Recommends:     ImageMagick
Recommends:     jp2a
Recommends:     w3m-img
Recommends:     xorg-x11-server-utils
Recommends:     xorg-x11-utils

%description
Neofetch displays information about your system next to an image,
your OS logo, or any ASCII file of your choice. The main purpose of Neofetch
is to be used in screenshots to show other users what OS/distribution you're
running, what theme/icons you're using and more.

%prep
%autosetup
sed 's,/usr/bin/env bash,%{_bindir}/bash,g' -i neofetch

%build

%install
%make_install PREFIX=%{_prefix} MANDIR=%{_mandir}

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Aug 03 2019 K. de Jong <keesdejong@fedoraproject.org> - 6.0.0-4
- Red Hat Bugzilla - Bug 1736808

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 K. de Jong <keesdejong@fedoraproject.org> - 6.0.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 K. de Jong <keesdejong@fedoraproject.org> - 5.0.0-1
- New upstream release

* Tue Jun 12 2018 K. de Jong <keesdejong@fedoraproject.org> - 4.0.2-1
- New upstream release
- Cleaned up dependencies

* Fri Apr 06 2018 Kees de Jong <keesdejong@fedoraproject.org> - 3.4.0-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 13 2017 Kees de Jong <keesdejong@fedoraproject.org> - 3.3.0-1
- Initial package

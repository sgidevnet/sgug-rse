# To reduce boilerplate.
%global make_flags bindir=%{_bindir} mandir="%{_mandir}" prefix="%{_prefix}" \\\
CC=%{__cc} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ENABLE_MAN=1


Name:           cc1541
Version:        3.1
Release:        1%{?dist}
Summary:        Tool for creating Commodore 1541 Floppy disk images in D64, G64, D71 or D81 format

License:        MIT
URL:            https://bitbucket.org/PTV_Claus/%{name}
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  make

%description
This is %{name} v%{version}, a tool for creating Commodore 1541
Floppy disk images in D64, G64, D71 or D81 format with custom
sector interleaving etc.   Also supports extended tracks 35-40
using either SPEED DOS or DOLPHIN DOS BAM-formatting.


%prep
%autosetup -S git -p 1


%build
%make_build %{make_flags}


%install
%make_install %{make_flags}


%check
%make_build check %{make_flags}


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Sep 03 2019 Björn Esser <besser82@fedoraproject.org> - 3.1-1
- New upstream release

* Wed Aug 28 2019 Björn Esser <besser82@fedoraproject.org> - 3.0-2
- Add an upstream patch to fix a bug

* Sun Aug 25 2019 Björn Esser <besser82@fedoraproject.org> - 3.0-1
- New upstream release

* Sun Jul 28 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-3
- Add some upstream patches to improve rpm packaging

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-1
- Initial import (#1722942)

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.3
- Upstream PR has been merged

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.2
- Remove pre-built binaries from build-tree during %%prep.

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.1
- Initial rpm release (#1722942)

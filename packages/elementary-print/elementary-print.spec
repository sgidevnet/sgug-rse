%global srcname print
%global appname io.elementary.print

Name:           elementary-print
Summary:        Simple shim for printing support via Contractor
Version:        0.1.3
Release:        3%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       contractor
Supplements:    contractor


%description
Simple shim for printing support via Contractor.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%files
%{_bindir}/%{appname}

%{_datadir}/contractor/%{appname}.contract


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Initial package for fedora.


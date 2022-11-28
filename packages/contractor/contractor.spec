Name:           contractor
Summary:        Desktop-wide extension service
Version:        0.3.4
Release:        3%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus


%description
An extension service that allows apps to use the exposed functionality
of registered apps. This way, apps don't have to have the functions hard
coded into them.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# Create the the directory where other programs put their contracts
mkdir -p %{buildroot}/%{_datadir}/%{name}


%files
%doc README.md
%license COPYING

%{_bindir}/%{name}

%dir %{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.4-1
- Update to version 0.3.4.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3-1
- Update to version 0.3.3.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-10
- Clean up .spec file.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-6
- Make BR on /usr/bin/pkg-config explicit.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-5
- Own contract directory explicitly.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-4
- Clean up spec file.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-3
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-2
- Spec file cosmetics.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-1
- Update to version 0.3.2.



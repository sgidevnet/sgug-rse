Name:           gnome-getting-started-docs
Version:        3.34.2
Release:        1%{?dist}
Summary:        Help a new user get started in GNOME

License:        CC-BY-SA
URL:            http://help.gnome.org/
Source0:        http://download.gnome.org/sources/gnome-getting-started-docs/3.34/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  yelp-tools
Requires: gnome-user-docs

%description
This package contains a 'Getting Started' guide that can be viewed
with yelp. It is normally used together with gnome-initial-setup.


%package cs
Summary:        Czech translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-cs)

%description cs
Czech (cs) translations for the Getting Started guide videos.


%package de
Summary:        German translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-de)

%description de
German (de) translations for the Getting Started guide videos.


%package es
Summary:        Spanish translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-es)

%description es
Spanish (es) translations for the Getting Started guide videos.


%package fr
Summary:        French translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-fr)

%description fr
French (fr) translations for the Getting Started guide videos.


%package gl
Summary:        Galician translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-gl)

%description gl
Galician (gl) translations for the Getting Started guide videos.


%package hu
Summary:        Hungarian translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-hu)

%description hu
Hungarian (hu) translations for the Getting Started guide videos.


%package it
Summary:        Italian translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-it)

%description it
Italian (it) translations for the Getting Started guide videos.


%package pl
Summary:        Polish translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-pl)

%description pl
Polish (pl) translations for the Getting Started guide videos.


%package pt_BR
Summary:        Brazilian Portuguese translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-pt_BR)

%description pt_BR
Brazilian Portuguese (pt_BR) translations for the Getting Started guide videos.


%package ru
Summary:        Russian translations for gnome-getting-started-docs videos
Requires:       gnome-getting-started-docs = %{version}-%{release}
Supplements:    (%{name} = %{version}-%{release} and langpacks-ru)

%description ru
Russian (ru) translations for the Getting Started guide videos.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install

%find_lang %{name} --all-name --with-gnome


%files -f %{name}.lang
%doc NEWS AUTHORS
%license COPYING
%exclude %{_datadir}/help/cs/gnome-help/figures/
%exclude %{_datadir}/help/de/gnome-help/figures/
%exclude %{_datadir}/help/es/gnome-help/figures/
%exclude %{_datadir}/help/fr/gnome-help/figures/
%exclude %{_datadir}/help/gl/gnome-help/figures/
%exclude %{_datadir}/help/hu/gnome-help/figures/
%exclude %{_datadir}/help/it/gnome-help/figures/
%exclude %{_datadir}/help/pl/gnome-help/figures/
%exclude %{_datadir}/help/pt_BR/gnome-help/figures/
%exclude %{_datadir}/help/ru/gnome-help/figures/

%files cs
%{_datadir}/help/cs/gnome-help/figures/

%files de
%{_datadir}/help/de/gnome-help/figures/

%files es
%{_datadir}/help/es/gnome-help/figures/

%files fr
%{_datadir}/help/fr/gnome-help/figures/

%files gl
%{_datadir}/help/gl/gnome-help/figures/

%files hu
%{_datadir}/help/hu/gnome-help/figures/

%files it
%{_datadir}/help/it/gnome-help/figures/

%files pl
%{_datadir}/help/pl/gnome-help/figures/

%files pt_BR
%{_datadir}/help/pt_BR/gnome-help/figures/

%files ru
%{_datadir}/help/ru/gnome-help/figures/


%changelog
* Wed Apr 29 2020 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 28 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Sun Feb 17 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Feb 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.18.2-3
- Added Supplements tag for langpacks installation

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Tue Oct 13 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Mon Apr 20 2015 Petr Kovar <pkovar@redhat.com> - 3.16.1-1
- Update to 3.16.1
- Use license macro for COPYING

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Oct 14 2014 Petr Kovar <pkovar@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Add subpackages for fr and ru video translations

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Mon Aug 18 2014 Petr Kovar <pkovar@redhat.com> - 3.13.90-1
- Update to 3.13.90

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Petr Kovar <pkovar@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Tue Mar 25 2014 Petr Kovar <pkovar@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Feb 18 2014 Petr Kovar <pkovar@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Nov 12 2013 Petr Kovar <pkovar@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Oct 15 2013 Petr Kovar <pkovar@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Petr Kovar <pkovar@redhat.com> - 3.10.0.1-1
- Update to 3.10.0.1

* Mon Sep 23 2013 Petr Kovar <pkovar@redhat.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Petr Kovar <pkovar@redhat.com> - 3.8.3-1
- Update to 3.8.3

* Tue May 14 2013 Petr Kovar <pkovar@redhat.com> - 3.8.2-1
- Update to 3.8.2
- Add gs-browse-web-firefox.page.patch
- Add subpackages for hu and it

* Wed Apr 17 2013 Petr Kovar <pkovar@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Petr Kovar <pkovar@redhat.com> - 3.8.0.1-1
- Update to 3.8.0.1

* Tue Mar 26 2013 Petr Kovar <pkovar@redhat.com> - 3.8.0-1
- Update to 3.8.0
- Add subpackages for translated videos

* Wed Mar 20 2013 Petr Kovar <pkovar@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Fri Feb 22 2013 Petr Kovar <pkovar@redhat.com> - 3.7.90-2%{?dist}
- gnome-initial-setup fix

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.2-2%{?dist}
- Add two missing files

* Tue Nov 20 2012 Matthias Clasen <mclasen@redhat.com> - 3.7.2-1%{?dist}
- Initial packaging

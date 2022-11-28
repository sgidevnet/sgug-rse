Name:           notification-daemon-engine-nodoka
Version:        0.1.0
Release:        29%{?dist}
Summary:        The Nodoka theme engine for the notification daemon

License:        GPLv3+
URL:            https://nodoka.fedorahosted.org/
Source0:        https://fedorahosted.org/releases/n/o/nodoka/notification-daemon-engine-nodoka-%{version}.tar.gz
Patch0:         notification-daemon-engine-nodoka-clipping.patch
Patch1:         notification-daemon-engine-nodoka-0.1.0-version-check.patch
Patch2:         notification-daemon-engine-nodoka-rtl.patch
Patch3:         notification-daemon-engine-nodoka-base-color.patch
# drop libsexy dep
Patch4:         sexy.patch
Patch5:         notification-daemon-engine-nodoka-window-type.patch
Patch6:         %{name}-0.1.0-automake.patch

BuildRequires:  gtk2-devel >= 2.17.1
BuildRequires:  libxml2-devel
BuildRequires:  autoconf automake libtool
Requires:       notification-daemon

%description
The Nodoka theme engine for the notification daemon.


%prep
%setup -q
%patch0 -p1 -b .clipping
%patch1 -p1 -b .version-check
%patch2 -p1 -b .rtl
%patch3 -p1 -b .base-color
%patch4 -p1 -b .sexy
%patch5 -p1 -b .window-type
%patch6 -p1 -b .automake

autoreconf -i -f

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true



%files
%doc AUTHORS ChangeLog COPYING Credits NEWS README
%{_libdir}/notification-daemon-1.0/engines/libnodoka.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Martin Sourada <mso@fedoraproject.org> - 0.1.0-16
- Fix build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.0-13
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 18 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.0-11
- Set the proper type hint on notification bubbles (bgo#595062)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.0-9
- Fix the libsexy removal patch

* Thu Jul  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.0-8
- Drop libsexy dep

* Sat Jun 20 2009 Martin Sourada <mso@fedoraproject.org> - 0.1.0-7
- Use gtkrc specified color for background (fixes rhbz #498422)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 27 2008 Martin Sourada <mso@fedoraproject.org> - 0.1.0-5
- Add support for rtl (rhbz #475381)

* Sun Nov 23 2008 Martin Sourada <mso@fedoraproject.org> - 0.1.0-4
- Make version check less strict (mclasen, rhbz #472661)

* Wed Jul 16 2008 Martin Sourada <martin.sourada@gmail.com> - 0.1.0-3
- Don't clip text in message bubbles (rhbz #455617)

* Fri May 16 2008 Martin Sourada <martin.sourada@gmail.com> - 0.1.0-2
- Add BR: libxml2-devel, see #446842

* Sun Apr 20 2008 Martin Sourada <martin.sourada@gmail.com> - 0.1.0-1
- Initial RPM package

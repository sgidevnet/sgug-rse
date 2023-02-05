Name:           gcolor2
Version:        0.4
Release:        18%{?dist}
Summary:        A simple color selector for GTK+2

License:        GPLv2
URL:            http://gcolor2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
# Patch extracted from
# http://patch-tracker.debian.org/patch/nondebian/dl/gcolor2/0.4-2.1
Patch0:         %{name}-0.4-missing-includes.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=716100
# bugs.debian.org/cgi-bin/bugreport.cgi?bug=634606
Patch1:         %{name}-0.4-ftbfs.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel perl(XML::Parser) desktop-file-utils

%description
gcolor2 is a simple color selector that was originally based on gcolor, 
ported to use GTK+2, and now has a completely new UI. 

%prep
%setup -q
%patch0 -p1 -b .missing
%patch1 -p1 -b .ftbfs
# make sure path to icon is correct
sed -i 's!/usr/share!%{_datadir}!' %{SOURCE1}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-install                                    \
  --dir=%{buildroot}%{_datadir}/applications       \
  %{SOURCE1}



%files
%doc AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4-4
- Fix FTBFS with patch by Johannes Lips (#716100)

* Sat Oct 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4-3
- Fix missing includes (#525783)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 16 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.4-1
- Initial Fedora package

Name:		9wm
Summary:	Emulation of the Plan 9 window manager 8 1/2
Version:	1.4.1
Release:	4%{?dist}
License:	MIT
# Source0:	https://woozle.org/neale/g.cgi/x11/9wm/snapshot/9wm-%{version}.tar.gz
Source0:	https://github.com/9wm/9wm/archive/%{version}.tar.gz
Source1:	9wm.desktop
URL:		https://woozle.org/neale/src/9wm/
BuildRequires:  gcc
BuildRequires:	libXext-devel, libX11-devel, desktop-file-utils
# It needs this to open a terminal.
Requires:	xterm

%description
9wm is an X window manager which attempts to emulate the Plan 9 window
manager 8-1/2 as far as possible within the constraints imposed by X.
It provides a simple yet comfortable user interface, without garish
decorations or title-bars. Or icons.  And it's click-to-type.

%prep
%setup -q -n 9wm-%{version}

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DSHAPE"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make DESTDIR=%{buildroot} BIN=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 install install.man
desktop-file-install					\
--dir=${RPM_BUILD_ROOT}%{_datadir}/xsessions/		\
%{SOURCE1}

%files
%doc README.md CREDITS.md
%license LICENSE.md
%{_bindir}/9wm
%{_datadir}/xsessions/9wm.desktop
%{_mandir}/man1/9wm.*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Sun Mar 26 2017 Tom Callaway <spot@fedoraproject.org> - 1.3.7-1
- update to 1.3.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Tom Callaway <spot@fedoraproject.org> - 1.3.5-1
- update to 1.3.5

* Tue Nov 17 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.4-1
- update to 1.3.4

* Thu Oct 29 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-2
- fix defattr invocation

* Tue Oct 6 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-1
- Initial package for Fedora


%global pkg lua
%global pkgname Lua major mode

Name:           emacs-%{pkg}
Version:        20151025
Release:        9%{?dist}
Summary:        Lua major mode for GNU Emacs

License:        GPLv2+
URL:            http://lua-mode.luaforge.net
Source0:        https://github.com/immerrr/lua-mode/archive/lua-mode-20151025.tar.gz
Source1:        lua-init.el
BuildArch:      noarch

BuildRequires:  emacs(bin), emacs-el >= %{_emacs_version}
BuildRequires:  pkgconfig
Requires:       emacs(bin) >= %{_emacs_version}

Obsoletes:      emacs-%{pkg}-el <= 20130419-5
Provides:       emacs-%{pkg}-el <= 20130419-5

%description
A GNU Emacs major mode for editing Lua code.

%prep
%setup -q -n lua-mode-%{version}


%build
%{_emacs_bytecompile} lua-mode.el


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -p -m 0644 lua-mode.el $RPM_BUILD_ROOT%{_emacs_sitelispdir}
install -p -m 0644 lua-mode.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}


%files
%{_emacs_sitestartdir}/lua-init.el
%{_emacs_sitelispdir}/lua-mode.elc
%{_emacs_sitelispdir}/lua-mode.el

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20151025-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 20151025-1
- Update to latest stable release 20151025

* Fri Oct 23 2015 Tim Niemueller <tim@niemueller.de> - 20130419-6
- Obsolete -el sub-package, fixes bugzilla 1234539

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130419-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130419-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Tim Niemueller <tim@niemueller.de> 20130419-3
- Use even more Emacs macros from build system

* Tue Jan 21 2014 Tim Niemueller <tim@niemueller.de> 20130419-2
- Use Emacs macros from build system

* Tue Jan 21 2014 Tim Niemueller <tim@niemueller.de> 20130419-1
- Update to latest stable release, fixes bz #1006896

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071122-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 27 2008 Tim Niemueller <timn@fedoraprojdect.org> 20071122-5
- dropped XEmacs support, an ancestor of lua-mode is in xemacs-packages-extra
- dropped patch, was only needed for XEmacs
- fixed errorneous require, must be %%{emacs_version} not just emacs_version.
- removed some double-slashes in paths

* Sat Jan 26 2008 Tim Niemueller <timn@fedoraprojdect.org> 20071122-4
- el packages require respective base package
- Use cp -p in build section to preserve timestamp

* Tue Jan 22 2008 Tim Niemueller <timn@fedoraprojdect.org> 20071122-3
- Use full templates, pkgconfig is not installed by default in buildroot

* Mon Jan 21 2008 Tim Niemueller <timn@fedoraprojdect.org> 20071122-2
- BR pkgconfig
- Excplicitly BR the minimum versions of emacs-el and xemacs-devel that
  provide the pkgconfig files

* Fri Jan 18 2008 Tim Niemueller <timn@fedoraprojdect.org> 20071122-1
- Initial SPEC file


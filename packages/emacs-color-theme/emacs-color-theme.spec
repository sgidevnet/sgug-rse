%global pkg color-theme
%global pkgname Emacs Color Themes

Name:		emacs-%{pkg}
Version:	6.6.0
Release:	17%{?dist}
Summary:	Color themes for Emacs

License:	GPLv2+
URL:		http://www.nongnu.org/color-theme
Source0:	http://ftp.twaren.net/Unix/NonGNU/color-theme/%{pkg}-%{version}.tar.gz
Source1:	emacs-color-theme-init.el
#Patches are submitted to upstream
#http://lists.nongnu.org/archive/html/color-theme-devel/2010-04/msg00000.html
#Patch to fix Makefile
Patch0:		emacs-%{pkg}-fix-compile.patch
#Patch to fix README
Patch1:		emacs-%{pkg}-fix-readme.patch
#Patch to fix License file
Patch2:		emacs-%{pkg}-fix-copying-eol.patch

BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}

%description
%{pkgname} is an add-on package for GNU Emacs.
It provides a lot of different color themes to skin your Emacs greatly
improving the editing experience. It also includes a neat framework to
help you creating new themes from your current emacs customization's.
Also features an easy way to share your custom themes with the world.  

%package -n %{name}-el
Summary:	Elisp source files for %{pkgname} under GNU Emacs
Requires:	%{name} = %{version}-%{release}

%description -n %{name}-el
This package contains the elisp source files for %{pkgname} under GNU
Emacs. You do not need to install this package to run %{pkgname}.
Install the %{name} package to use %{pkgname} with GNU Emacs.

%prep
%setup -q -n %{pkg}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes
mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
cp *.el *.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}
cp themes/*.el themes/*.elc %{buildroot}%{_emacs_sitelispdir}/%{pkg}/themes

%files
%doc COPYING README
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/themes/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/emacs-color-theme-init.el

%files -n %{name}-el
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/themes/*.el

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 9 2010 Arun SAG <sagarun@gmail.com> - 6.6.0-3
- clean section removed
- Added startup file emacs-color-theme-init.el
- 
* Sat Apr 17 2010 Arun SAG <sagarun@gmail.com> - 6.6.0-2
- Spec adjusted to obey latest emacs packaging guidelines
- License field corrected to GPLv2+

* Thu May 15 2009 Filippo Argiolas <fargiolas@gnome.org> - 6.6.0-1
- Initial packaging

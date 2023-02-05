%define pkg htmlize
%define pkgname HTMLize

%if %($(pkg-config emacs) ; echo $?)
%define emacs_lispdir %{_datadir}/emacs/site-lisp
%define emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%define emacs_version 22.2
%else
%define emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%define emacs_startdir %(pkg-config emacs --variable sitestartdir)
%define emacs_version %(pkg-config emacs --modversion)
%endif

Summary:	Convert buffer text and decorations to HTML
Name:		emacs-%{pkg}
Version:	1.34
Release:	18%{?dist}
License:	GPLv2+
URL:		http://www.emacswiki.org/emacs-en/Htmlize
Source0:	http://fly.srk.fer.hr/~hniksic/emacs/%{pkg}.el
Source1:	%{pkg}-init.el


Requires:	emacs(bin) >= emacs_version

BuildRequires:	emacs
BuildRequires:	emacs-el

BuildArch:	noarch

%description
%{pkgname} is an add-on package for GNU Emacs. It converts the buffer text and
the associated decorations to HTML. The conversion is quite sophisticated, it
understands non-ascii characters, looks up colours in the X11 RGB database,
and can generate either CSS or old style font bits.

%package el
Summary:	Emacs Lisp source files for %{name}

Requires:	%{name} = %{version}-%{release}

%description el
This package contains Emacs Lisp source files for %{name} under
GNU Emacs. You do not need to install this package to run %{pkgname}.
Install the %{name} package to use %{pkgname} with GNU Emacs.

%prep
%setup -cT
cp -p %{SOURCE0} .

%build
emacs -batch -f batch-byte-compile ./%{pkg}.el

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{emacs_lispdir}/%{pkg}
mkdir -p $RPM_BUILD_ROOT%{emacs_startdir}

install -p -m644 ./%{pkg}.el $RPM_BUILD_ROOT%{emacs_lispdir}/%{pkg}
install -p -m644 ./%{pkg}.elc $RPM_BUILD_ROOT%{emacs_lispdir}/%{pkg}
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{emacs_startdir}

%files
%dir %{emacs_lispdir}/%{pkg}
%{emacs_lispdir}/%{pkg}/%{pkg}.elc
%{emacs_startdir}/%{pkg}-init.el

%files el
%{emacs_lispdir}/%{pkg}/%{pkg}.el

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.34-2
- Added copyright and distribution notices to htmlize-init.el.

* Sat Jan 17 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.34-1
- Initial build.

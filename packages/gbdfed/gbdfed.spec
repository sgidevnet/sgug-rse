Name:		gbdfed
Summary: 	Bitmap Font Editor
Version:	1.6
Release:	12%{?dist}
License:	MIT
Source0:	http://www.math.nmsu.edu/~mleisher/Software/gbdfed/%{name}-%{version}.tar.bz2
Source1:	http://www.math.nmsu.edu/~mleisher/Software/gbdfed/%{name}16x16.png
Source2:	gbdfed.desktop
Patch0:		gbdfed-1.6-format-security-fix.patch
# Fix some of the gtk issues
Patch2:		gbdfed-1.6-gtkfix.patch
URL:		http://www.math.nmsu.edu/~mleisher/Software/gbdfed/
BuildRequires:  gcc
BuildRequires:	freetype-devel, pango-devel, libX11-devel, libICE-devel, gtk2-devel
BuildRequires:	desktop-file-utils, autoconf

%description
gbdfed lets you interactively create new bitmap font files or 
modify existing ones. It allows editing multiple fonts and multiple 
glyphs, it allows cut and paste operations between fonts and glyphs and 
editing font properties. The editor works natively with BDF fonts.

%prep
%setup -q 
%patch0 -p1 -b .format-security-fix
%patch2 -p1 -b .gtkfix

# This is incredibly hackish, and will likely not work when these deprecated bits are removed outright.
sed "s:-D.*_DISABLE_DEPRECATED::" -i Makefile.in

%build
autoconf
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" install
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/gbdfed.png
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{SOURCE2}

%files
%doc README
%{_bindir}/gbdfed
%{_datadir}/pixmaps/gbdfed.png
%{_datadir}/applications/*.desktop
%{_mandir}/man1/gbdfed*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Tom Callaway <spot@fedoraproject.org> - 1.6-1
- update to 1.6
- fix format-security issues

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-3
- coax this beast to life for one last build

* Wed Feb 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-2
- Fix implicit DSO issue with libX11

* Tue Jul 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-1
- update to 1.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4-1
- initial Fedora package

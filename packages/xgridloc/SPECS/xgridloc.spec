Name:		xgridloc
Version:	0.9
Release:	28%{?dist}
Summary:	A GTK+ application for the calculation of Maidenhead QRA Locators

License:	GPLv3
URL:		http://5b4az.chronos.org.uk/pages/locator.html

Source0:	http://5b4az.chronos.org.uk/pkg/locator/%{name}/%{name}-%{version}.tar.gz
# desktop file
Source1:	%{name}.desktop
# icon file
Source2:	%{name}.png
# default config file wrapper script 
Source3:	xgridloc.sh.in


BuildRequires:	desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel

%description
xgridloc is a GTK+ graphical version of gridloc and performs the same basic 
functions for ham radio operators, but additionally it can use xplanet to 
display the home and DX locations and the great circle path between them.

%prep
%setup -qn %{name}
sh autogen.sh

%build
./autogen.sh
%configure LDFLAGS="-lm"
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" PACKAGE_LIBS="$PACKAGE_LIBS -lm"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# no upstream .desktop or icon yet so we'll use a temporary one.
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install  \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
# --vendor="fedora" obsolete per new package guidelines.

# install default user configuration file
install -p -D -m 0644 $RPM_BUILD_DIR/%{name}/default/.xgridlocrc $RPM_BUILD_ROOT%{_datadir}/%{name}/xgridlocrc

# move original binary to libexecdir
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-bin
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

# install wrapper script 
install -p -D -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/xgridloc

%files
%doc AUTHORS NEWS README doc/%{name}.html COPYING
%dir %{_datadir}/%{name}
%{_libexecdir}/%{name}-bin
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/xgridlocrc
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9-13
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 30 2010 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-11
- recommit

* Fri Apr 30 2010 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-10
- fix .desktop add Network;

* Thu Apr 22 2010 Jon Ciesla <limb@jcomserv.net> - 0.9-9
- Fix for libm DSO Linking FTBFS, BZ 565163.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 9 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-6
- Upstream source added COPYING file
- Fix .desktop file removed ext from icon
- Mock build f11/devel i386
- Test build on Koji all arches

* Fri Feb 6 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-5
- bump src to f11
- minor spec edits

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-4
- Check rpmlint fix lint errors
- 3 packages and 1 specfiles checked; 0 errors, 0 warnings.
- Submit for review
- Mock build f9/10/devel i386
- Test build on Koji all arches

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-3
- Add default config file
- Mock build f9/10/devel i386

* Sun Jan 18 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-2
- Mock build f9/10/devel i386

* Wed Jan 14 2009 Randall J. Berry 'Dp67' <dp67@fedoraproject.org> - 0.9-1
- Upstream upgrade to 0.9
- rpmbuild F9 i386

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.7-1
- Initial spec

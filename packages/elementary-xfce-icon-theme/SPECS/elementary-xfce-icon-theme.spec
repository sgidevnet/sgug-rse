Name:           elementary-xfce-icon-theme
Version:        0.15.1
Release:        2%{?dist}
Summary:        Icons for Xfce based on the elementary Project Icon Theme
 

License:        GPLv2
URL:            https://github.com/shimmerproject/elementary-xfce 
Source0:       https://github.com/shimmerproject/elementary-xfce/releases/tag/%{version}#/elementary-xfce-%{version}.tar.gz 

BuildArch:      noarch

BuildRequires:  gtk3-devel >= 3.18
BuildRequires:  optipng

%description
This is an icon-theme maintained with Xfce in mind,
but it supports other desktops like Gnome3 as well.
It's a fork of the upstream elementary-project, 
which took place because the team decided to
drop a lot of desktop-specific symlinks. 
This icon-theme is supposed to keep everything 
working, but we'll still pull new icons from upstream 
and integrate them occasionally.

%prep
%setup -c -q %{name}/
mkdir -p doc/elementary-xfce{,-dark}
# fix for the wrong naming inside the tar.gz
mv elementary-xfce-%{version}/{README.md,LICENSE,CONTRIBUTORS,AUTHORS} doc/elementary-xfce/
# Create symbolic links for each theme variant
ln -s ../elementary-xfce/{README.md,LICENSE,CONTRIBUTORS,AUTHORS} doc/elementary-xfce-dark/

%build


%install
mkdir -p  %{buildroot}%{_datadir}/icons
cp -a elementary-xfce-%version/elementary-xfce/  %{buildroot}%{_datadir}/icons
cp -a elementary-xfce-%version/elementary-xfce-dark/  %{buildroot}%{_datadir}/icons

chmod 0644  %{buildroot}%{_datadir}/icons/elementary-xfce/index.theme
chmod 0644  %{buildroot}%{_datadir}/icons/elementary-xfce-dark/index.theme


# Remove darker and darkest theme
rm -rf %{buildroot}%{_datadir}/icons/elementary-xfce-darkest/
rm -rf %{buildroot}%{_datadir}/icons/elementary-xfce-darker

# Remove broken links
rm -rf %{buildroot}%{_datadir}/icons/elementary-xfce/{README.md,LICENSE,CONTRIBUTORS,AUTHORS}
rm -rf %{buildroot}%{_datadir}/icons/elementary-xfce-dark/{README.md,LICENSE,CONTRIBUTORS,AUTHORS}



%post
touch --no-create %{_datadir}/icons/elementary-xfce &>/dev/null ||:
touch --no-create %{_datadir}/icons/elementary-xfce-dark &>/dev/null ||:



%postun
if [ $1 -eq 0 ] ; then
         touch --no-create %{_datadir}/icons/elementary-xfce &>/dev/null
         touch --no-create %{_datadir}/icons/elementary-xfce-dark &>/dev/null     
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce &>/dev/null
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce-dark
&>/dev/null

fi

%posttrans
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce &>/dev/null
         gtk-update-icon-cache -q %{_datadir}/icons/elementary-xfce-dark
&>/dev/null


%files
%{_datadir}/icons/elementary-xfce/
%{_datadir}/icons/elementary-xfce-dark/
%doc doc/*


%changelog
* Sun Jul 05 2020 Johannes Lips <hannes@fedoraproject.org> - 0.15.1-2
- removal of the darker theme - no benefit and lots of issues

* Sun Jul 05 2020 Johannes Lips <hannes@fedoraproject.org> - 0.15.1-1
- update to latest upstream version 0.15.1

* Tue Apr 14 2020 Johannes Lips <hannes@fedoraproject.org> - 0.15-2
- minor fixes

* Sun Mar 22 2020 Johannes Lips <hannes@fedoraproject.org> - 0.15-1
- update to latest upstream version 0.15

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Johannes Lips <hannes@fedoraproject.org> - 0.14-1
- update to latest upstream version 0.14

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Johannes Lips <hannes@fedoraproject.org> - 0.13.1-1
- update to latest upstream version 0.13.1

* Fri Sep 14 2018 Johannes Lips <hannes@fedoraproject.org> - 0.13-1
- update to latest upstream version 0.13

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Johannes Lips <hannes@fedoraproject.org> - 0.12-1
- update to latest upstream version 0.12

* Wed May 09 2018 Johannes Lips <hannes@fedoraproject.org> - 0.11-1
- update to latest upstream version 0.11

* Thu Mar 01 2018 Johannes Lips <hannes@fedoraproject.org> - 0.10-1
- update to latest upstream version 0.10

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Johannes Lips <hannes@fedoraproject.org> - 0.9-1
- update to latest upstream version 0.9

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Johannes Lips <hannes@fedoraproject.org> - 0.8-1
- update to latest upstream version 0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Johannes Lips <hannes@fedoraproject.org> - 0.7-1
- update to latest upstream version 0.7

* Fri Aug 21 2015 Johannes Lips <hannes@fedoraproject.org> - 0.6-1
- update to latest upstream version 0.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 17 2015 Johannes Lips <hannes@fedoraproject.org> - 0.5-1
- update to latest upstream version 0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Johannes Lips <hannes@fedoraproject.org> - 0.4-1
- update to latest upstream version 0.4
- add section to prevent conflicting file problem

* Sat Jul 27 2013 Johannes Lips <hannes@fedoraproject.org> - 0.3-3
- added %%posttrans scripts

* Thu Jul 25 2013 Johannes Lips <hannes@fedoraproject.org> - 0.3-2
- minor fixes of the spec

* Sat Jul 06 2013 Johannes Lips <hannes@fedoraproject.org> - 0.3-1
- Intial rpm build Fedora

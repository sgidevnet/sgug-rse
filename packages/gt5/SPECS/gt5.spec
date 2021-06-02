Name:		gt5
Summary:	A diff-capable 'du-browser'
Version:	1.4.0
Release:	22%{?dist}
License:	GPL+
URL:		http://gt5.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gt5-1.4.0-fix-max-depth.diff
BuildArch:	noarch
#something else is required in runtime?
Requires:	gawk
#sed is not needed to mention only in BuildRequires
Requires:	sed
#Some console web browser is required (e.g. links links2 elinks lynx w3m)
Requires:	text-www-browser

%description
Allows to check what takes the most of your hard disk space and track
its changes.
Note: It requires some console web browser installed in the system
(e.g. links, links2, elinks, lynx, w3m).

%prep
%setup -q
%patch0 -p0

%build
#it's a shell-script, nothing to do

%install
rm -fr %{buildroot}
#make install requires a patch to drop out chown root:root,
#it was suggested to use install -p instead of
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -p gt5 %{buildroot}%{_bindir}/
install -p gt5.1 %{buildroot}%{_mandir}/man1/

%files
%attr(0755,root,root) %{_bindir}/gt5
#INSTALL is not needed
%doc README LICENSE Changelog
%{_mandir}/man1/gt5.1*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.4.0-13
- Fix critical problem with parsing `du` man page
- Fix rpmlint warnings
 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.0-5
- fix conditional comparison

* Sat Oct 27 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.4.0-4
- applied suggestions by Mamoru Tasaka (all below)
- removed a chown patch by a direct use of an 'install' command
- removed INSTALL from a documentation set
- added using "text-www-browser" virtial Provides for F-8+

* Tue Sep 18 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.4.0-3
- {name} variable used in a source URL (thanks to Parag AN)

* Tue Sep 11 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.4.0-2
- sed restored in Requires section
- added info about required console web browser (thanks to Till Maas)

* Tue Sep 04 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.4.0-1
- updated to 1.4.0
- removed DESTDIR patch (merged with an upstream version)

* Tue Sep 04 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3d-3
- added missing DESTDIR in a patch (thanks to Thomas Sattler)
- specified licence type (due to a new Licensing Guidelines)

* Tue May 29 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3d-2
- BuildArch changed to noarch

* Sat May 12 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.3d-1
- initial release


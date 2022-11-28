Name:           gnome-search-tool
Version:        3.6.0
Release:        15%{?dist}
Summary:        Utility for finding files for GNOME

License:        GPLv2+ and GFDL
#No URL for the package specifically, as of now
URL:            http://www.gnome.org/gnome-3/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-search-tool/3.6/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  rarian-compat
BuildRequires:  docbook-dtds
BuildRequires:  libSM-devel
BuildRequires:  desktop-file-utils

Obsoletes: gnome-utils < 1:3.3
Obsoletes: gnome-utils-devel < 1:3.3
Obsoletes: gnome-utils-libs < 1:3.3

%description
GNOME Search Tool is a utility for finding files on your system. To perform a
basic search, you can type a filename or a partial filename, with or without
wildcards. To refine your search, you can apply additional search options.

GNOME Search Tool uses the find, grep, and locate UNIX commands. Since the
find, grep, and locate commands support the -i option, all searches are
case-insensitive.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

make install DESTDIR=$RPM_BUILD_ROOT

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=730809
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">gnome-search-tool.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Search the files on your computer</summary>
  <description>
    <p>
      The Search Tool allows you to search your computer for files
      based on their names. It also allows you to restrict the search
      to specific directories, and specify other parameters for searching
      such as when a file was last modified.
    </p>
  </description>
  <url type="homepage">https://git.gnome.org/browse/gnome-search-tool/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-search-tool/a.png</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.docs NEWS
%{_datadir}/GConf/gsettings/gnome-search-tool.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-search-tool.gschema.xml
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gsearchtool
%{_mandir}/man1/%{name}.1.gz


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.6.0-6
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Sat Mar 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.1-6
- Don't obsolete gnome-system-log

* Fri Mar 16 2012 Rui Matos <rmatos@redhat.com> - 3.3.1-5
- Obsolete all gnome-utils subpackages

* Tue Mar 13 2012 Rui Matos <rmatos@redhat.com> - 3.3.1-4
- Added Obsoletes: gnome-utils < 1:3.3

* Mon Mar 12 2012 Rui Matos <rmatos@redhat.com> - 3.3.1-3
- Use GConf rpm macros instead of open coded scriplets

* Mon Mar  5 2012 Rui Matos <rmatos@redhat.com> - 3.3.1-2
- spec file cleanup

* Tue Nov 15 2011 Anuj More <anujmorex@gmail.com> - 3.3.1-1
- rebuilt


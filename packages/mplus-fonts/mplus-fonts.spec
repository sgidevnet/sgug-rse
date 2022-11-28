###############################################################################
# Definitions
###############################################################################
%global fixed_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and fixed-halfwidth \
%1 %2 %3 for alphabets. They are 5 weights from Thin to Bold.   

%global proportional_desc() \
The combination of fixed-fullwidth M+ %2 for Japanese and proportional  \
%1 %2 %3 for alphabets. They are 7 weights from Thin to Black.         

%global common_desc() \
The Mplus fonts are 7 families of fonts, of which 4 are combinations \
of proportional font families,variations of fixed-fullwidth fonts, \
variations of fixed-halfwidth fonts and each have between 5 - 7 \
different weights.

%global summary_p M+ P is aimed as sophisticated and relaxed design

%global summary_c M+ C is optimized to be proportioned and has two variations

%global summary_m M+ M emphasize the balance of natural letterform and high legibility


%global fontname mplus

###############################################################################
# Header
###############################################################################

Name:       %{fontname}-fonts
Version:    056
Release:    11%{?dist}
Summary:    The Mplus fonts is a superfamily of fonts designed by Coji Morishita

License:    mplus
URL:        http://%{fontname}-fonts.sourceforge.jp/%{fontname}-outline-fonts/index-en.html
Source0:    http://dl.sourceforge.jp/%{fontname}-fonts/6650/%{fontname}-TESTFLIGHT-%{version}.tar.xz

BuildArch: noarch  
BuildRequires:   fontpackages-devel  

%description
%common_desc

###############################################################################
# Package section
###############################################################################

%package common
Summary:  Mplus, common files (documentation…)
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


# 1p
%package -n %{fontname}-1p-fonts
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1p-fonts
%proportional_desc M+ 1P Type-1

%_font_pkg -n %{fontname}-1p %{fontname}-1p-*.ttf
%{_datadir}/appdata/mplus-1p.metainfo.xml

# 2p
%package -n %{fontname}-2p-fonts
Summary: %summary_p
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2p-fonts
%proportional_desc M+ 2P Type-2

%_font_pkg -n %{fontname}-2p %{fontname}-2p-*.ttf
%{_datadir}/appdata/%{fontname}-2p.metainfo.xml

# 1c
%package -n %{fontname}-1c-fonts
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1c-fonts
%proportional_desc M+ 1C Type-1

%_font_pkg -n %{fontname}-1c %{fontname}-1c-*.ttf
%{_datadir}/appdata/%{fontname}-1c.metainfo.xml

# 2c
%package -n %{fontname}-2c-fonts
Summary: %summary_c
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2c-fonts
%proportional_desc M+ 2C Type-2

%_font_pkg -n %{fontname}-2c %{fontname}-2c-*.ttf
%{_datadir}/appdata/%{fontname}-2c.metainfo.xml

# 1m
%package -n %{fontname}-1m-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1m-fonts
%fixed_desc M+ 1M Type-1

%_font_pkg -n %{fontname}-1m %{fontname}-1m-*.ttf
%{_datadir}/appdata/%{fontname}-1m.metainfo.xml

# 2m
%package -n %{fontname}-2m-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-2m-fonts
%fixed_desc M+ 2M Type-2

%_font_pkg -n %{fontname}-2m %{fontname}-2m-*.ttf
%{_datadir}/appdata/%{fontname}-2m.metainfo.xml

# 1mn
%package -n %{fontname}-1mn-fonts
Summary: %summary_m
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-1mn-fonts
%fixed_desc M+ 1MN Type-1

%_font_pkg -n %{fontname}-1mn %{fontname}-1mn-*.ttf
%{_datadir}/appdata/%{fontname}-1mn.metainfo.xml

###############################################################################
# Files
###############################################################################
%prep
%setup -q -n %{fontname}-TESTFLIGHT-%{version}

%build

%install

# Add AppStream metadata
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1c.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1c</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1C</name>
  <summary>A font which is optimized to be proportioned</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2c.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-2c</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1C</name>
  <summary>A font which is optimized to be proportioned</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1m.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1m</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1M</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1mn.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1mn</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1MN</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-1p.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1p</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 1P</name>
  <summary>A font which is aimed as sophisticated and relaxed design</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2p.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-1p</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 2P</name>
  <summary>A font which is aimed as sophisticated and relaxed design</summary>
</component>
EOF
cat > %{buildroot}%{_datadir}/appdata/%{fontname}-2m.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="font">
  <id>mplus-2m</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>M+ 2M</name>
  <summary>A font which emphasizes the balance of natural letterform with high legibility</summary>
</component>
EOF

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

%files common
%doc LICENSE_{E,J} README_{E,J}

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 056-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 056-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 056-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 056-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 056-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 056-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 056-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 056-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 056-3
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 056-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 16 2013 Parag <paragn AT fedoraproject DOT org> - 056-1
- update to 056 version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Igshaan Mesias <igshaan.mesias@gmail.com> - 028-1
- Initial Release


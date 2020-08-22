%define release_name Not Just Tools
%define dist_version 0.0.6beta
%define bug_version 0.0.6beta

# Change this when branching to fNN
%define doc_version 0.0.6beta

# The package can only be built by a very small number of people
# if you are not sure you can build it do not attempt to

Summary:        SGUG RSE release files
Name:           sgugrse-release
Version:        0.0.6beta
Release:        1
License:        MIT
URL:            https://sgi.sh/

Source1:        LICENSE
#Source2:        Fedora-Legal-README.txt

#Source10:       85-display-manager.preset
#Source11:       90-default.preset
#Source12:       90-default-user.preset
#Source13:       99-default-disable.preset
#Source14:       80-server.preset
#Source15:       80-workstation.preset
#Source16:       org.gnome.shell.gschema.override
#Source17:       org.projectatomic.rpmostree1.rules
#Source18:       80-iot.preset
Source19:       distro-template.swidtag
Source20:       distro-edition-template.swidtag
#Source21:       iot-clevis.conf
#Source22:       80-coreos.preset

BuildArch:      noarch

Provides:       sgugrse-release = %{version}-%{release}
Provides:       sgugrse-release-variant = %{version}-%{release}

# We need to Provides: and Conflicts: system release here and in each
# of the sgugrse-release-$VARIANT subpackages to ensure that only one
# may be installed on the system at a time.
Conflicts:      system-release
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       sgugrse-release-common = %{version}-%{release}

BuildRequires:  sgug-rpm-config >= 2-1

%description
SGUG RSE release files such as various /usr/sgug/etc/ files that define the release and files that determine which services are enabled by default.


%package common
Summary: SGUG RSE release files

Requires:   sgugrse-release-variant = %{version}-%{release}
Suggests:   sgugrse-release

Obsoletes:  sgug-release < 0.0.6beta
Provides:   sgug-release
Obsoletes:  sgugrse-release < 0.0.6beta

Requires:   sgugrse-repos(%{version}) >= 0.0.6beta

%description common
Release files common to all Editions and Spins of SGUG RSE

# %package cinnamon
# Summary:        Base package for Fedora Cinnamon-specific default configurations

# RemovePathPostfixes: .cinnamon
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description cinnamon
# Provides a base package for Fedora Cinnamon-specific configuration files to
# depend on as well as Cinnamon system defaults.


# %package cloud
# Summary:        Base package for Fedora Cloud-specific default configurations

# RemovePathPostfixes: .cloud
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description cloud
# Provides a base package for Fedora Cloud-specific configuration files to
# depend on.


# %package container
# Summary:        Base package for Fedora container specific default configurations

# RemovePathPostfixes: .container
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description container
# Provides a base package for Fedora container specific configuration files to
# depend on as well as container system defaults.


# %package coreos
# Summary:        Base package for Fedora CoreOS-specific default configurations

# RemovePathPostfixes: .coreos
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description coreos
# Provides a base package for Fedora CoreOS Host-specific configuration files to
# depend.


# %package iot
# Summary:        Base package for Fedora IoT specific default configurations

# RemovePathPostfixes: .iot
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description iot
# Provides a base package for Fedora IoT specific configuration files to
# depend on as well as IoT system defaults.


# %package kde
# Summary:        Base package for Fedora KDE Plasma-specific default configurations

# RemovePathPostfixes: .kde
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description kde
# Provides a base package for Fedora KDE Plasma-specific configuration files to
# depend on as well as KDE Plasma system defaults.


# %package matecompiz
# Summary:        Base package for Fedora MATE-Compiz-specific default configurations

# RemovePathPostfixes: .matecompiz
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description matecompiz
# Provides a base package for Fedora MATE-compiz-specific configuration files to
# depend on as well as MATE-Compiz system defaults.


# %package server
# Summary:        Base package for Fedora Server-specific default configurations

# RemovePathPostfixes: .server
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description server
# Provides a base package for Fedora Server-specific configuration files to
# depend on.


# %package silverblue
# Summary:        Base package for Fedora Silverblue-specific default configurations

# RemovePathPostfixes: .silverblue
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description silverblue
# Provides a base package for Fedora Silverblue-specific configuration files to
# depend on as well as Silverblue system defaults.


# %package snappy
# Summary:        Base package for Fedora snap specific default configurations

# RemovePathPostfixes: .snappy
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description snappy
# Provides a base package for Fedora snap specific configuration files to
# depend on as well as Snappy system defaults.


# %package soas
# Summary:        Base package for Fedora Sugar on a Stick-specific default configurations

# RemovePathPostfixes: .soas
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description soas
# Provides a base package for Fedora Sugar on a Stick-specific configuration files to
# depend on as well as SoaS system defaults.


%package workstation
Summary:        Base package for SGUG RSE Workstation-specific default configurations

RemovePathPostfixes: .workstation
Conflicts:      system-release
Provides:       sgugrse-release = %{version}-%{release}
Provides:       sgugrse-release-variant = %{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})
Provides:       base-module(platform:f%{version})
Requires:       sgugrse-release-common = %{version}-%{release}
Provides:       system-release-product


%description workstation
Provides a base package for SGUG RSE Workstation-specific configuration files to
depend on.


# %package xfce
# Summary:        Base package for Fedora Xfce specific default configurations

# RemovePathPostfixes: .xfce
# Conflicts:      system-release
# Provides:       fedora-release = %{version}-%{release}
# Provides:       fedora-release-variant = %{version}-%{release}
# Provides:       system-release
# Provides:       system-release(%{version})
# Provides:       base-module(platform:f%{version})
# Requires:       fedora-release-common = %{version}-%{release}


# %description xfce
# Provides a base package for Fedora Xfce specific configuration files to
# depend on as well as Xfce system defaults.


%prep
#sed -i 's|@@VERSION@@|%{dist_version}|g' %{SOURCE2}

echo "This package is super not finished"
exit 1

%build

perl -pi -e "s|||g" blah

%install
rm -rf %{buildroot}/*
install -d %{buildroot}%{_prefix}/lib
echo "SGUG RSE release %{version} (%{release_name})" > %{buildroot}%{_prefix}/lib/sgugrse-release
echo "cpe:/o:sgugrseproject:sgugrse:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../../../usr/sgug/lib/sgugrse-release %{buildroot}%{_sysconfdir}/sgugrse-release
ln -s ../../../usr/sgug/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s sgugrse-release %{buildroot}%{_sysconfdir}/sgug-release
ln -s sgugrse-release %{buildroot}%{_sysconfdir}/system-release

# Create the common os-release file
cat << EOF >>%{buildroot}%{_prefix}/lib/os-release
NAME=SGUG RSE
VERSION="%{dist_version} (%{release_name})"
ID=sgugrse
VERSION_ID=%{dist_version}
VERSION_CODENAME=""
PLATFORM_ID="platform:rse%{dist_version}"
PRETTY_NAME="SGUG RSE %{dist_version} (%{release_name})"
ANSI_COLOR="0;34"
LOGO=sgugrse-logo-icon
CPE_NAME="cpe:/o:sgugrseproject:sgugrse:%{dist_version}"
HOME_URL="https://sgi.sh/"
DOCUMENTATION_URL="https://sgi.sh/"
SUPPORT_URL="https://sgi.sh/"
BUG_REPORT_URL="https://sgi.sh/"
EOF

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../../../usr/sgug/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../../../usr/sgug/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

mkdir -p %{buildroot}%{_swidtagdir}

# Create os-release files for the different editions

# # Cinnamon
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.cinnamon
# echo "VARIANT=\"Cinnamon\"" >> %{buildroot}%{_prefix}/lib/os-release.cinnamon
# echo "VARIANT_ID=cinnamon" >> %{buildroot}%{_prefix}/lib/os-release.cinnamon
# sed -i -e "s|(%{release_name})|(Cinnamon)|g" %{buildroot}%{_prefix}/lib/os-release.cinnamon
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cinnamon/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cinnamon

# # Cloud
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.cloud
# echo "VARIANT=\"Cloud Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.cloud
# echo "VARIANT_ID=cloud" >> %{buildroot}%{_prefix}/lib/os-release.cloud
# sed -i -e "s|(%{release_name})|(Cloud Edition)|g" %{buildroot}%{_prefix}/lib/os-release.cloud
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Cloud/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cloud

# # Container
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.container
# echo "VARIANT=\"Container Image\"" >> %{buildroot}%{_prefix}/lib/os-release.container
# echo "VARIANT_ID=container" >> %{buildroot}%{_prefix}/lib/os-release.container
# sed -i -e "s|(%{release_name})|(Container Image)|g" %{buildroot}%{_prefix}/lib/os-release.container
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Container/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.container

# # CoreOS
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.coreos
# echo "VARIANT=\"CoreOS\"" >> %{buildroot}%{_prefix}/lib/os-release.coreos
# echo "VARIANT_ID=coreos" >> %{buildroot}%{_prefix}/lib/os-release.coreos
# sed -i -e "s|(%{release_name})|(CoreOS)|g" %{buildroot}%{_prefix}/lib/os-release.coreos
# sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-coreos/"|' %{buildroot}%{_prefix}/lib/os-release.coreos
# sed -i -e 's|HOME_URL=.*|HOME_URL="https://getfedora.org/coreos/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
# sed -i -e 's|SUPPORT_URL=.*|SUPPORT_URL="https://github.com/coreos/fedora-coreos-tracker/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
# sed -i -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://github.com/coreos/fedora-coreos-tracker/"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
# sed -i -e 's|PRETTY_NAME=.*|PRETTY_NAME="Fedora CoreOS %{dist_version}"|' %{buildroot}/%{_prefix}/lib/os-release.coreos
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/CoreOS/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.coreos

# # IoT
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.iot
# echo "VARIANT=\"IoT Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.iot
# echo "VARIANT_ID=iot" >> %{buildroot}%{_prefix}/lib/os-release.iot
# sed -i -e "s|(%{release_name})|(IoT Edition)|g" %{buildroot}%{_prefix}/lib/os-release.iot
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/IoT/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.iot

# # KDE Plasma
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.kde
# echo "VARIANT=\"KDE Plasma\"" >> %{buildroot}%{_prefix}/lib/os-release.kde
# echo "VARIANT_ID=kde" >> %{buildroot}%{_prefix}/lib/os-release.kde
# sed -i -e "s|(%{release_name})|(KDE Plasma)|g" %{buildroot}%{_prefix}/lib/os-release.kde
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/KDE/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde

# # MATE-Compiz
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.matecompiz
# echo "VARIANT=\"MATE-Compiz\"" >> %{buildroot}%{_prefix}/lib/os-release.matecompiz
# echo "VARIANT_ID=matecompiz" >> %{buildroot}%{_prefix}/lib/os-release.matecompiz
# sed -i -e "s|(%{release_name})|(MATE-Compiz)|g" %{buildroot}%{_prefix}/lib/os-release.matecompiz
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/MATE-Compiz/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.matecompiz

# # Server
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.server
# echo "VARIANT=\"Server Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.server
# echo "VARIANT_ID=server" >> %{buildroot}%{_prefix}/lib/os-release.server
# sed -i -e "s|(%{release_name})|(Server Edition)|g" %{buildroot}%{_prefix}/lib/os-release.server
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Server/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.server

# # Silverblue
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.silverblue
# echo "VARIANT=\"Silverblue\"" >> %{buildroot}%{_prefix}/lib/os-release.silverblue
# echo "VARIANT_ID=silverblue" >> %{buildroot}%{_prefix}/lib/os-release.silverblue
# sed -i -e "s|(%{release_name})|(Silverblue)|g" %{buildroot}%{_prefix}/lib/os-release.silverblue
# sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora-silverblue/"|' %{buildroot}%{_prefix}/lib/os-release.silverblue
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Silverblue/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.silverblue

# # Snappy
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.snappy
# echo "VARIANT=\"Snappy\"" >> %{buildroot}%{_prefix}/lib/os-release.snappy
# echo "VARIANT_ID=snappy" >> %{buildroot}%{_prefix}/lib/os-release.snappy
# sed -i -e "s|(%{release_name})|(Snappy)|g" %{buildroot}%{_prefix}/lib/os-release.snappy
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Snappy/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.snappy

# # Sugar on a Stick
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.soas
# echo "VARIANT=\"Sugar on a Stick\"" >> %{buildroot}%{_prefix}/lib/os-release.soas
# echo "VARIANT_ID=soas" >> %{buildroot}%{_prefix}/lib/os-release.soas
# sed -i -e "s|(%{release_name})|(Sugar on a Stick)|g" %{buildroot}%{_prefix}/lib/os-release.soas
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Sugar/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.soas

# Workstation
cp -p %{buildroot}%{_prefix}/lib/os-release \
      %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT=\"Workstation Edition\"" >> %{buildroot}%{_prefix}/lib/os-release.workstation
echo "VARIANT_ID=workstation" >> %{buildroot}%{_prefix}/lib/os-release.workstation
sed -i -e "s|(%{release_name})|(Workstation Edition)|g" %{buildroot}%{_prefix}/lib/os-release.workstation
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Workstation/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.sgugrseproject.Sgugrse-edition.swidtag.workstation

# # Xfce
# cp -p %{buildroot}%{_prefix}/lib/os-release \
#       %{buildroot}%{_prefix}/lib/os-release.xfce
# echo "VARIANT=\"Xfce\"" >> %{buildroot}%{_prefix}/lib/os-release.xfce
# echo "VARIANT_ID=xfce" >> %{buildroot}%{_prefix}/lib/os-release.xfce
# sed -i -e "s|(%{release_name})|(Xfce)|g" %{buildroot}%{_prefix}/lib/os-release.xfce
# sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/Xfce/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.xfce

# Create the symlink for /etc/os-release
ln -s ../../../usr/sgug/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# # Set up the dist tag macros
# install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
# cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# # dist macros.

# %%sgugrse              %{dist_version}
# %%__bootstrap         ~bootstrap
# %%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}.fc%{dist_version}%%{?with_bootstrap:%{__bootstrap}}
# %%sgugrse%{dist_version}                1
# EOF

# Install licenses
mkdir -p licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE
#install -pm 0644 %{SOURCE2} licenses/Fedora-Legal-README.txt

# # Default system wide
# install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
# install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# # Fedora CoreOS
# install -Dm0644 %{SOURCE22} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# # Fedora IoT
# install -Dm0644 %{SOURCE18} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# mkdir -p %{buildroot}/%{_sysconfdir}/dracut.conf.d
# install -Dm0644 %{SOURCE21} -t %{buildroot}/%{_sysconfdir}/dracut.conf.d/

# # Fedora Server
# install -Dm0644 %{SOURCE14} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# # Fedora Workstation
# install -Dm0644 %{SOURCE15} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# # Override the list of enabled gnome-shell extensions for Workstation
# install -Dm0644 %{SOURCE16} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
# install -Dm0644 %{SOURCE17} -t %{buildroot}%{_datadir}/polkit-1/rules.d/

# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%{bug_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.sgugrseproject.Sgugrse-%{bug_version}.swidtag
install -d %{buildroot}%{_sysconfdir}/swid/swidtags.d
ln -s %{_swidtagdir} %{buildroot}%{_sysconfdir}/swid/swidtags.d/sgugrseproject.org

# Work around upgrade bug
# See https://bugzilla.redhat.com/show_bug.cgi?id=1710543
# If we are upgrading from a system with two fedora-release-$EDITION packages
# on it, if DNF upgrade decides to keep the drop that doesn't match
# /usr/lib/variant, it will forcibly create a /usr/lib/os-release symlink
# after the new upgraded package is installed, resulting in an unbootable
# system. As a hack, we'll assume ownership of /usr/lib/variant and set it to
# a nonexistent edition name, to ensure that no symlink gets created.
# This hack and this file can be dropped in Fedora 32, since we don't support
# upgrades from Fedora N-3.
#echo _DISABLED_ > %{buildroot}%{_prefix}/lib/variant


# %posttrans common -p <lua>
# -- Migrate users affected by rhbz#1780827 away from the eclipse module
# -- But only do it once
# original = "%{_sysconfdir}/dnf/modules.d/eclipse.module"
# moved = original .. ".rpmmoved"
# if not posix.stat(moved) then
#   if posix.stat(original) then
#     os.rename(original, moved)
#     print("Disabling eclipse module. See https://fedoraproject.org/wiki/Common_F31_bugs#eclipse-module-reset")
#   else
#     io.open(moved, "w"):close()
#   end
# end


%files common
#%%license licenses/LICENSE licenses/Fedora-Legal-README.txt
%license licenses/LICENSE
%{_prefix}/lib/sgugrse-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/sgugrse-release
%{_sysconfdir}/sgug-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
#%%attr(0644,root,root) %%{_prefix}/lib/variant
#%%attr(0644,root,root) %%{_rpmconfigdir}/macros.d/macros.dist
#%%dir %{_prefix}/lib/systemd/user-preset/
#%%{_prefix}/lib/systemd/user-preset/90-default-user.preset
#%%dir %{_prefix}/lib/systemd/system-preset/
#%%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
#%%{_prefix}/lib/systemd/system-preset/90-default.preset
#%%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%dir %{_swidtagdir}
%{_swidtagdir}/org.sgugrseproject.Sgugrse-%{bug_version}.swidtag
%dir %{_sysconfdir}/swid
%{_sysconfdir}/swid/swidtags.d


%files
%{_prefix}/lib/os-release


# %files cloud
# %{_prefix}/lib/os-release.cloud
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cloud


# %files cinnamon
# %{_prefix}/lib/os-release.cinnamon
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.cinnamon


# %files container
# %{_prefix}/lib/os-release.container
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.container


# %files coreos
# %{_prefix}/lib/systemd/system-preset/80-coreos.preset
# %{_prefix}/lib/os-release.coreos
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.coreos


# %files iot
# %{_prefix}/lib/os-release.iot
# %{_prefix}/lib/systemd/system-preset/80-iot.preset
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.iot
# %{_sysconfdir}/dracut.conf.d/iot-clevis.conf


# %files kde
# %{_prefix}/lib/os-release.kde
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde


# %files matecompiz
# %{_prefix}/lib/os-release.matecompiz
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.matecompiz


# %files server
# %{_prefix}/lib/os-release.server
# %{_prefix}/lib/systemd/system-preset/80-server.preset
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.server


# %files silverblue
# %{_prefix}/lib/os-release.silverblue
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.silverblue
# # Keep this in sync with workstation below
# %{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
# %{_prefix}/lib/systemd/system-preset/80-workstation.preset
# %attr(0644,root,root) %{_prefix}/share/polkit-1/rules.d/org.projectatomic.rpmostree1.rules

# %files snappy
# %{_prefix}/lib/os-release.snappy
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.snappy


# %files soas
# %{_prefix}/lib/os-release.soas
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.soas


%files workstation
%{_prefix}/lib/os-release.workstation
%attr(0644,root,root) %{_swidtagdir}/org.sgugrseproject.Sgugrse-edition.swidtag.workstation
# Keep this in sync with silverblue above
#%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
#%{_prefix}/lib/systemd/system-preset/80-workstation.preset
#%attr(0644,root,root) %{_prefix}/share/polkit-1/rules.d/org.projectatomic.rpmostree1.rules


# %files xfce
# %{_prefix}/lib/os-release.xfce
# %attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.xfce


%changelog
* Tue Apr 28 2020 Stephen Gallagher <sgallagh@redhat.com> - 31-4
- Enable sa-update.timer

* Wed Mar 18 2020 Stephen Gallagher <sgallagh@redhat.com> - 31-3
- Reset eclipse module (rhbz#1780827)

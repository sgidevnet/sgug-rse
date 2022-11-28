%define release_name Miss Moneypenny
%define dist_version 0.0.7beta
%define bug_version 0.0.7beta

# Change this when branching to fNN
%define doc_version 0.0.7beta

# The package can only be built by a very small number of people
# if you are not sure you can build it do not attempt to

Summary:        SGUG RSE release files
Name:           sgugrse-release
Version:        0.0.7beta
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

Requires:   sgugrse-repos(%{version}) >= 0.0.7beta

%description common
Release files common to all Editions and Spins of SGUG RSE

%prep
#sed -i 's|@@VERSION@@|%{dist_version}|g' %{SOURCE2}

%build

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

# Create the symlink for /etc/os-release
ln -s ../../../usr/sgug/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Install licenses
mkdir -p licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE
#install -pm 0644 %{SOURCE2} licenses/Fedora-Legal-README.txt

# # Default system wide
# install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
# install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
# install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Override the list of enabled gnome-shell extensions for Workstation
# install -Dm0644 %{SOURCE16} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
# install -Dm0644 %{SOURCE17} -t %{buildroot}%{_datadir}/polkit-1/rules.d/

# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%%{bug_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.sgugrseproject.Sgugrse-%{bug_version}.swidtag
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

%changelog
* Wed Dec 16 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7beta-1
- Setting correct release version

* Tue Nov 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7alpha-1
- Building up the support infra for microdnf

* Tue Apr 28 2020 Stephen Gallagher <sgallagh@redhat.com> - 31-4
- Enable sa-update.timer

* Wed Mar 18 2020 Stephen Gallagher <sgallagh@redhat.com> - 31-3
- Reset eclipse module (rhbz#1780827)

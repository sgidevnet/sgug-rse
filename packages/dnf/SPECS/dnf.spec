%global debug 1

%if 0%{debug}
%global __strip /bin/true
%endif

# default dependencies
%global hawkey_version 0.48.0
%global libcomps_version 0.1.8
%global libmodulemd_version 1.4.0
%global rpm_version 4.14.0

# conflicts
%global conflicts_dnf_plugins_core_version 4.0.16
%global conflicts_dnf_plugins_extras_version 4.0.4
%global conflicts_dnfdaemon_version 0.3.19

# override dependencies for rhel 7
%if 0%{?rhel} == 7
    %global rpm_version 4.11.3-32
%endif

%if 0%{?rhel} == 7 && 0%{?centos}
    %global rpm_version 4.11.3-25.el7.centos.1
%endif

# override dependencies for fedora 26
%if 0%{?fedora} == 26
    %global rpm_version 4.13.0.1-7
%endif


#%%if 0%%{?rhel} && 0%%{?rhel} <= 7
#%%bcond_with python3
#%%else
%bcond_without python3
#%%endif

#%%if 0%%{?rhel} >= 8 || 0%%{?fedora} > 29
## Disable python2 build
%bcond_with python2
#%%else
#%%bcond_without python2
#%%endif

# YUM compat subpackage configuration
#
# level=full    -> deploy all compat symlinks (conflicts with yum < 4)
# level=minimal -> deploy a subset of compat symlinks only
#                  (no conflict with yum >= 3.4.3-505)*
# level=preview -> minimal level with altered paths (no conflict with yum < 4)
# *release 505 renamed /usr/bin/yum to /usr/bin/yum-deprecated
# %%global yum_compat_level full
# %%global yum_subpackage_name yum
# %%if 0%%{?fedora}
#     # Avoid file conflict with yum < 4 in all Fedoras
#     # It can be resolved by pretrans scriptlet but they are not recommended in Fedora
#     %%global yum_compat_level minimal
#     %%if 0%%{?fedora} < 31
#         # Avoid name conflict with yum < 4
#         %%global yum_subpackage_name %%{name}-yum
#     %%endif
# %%endif
# %%if 0%%{?rhel} && 0%%{?rhel} <= 7
#     %%global yum_compat_level preview
#     %%global yum_subpackage_name nextgen-yum4
# %%endif
%global yum_compat_level minimal
%global yum_subpackage_name yum

# paths
%global confdir %{_sysconfdir}/%{name}
%global pluginconfpath %{confdir}/plugins

%if %{with python2}
    %global py2pluginpath %{python2_sitelib}/%{name}-plugins
%endif

%if %{with python3}
    %global py3pluginpath %{python3_sitelib}/%{name}-plugins
%endif

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}


%global pkg_summary     Package manager
%global pkg_description Utility that allows users to manage packages on their systems. \
It supports RPMs, modules and comps groups & environments.

Name:           dnf
Version:        4.2.23
Release:        1%{?dist}
Summary:        %{pkg_summary}
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:        GPLv2+ and GPLv2 and GPL
URL:            https://github.com/rpm-software-management/dnf
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  gettext
# Documentation
#BuildRequires:  systemd
BuildRequires:  bash-completion
%if %{with python3}
BuildRequires:  %{_bindir}/sphinx-build-3
Requires:       python3-%{name} = %{version}-%{release}
%else
BuildRequires:  %{_bindir}/sphinx-build
Requires:       python2-%{name} = %{version}-%{release}
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       python-dbus
Requires:       %{_bindir}/sqlite3
%else
%if %{with python3}
Recommends:     (python3-dbus if NetworkManager)
%else
Recommends:     (python2-dbus if NetworkManager)
%endif
Recommends:     (%{_bindir}/sqlite3 if bash-completion)
%endif
Provides:       dnf-command(alias)
Provides:       dnf-command(autoremove)
Provides:       dnf-command(check-update)
Provides:       dnf-command(clean)
Provides:       dnf-command(distro-sync)
Provides:       dnf-command(downgrade)
Provides:       dnf-command(group)
Provides:       dnf-command(history)
Provides:       dnf-command(info)
Provides:       dnf-command(install)
Provides:       dnf-command(list)
Provides:       dnf-command(makecache)
Provides:       dnf-command(mark)
Provides:       dnf-command(provides)
Provides:       dnf-command(reinstall)
Provides:       dnf-command(remove)
Provides:       dnf-command(repolist)
Provides:       dnf-command(repoquery)
Provides:       dnf-command(repository-packages)
Provides:       dnf-command(search)
Provides:       dnf-command(updateinfo)
Provides:       dnf-command(upgrade)
Provides:       dnf-command(upgrade-to)
Conflicts:      python2-dnf-plugins-core < %{conflicts_dnf_plugins_core_version}
Conflicts:      python3-dnf-plugins-core < %{conflicts_dnf_plugins_core_version}
Conflicts:      python2-dnf-plugins-extras-common < %{conflicts_dnf_plugins_extras_version}
Conflicts:      python3-dnf-plugins-extras-common < %{conflicts_dnf_plugins_extras_version}

%description
%{pkg_description}

%package data
Summary:        Common data and configuration files for DNF
#Requires:       libreport-filesystem
Obsoletes:      %{name}-conf <= %{version}-%{release}
Provides:       %{name}-conf = %{version}-%{release}

%description data
Common data and configuration files for DNF

%package -n %{yum_subpackage_name}
Requires:       %{name} = %{version}-%{release}
Summary:        %{pkg_summary}
%if 0%{?fedora}
%if 0%{?fedora} >= 31
Provides:       %{name}-yum = %{version}-%{release}
Obsoletes:      %{name}-yum < 5
%else
Conflicts:      yum < 3.4.3-505
%endif
%endif

%description -n %{yum_subpackage_name}
%{pkg_description}

%if %{with python2}
%package -n python2-%{name}
Summary:        Python 2 interface to DNF
%{?python_provide:%python_provide python2-%{name}}
BuildRequires:  python2-devel
BuildRequires:  python2-hawkey >= %{hawkey_version}
BuildRequires:  python2-libdnf >= %{hawkey_version}
BuildRequires:  python2-libcomps >= %{libcomps_version}
BuildRequires:  python2-libdnf
BuildRequires:  python2-nose
BuildRequires:  libmodulemd >= %{libmodulemd_version}
Requires:       libmodulemd >= %{libmodulemd_version}
%if (0%{?rhel} && 0%{?rhel} <= 7)
BuildRequires:  pygpgme
Requires:       pygpgme
BuildRequires:  python-enum34
Requires:       python-enum34
%else
BuildRequires:  python2-gpg
Requires:       python2-gpg
BuildRequires:  python2-enum34
Requires:       python2-enum34
%endif
Requires:       %{name}-data = %{version}-%{release}
%if 0%{?fedora}
Recommends:     deltarpm
# required for DNSSEC main.gpgkey_dns_verification https://dnf.readthedocs.io/en/latest/conf_ref.html
Recommends:     python2-unbound
%endif
Requires:       python2-hawkey >= %{hawkey_version}
Requires:       python2-libdnf >= %{hawkey_version}
Requires:       python2-libcomps >= %{libcomps_version}
Requires:       python2-libdnf
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  rpm-python >= %{rpm_version}
Requires:       rpm-python >= %{rpm_version}
%else
BuildRequires:  python2-rpm >= %{rpm_version}
Requires:       python2-rpm >= %{rpm_version}
#Recommends:     rpm-plugin-systemd-inhibit
%endif
Conflicts:      dnfdaemon < %{conflicts_dnfdaemon_version}

%description -n python2-%{name}
Python 2 interface to DNF.
%endif
# ^ %%{with python2}

%if %{with python3}
%package -n python3-%{name}
Summary:        Python 3 interface to DNF
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-hawkey >= %{hawkey_version}
BuildRequires:  python3-libdnf >= %{hawkey_version}
BuildRequires:  python3-libcomps >= %{libcomps_version}
BuildRequires:  python3-libdnf
BuildRequires:  libmodulemd >= %{libmodulemd_version}
Requires:       libmodulemd >= %{libmodulemd_version}
BuildRequires:  python3-nose
BuildRequires:  python3-gpg
Requires:       python3-gpg
Requires:       %{name}-data = %{version}-%{release}
%if 0%{?fedora}
Recommends:     deltarpm
%endif
Requires:       python3-hawkey >= %{hawkey_version}
Requires:       python3-libdnf >= %{hawkey_version}
Requires:       python3-libcomps >= %{libcomps_version}
Requires:       python3-libdnf
BuildRequires:  python3-rpm >= %{rpm_version}
Requires:       python3-rpm >= %{rpm_version}
# required for DNSSEC main.gpgkey_dns_verification https://dnf.readthedocs.io/en/latest/conf_ref.html
Recommends:     python3-unbound
#%%if 0%%{?rhel} && 0%%{?rhel} <= 7
#Requires:       rpm-plugin-systemd-inhibit
#%%else
#Recommends:     rpm-plugin-systemd-inhibit
#%%endif

%description -n python3-%{name}
Python 3 interface to DNF.
%endif

#%%package automatic
#Summary:        %%{pkg_summary} - automated upgrades
#BuildRequires:  systemd
#Requires:       %%{name} = %%{version}-%%{release}
#%%{?systemd_requires}
#
#%%description automatic
#Systemd units that can periodically download package upgrades and apply them.


%prep
%autosetup -p1
mkdir build-py2
mkdir build-py3

# Rewrite hardcoded sysconfdir
perl -pi -e "s|SYSCONFDIR /etc|SYSCONFDIR  %{_sysconfdir}|g" CMakeLists.txt

%build
export TOP_WD=`pwd`
%if %{with python2}
    cd build-py2
    %cmake .. -DPYTHON_DESIRED:FILEPATH=%{__python2} -DDNF_VERSION=%{version}
    %make_build
    make doc-man
    cd $TOP_WD
%endif

%if %{with python3}
    cd build-py3
    %cmake .. -DPYTHON_DESIRED:FILEPATH=%{__python3} -DDNF_VERSION=%{version}
    %make_build
    make doc-man
    cd $TOP_WD
%endif


%install
rm -rf $RPM_BUILD_ROOT
export TOP_WD=`pwd`
%if %{with python2}
    cd build-py2
    %make_install
    cd $TOP_WD
%endif

%if %{with python3}
    cd build-py3
    %make_install
    cd $TOP_WD
%endif

%find_lang %{name}
mkdir -p %{buildroot}%{confdir}/vars
mkdir -p %{buildroot}%{confdir}/aliases.d
mkdir -p %{buildroot}%{pluginconfpath}/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules.defaults.d
%if %{with python2}
mkdir -p %{buildroot}%{py2pluginpath}/
%endif
%if %{with python3}
mkdir -p %{buildroot}%{py3pluginpath}/__pycache__/
%endif
mkdir -p %{buildroot}%{_localstatedir}/log/
mkdir -p %{buildroot}%{_var}/cache/dnf/
touch %{buildroot}%{_localstatedir}/log/%{name}.log
%if %{with python3}
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf
mv %{buildroot}%{_bindir}/dnf-automatic-3 %{buildroot}%{_bindir}/dnf-automatic
%else
ln -sr %{buildroot}%{_bindir}/dnf-2 %{buildroot}%{_bindir}/dnf
mv %{buildroot}%{_bindir}/dnf-automatic-2 %{buildroot}%{_bindir}/dnf-automatic
%endif
rm -vf %{buildroot}%{_bindir}/dnf-automatic-*

# Strict conf distribution
%if 0%{?rhel}
mv -f %{buildroot}%{confdir}/%{name}-strict.conf %{buildroot}%{confdir}/%{name}.conf
%else
rm -vf %{buildroot}%{confdir}/%{name}-strict.conf
%endif

# YUM compat layer
ln -sr  %{buildroot}%{confdir}/%{name}.conf %{buildroot}%{_sysconfdir}/yum.conf
%if %{with python3}
ln -sr  %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/yum
%else
%if "%{yum_compat_level}" == "preview"
ln -sr  %{buildroot}%{_bindir}/dnf-2 %{buildroot}%{_bindir}/yum4
ln -sr  %{buildroot}%{_mandir}/man8/dnf.8.gz %{buildroot}%{_mandir}/man8/yum4.8.gz
rm -f %{buildroot}%{_mandir}/man8/yum.8.gz
%else
ln -sr  %{buildroot}%{_bindir}/dnf-2 %{buildroot}%{_bindir}/yum
%endif
%endif
%if "%{yum_compat_level}" == "full"
mkdir -p %{buildroot}%{_sysconfdir}/yum
ln -sr  %{buildroot}%{pluginconfpath} %{buildroot}%{_sysconfdir}/yum/pluginconf.d
ln -sr  %{buildroot}%{confdir}/protected.d %{buildroot}%{_sysconfdir}/yum/protected.d
ln -sr  %{buildroot}%{confdir}/vars %{buildroot}%{_sysconfdir}/yum/vars
%endif

# Remove systemd things we aren't interested in
rm -rf $RPM_BUILD_ROOT/usr/lib
rm -rf $RPM_BUILD_ROOT%{_bindir}/dnf-automatic
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/dnf/automatic.conf
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/libreport/events.d/collect_dnf.conf
rm -rf $RPM_BUILD_ROOT%{_mandir}/man8/dnf-automatic*

%check
export TOP_WD=`pwd`
%if %{with python2}
    cd build-py2
    ctest -VV
    cd $TOP_WD
%endif

%if %{with python3}
    cd build-py3
    ctest -VV
    cd $TOP_WD
%endif


#%%post
#%%systemd_post dnf-makecache.timer

#%%preun
#%%systemd_preun dnf-makecache.timer

#%%postun
#%%systemd_postun_with_restart dnf-makecache.timer


#%%post automatic
#%%systemd_post dnf-automatic.timer
#%%systemd_post dnf-automatic-notifyonly.timer
#%%systemd_post dnf-automatic-download.timer
#%%systemd_post dnf-automatic-install.timer

#%%preun automatic
#%%systemd_preun dnf-automatic.timer
#%%systemd_preun dnf-automatic-notifyonly.timer
#%%systemd_preun dnf-automatic-download.timer
#%%systemd_preun dnf-automatic-install.timer

#%%postun automatic
#%%systemd_postun_with_restart dnf-automatic.timer
#%%systemd_postpun_with_restart dnf-automatic-notifyonly.timer
#%%systemd_postun_with_restart dnf-automatic-download.timer
#%%systemd_postun_with_restart dnf-automatic-install.timer


%files -f %{name}.lang
%{_bindir}/%{name}
%if 0%{?rhel} && 0%{?rhel} <= 7
%{_sysconfdir}/bash_completion.d/%{name}
%else
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%endif
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/yum2dnf.8*
%{_mandir}/man7/dnf.modularity.7*
#%%{_unitdir}/%%{name}-makecache.service
#%%{_unitdir}/%%{name}-makecache.timer
%{_var}/cache/%{name}/

%files data
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%dir %{confdir}
%dir %{confdir}/modules.d
%dir %{confdir}/modules.defaults.d
%dir %{pluginconfpath}
%dir %{confdir}/protected.d
%dir %{confdir}/vars
%dir %{confdir}/aliases.d
%exclude %{confdir}/aliases.d/zypper.conf
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/protected.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(644,-,-) %{_localstatedir}/log/hawkey.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.librepo.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.rpm.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.plugin.log
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}
%ghost %attr(644,-,-) %{_sharedstatedir}/%{name}/groups.json
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}/yumdb
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}/history
%{_mandir}/man5/%{name}.conf.5*
#%%{_tmpfilesdir}/%%{name}.conf
#%%{_sysconfdir}/libreport/events.d/collect_dnf.conf

%files -n %{yum_subpackage_name}
%if "%{yum_compat_level}" == "full"
%{_bindir}/yum
%{_sysconfdir}/yum.conf
%{_sysconfdir}/yum/pluginconf.d
%{_sysconfdir}/yum/protected.d
%{_sysconfdir}/yum/vars
%{_mandir}/man8/yum.8*
%{_mandir}/man5/yum.conf.5.*
%{_mandir}/man8/yum-shell.8*
%{_mandir}/man1/yum-aliases.1*
%config(noreplace) %{confdir}/protected.d/yum.conf
%else
%exclude %{_sysconfdir}/yum.conf
%exclude %{_sysconfdir}/yum/pluginconf.d
%exclude %{_sysconfdir}/yum/protected.d
%exclude %{_sysconfdir}/yum/vars
%exclude %{confdir}/protected.d/yum.conf
%exclude %{_mandir}/man5/yum.conf.5.*
%exclude %{_mandir}/man8/yum-shell.8*
%exclude %{_mandir}/man1/yum-aliases.1*
%endif

%if "%{yum_compat_level}" == "minimal"
%{_bindir}/yum
%{_mandir}/man8/yum.8*
%endif

%if "%{yum_compat_level}" == "preview"
%{_bindir}/yum4
%{_mandir}/man8/yum4.8*
%exclude %{_mandir}/man8/yum.8*
%endif

%if %{with python2}
%files -n python2-%{name}
%{_bindir}/%{name}-2
%exclude %{python2_sitelib}/%{name}/automatic
%{python2_sitelib}/%{name}/
%dir %{py2pluginpath}
%endif

%if %{with python3}
%files -n python3-%{name}
%{_bindir}/%{name}-3
%exclude %{python3_sitelib}/%{name}/automatic
%{python3_sitelib}/%{name}/
%dir %{py3pluginpath}
%dir %{py3pluginpath}/__pycache__
%endif

#%%files automatic
#%%{_bindir}/%%{name}-automatic
#%%config(noreplace) %%{confdir}/automatic.conf
#%%{_mandir}/man8/%%{name}-automatic.8*
#%%{_unitdir}/%%{name}-automatic.service
#%%{_unitdir}/%%{name}-automatic.timer
#%%{_unitdir}/%%{name}-automatic-notifyonly.service
#%%{_unitdir}/%%{name}-automatic-notifyonly.timer
#%%{_unitdir}/%%{name}-automatic-download.service
#%%{_unitdir}/%%{name}-automatic-download.timer
#%%{_unitdir}/%%{name}-automatic-install.service
#%%{_unitdir}/%%{name}-automatic-install.timer
#%%if %%{with python3}
#%%{python3_sitelib}/%%{name}/automatic/
#%%else
#%%{python2_sitelib}/%%{name}/automatic/
#%%endif

%changelog
* Tue Nov 10 2020 Daniel Hams <daniel.hams@gmail.com> - 4.2.23-1
- Import broken package into sgug-rse

* Tue Jun 02 2020 Nicola Sella <nsella@redhat.com> - 4.2.23-1
- Fix behavior of install-n, autoremove-n, remove-n, repoquery-n
- Fix behavior of localinstall and list-updateinfo aliases
- Add updated field to verbose output of updateinfo list (RhBug: 1801092)
- Add comment option to transaction (RhBug:1773679)
- Add new API for handling gpg signatures (RhBug:1339617)
- Verify GPG signatures when running dnf-automatic (RhBug:1793298)
- Fix up Conflicts: on python-dnf-plugins-extras
- [doc] Move yum-plugin-post-transaction-actions to dnf-plugins-core
- Remove args "--set-enabled", "--set-disabled" from DNF (RhBug:1727882)
- Search command is now alphabetical (RhBug:1811802)
- Fix downloading packages with full URL as their location
- repo: catch libdnf.error.Error in addition to RuntimeError in load() (RhBug:1788182)
- History table to max size when redirect to file (RhBug:1786335,1786316)

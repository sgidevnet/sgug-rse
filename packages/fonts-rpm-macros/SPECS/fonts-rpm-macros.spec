# SPDX-License-Identifier: MIT
%global forgeurl  https://pagure.io/fonts-rpm-macros
Version: 2.0.3
%forgemeta

#https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/51
%global _spectemplatedir %{_datadir}/rpmdevtools/sgug
%global _docdir_fmt     %{name}
%global ftcgtemplatedir %{_datadir}/fontconfig/templates

# Master definition that will be written to macro files
%global _fontbasedir            %{_datadir}/fonts
%global _fontconfig_masterdir   %{_sysconfdir}/fonts
%global _fontconfig_confdir     %{_sysconfdir}/fonts/conf.d
%global _fontconfig_templatedir %{_datadir}/fontconfig/conf.avail

BuildArch: noarch

Name:      fonts-rpm-macros
Release:   2%{?dist}
Summary:   Build-stage rpm automation for fonts packages

License:   GPLv3+
URL:       https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Source:    %{forgesource}

Requires:  fonts-srpm-macros = %{version}-%{release}
Requires:  fonts-filesystem  = %{version}-%{release}

Provides:  fontpackages-devel = %{version}-%{release}
Obsoletes: fontpackages-devel < %{version}-%{release}
# Tooling dropped for now as no one was willing to maintain it
Obsoletes: fontpackages-tools < %{version}-%{release}

Requires:  fontconfig
#Requires:  libappstream-glib
Requires:  uchardet

# For the experimental generator
Requires:  python3-ruamel-yaml
Requires:  python3-lxml

%description
This package provides build-stage rpm automation to simplify the creation of
fonts packages.

It does not need to be included in the default build root: fonts-srpm-macros
will pull it in for fonts packages only.

%package -n fonts-srpm-macros
Summary:   Source-stage rpm automation for fonts packages
Requires:  redhat-rpm-config

%description -n fonts-srpm-macros
This package provides SRPM-stage rpm automation to simplify the creation of
fonts packages.

It limits itself to the automation subset required to create fonts SRPM
packages and needs to be included in the default build root.

The rest of the automation is provided by the fonts-rpm-macros package, that
fonts-srpm-macros will pull in for fonts packages only.

%package -n fonts-filesystem
Summary:   Directories used by font packages
License:   MIT

Provides:  fontpackages-filesystem = %{version}-%{release}
Obsoletes: fontpackages-filesystem < %{version}-%{release}

%description -n fonts-filesystem
This package contains the basic directory layout used by font packages,
including the correct permissions for the directories.

%package -n fonts-rpm-templates
Summary:   Example fonts packages rpm spec templates
License:   MIT

Requires:    fonts-rpm-macros = %{version}-%{release}
Supplements: fonts-rpm-macros = %{version}-%{release}

%description -n fonts-rpm-templates
This package contains documented rpm spec templates showcasing how to use the
macros provided by fonts-rpm-macros to create fonts packages.

%prep
%forgesetup
%writevars -f rpm/macros.d/macros.fonts-srpm _fontbasedir _fontconfig_masterdir _fontconfig_confdir _fontconfig_templatedir
for template in templates/rpm/*\.spec ; do
  target=$(echo "${template}" | sed "s|^\(.*\)\.spec$|\1-bare.spec|g")
  grep -v '^#' "${template}" > "${target}"
  touch -r "${template}" "${target}"
done

# Fix up some hardcoded paths
perl -pi -e "s|/usr/bin/python|%{_bindir}/python|g" bin/fc-weight
perl -pi -e "s|/usr/bin/python|%{_bindir}/python|g" bin/gen-fontconf

%install
install -m 0755 -d    %{buildroot}%{_fontbasedir} \
                      %{buildroot}%{_fontconfig_masterdir} \
                      %{buildroot}%{_fontconfig_confdir} \
                      %{buildroot}%{_fontconfig_templatedir}

install -m 0755 -vd   %{buildroot}%{_spectemplatedir}
install -m 0644 -vp   templates/rpm/*spec \
                      %{buildroot}%{_spectemplatedir}
install -m 0755 -vd   %{buildroot}%{ftcgtemplatedir}
install -m 0644 -vp   templates/fontconfig/*{conf,txt} \
                      %{buildroot}%{ftcgtemplatedir}

install -m 0755 -vd   %{buildroot}%{rpmmacrodir}
install -m 0644 -vp   rpm/macros.d/macros.fonts-* \
                      %{buildroot}%{rpmmacrodir}
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0644 -vp   rpm/lua/srpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/rpm
install -m 0644 -vp   rpm/lua/rpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/rpm

install -m 0755 -vd   %{buildroot}%{_bindir}
install -m 0755 -vp   bin/* %{buildroot}%{_bindir}

# For now remove the files that should be in the RPMs we can't yet use
# due to more python madness.
#rm $RPM_BUILD_ROOT%{_bindir}/*
#rm $RPM_BUILD_ROOT%{rpmmacrodir}/macros.fonts-rpm*
#rm $RPM_BUILD_ROOT%{_rpmluadir}/fedora/rpm/*.lua
#rm $RPM_BUILD_ROOT/LICENSE-templates.txt
#rm $RPM_BUILD_ROOT/ *.md changelog.txt
rm $RPM_BUILD_ROOT%{_spectemplatedir}/*.spec
rm $RPM_BUILD_ROOT%{ftcgtemplatedir}/*conf
rm $RPM_BUILD_ROOT%{ftcgtemplatedir}/*txt

%files
%license LICENSE.txt
%{_bindir}/*
%{rpmmacrodir}/macros.fonts-rpm*
%{_rpmluadir}/fedora/rpm/*.lua

%files -n fonts-srpm-macros
%license LICENSE.txt
%doc     *.md changelog.txt
%{rpmmacrodir}/macros.fonts-srpm*
%{_rpmluadir}/fedora/srpm/*.lua

%files -n fonts-filesystem
%dir %{_datadir}/fontconfig
%dir %{_fontbasedir}
%dir %{_fontconfig_masterdir}
%dir %{_fontconfig_confdir}
%dir %{_fontconfig_templatedir}

#%files -n fonts-rpm-templates
#%license LICENSE-templates.txt
#%doc     *.md changelog.txt
#%{_spectemplatedir}/*.spec
#%dir %{ftcgtemplatedir}
#%doc %{ftcgtemplatedir}/*conf
#%doc %{ftcgtemplatedir}/*txt

%changelog
* Sun Aug 16 2020 Daniel Hams <daniel.hams@gmail.com> - 2.0.3-2
- Re-enable the rpm-macros package

* Mon Apr 13 2020 Daniel Hams <daniel.hams@gmail.com> - 2.0.3-1
- Import into wip, disable packages needing tree of python deps

* Sat Feb 29 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.3-1
✅ minor rpmlint-oriented fixlets

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-1
✅ improve experimental fontconfig configuration generator

* Thu Feb 20 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.1-3
✅ limit descriptions to 80 columns

* Fri Feb 14 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.1-2
✅ use fonts packaging guidelines as URL
- 2.0.1-1
✅ first 2.x version proposed to Fedora, after FPC approval
   https://meetbot-raw.fedoraproject.org/fedora-meeting-1/2020-02-13/fpc.2020-02-13-17.00.txt

* Mon Nov 11 2019 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.0-1
✅ transform into fonts-rpm-macros
✅ major rpm macro and rpm spec template rework


* Mon Nov 10 2008 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0-1
✅ initial release

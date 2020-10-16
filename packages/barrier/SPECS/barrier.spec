%global barrier_revision 8941e56f
Summary: Keyboard and mouse sharing solution
Name: barrier
Version: 2.3.3
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: https://github.com/debauchee/barrier
# This source is a lie, I used 43708ae0d636539f5d9627133baba7cce3ea0812 from github
Source0: https://github.com/debauchee/barrier/archive/barrier-v%{version}.tar.gz
Patch100: barrier.sgifixes.patch


BuildRequires: cmake3
#BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: libX11-devel
#BuildRequires: libXtst-devel
#BuildRequires: qt5-qtbase-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: openssl-devel

%description
Barrier allows you to share one mouse and keyboard between multiple computers.
Work seamlessly across Windows, macOS and Linux.

%prep
%setup -q -n %{name}-%{version}
%patch100 -p1 -b .sgifixes

%build
%{cmake3} -DSYNERGY_VERSION_STAGE:STRING=release -DSYNERGY_REVISION:STRING=%{barrier_revision} .
make %{?_smp_mflags}


%install
# no GUI for you
# install -D -p -m 0755 bin/barrier %{buildroot}%{_bindir}/barrier
install -D -p -m 0755 bin/barrierc %{buildroot}%{_bindir}/barrierc
install -D -p -m 0755 bin/barriers %{buildroot}%{_bindir}/barriers
install -D -p -m 0644 doc/barrierc.1 %{buildroot}%{_mandir}/man1/barrierc.1
install -D -p -m 0644 doc/barriers.1 %{buildroot}%{_mandir}/man1/barriers.1
install -D -p -m 0644 res/barrier.desktop %{buildroot}%{_datadir}/applications/barrier.desktop
install -D -p -m 0644 res/barrier.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/barrier.svg

cd %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/metainfo
## Write AppStream
cat <<END> %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2018 Ding-Yi Chen <dchen@redhat.com> -->
<component type="desktop-application">
  <id>%{name}</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPLv2</project_license>
  <name>barrier</name>
  <summary>Share mouse and keyboard between multiple computers over the network</summary>

  <description>
    <p>
      Barrier allows you to share one mouse and keyboard between multiple computers.
      Work seamlessly across Windows, macOS and Linux.
    </p>
  </description>

  <launchable type="desktop-id">%{name}.desktop</launchable>

  <url type="homepage">https://github.com/debauchee/barrier</url>

  <provides>
    <binary>barrier</binary>
    <binary>barrierc</binary>
    <binary>barriers</binary>
  </provides>

  <releases>
    <release version="%{version}" date="2019-03-21" />
  </releases>
</component>
END

#desktop-file-install --delete-original \
#  --dir %{buildroot}%{_datadir}/applications \
#  --set-icon=%{_datadir}/icons/hicolor/scalable/apps/barrier.svg \
#  %{buildroot}%{_datadir}/applications/barrier.desktop
#
#desktop-file-validate %{buildroot}/%{_datadir}/applications/barrier.desktop

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%doc LICENSE ChangeLog res/Readme.txt doc/barrier.conf.example*
#%{_bindir}/barrier
%{_bindir}/barrierc
%{_bindir}/barriers
%{_datadir}/icons/hicolor/scalable/apps/barrier.svg
%{_datadir}/applications/barrier.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/barrierc.1*
%{_mandir}/man1/barriers.1*

%changelog
* Thu Mar 21 2019 wendall911 <wendallc@83864.com>
- Actual working spec file for Fedora

* Sat Jan 27 2018 Debauchee <todo@mail.com>
- Initial version of the package


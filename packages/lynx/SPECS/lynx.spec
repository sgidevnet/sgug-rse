%global devrel 1

Summary: A text-based Web browser
Name: lynx
Version: 2.8.9
Release: 6%{?dist}
License: GPLv2
Source: https://invisible-mirror.net/archives/lynx/tarballs/lynx%{version}rel.%{devrel}.tar.bz2
URL: http://lynx.browser.org/

# RH specific tweaks - directory layout, utf-8 by default, misc. configuration
Patch0: lynx-2.8.9-redhat.patch

# patch preparing upstream sources for rpmbuild, in particular for parallel make
Patch1: lynx-2.8.9-build.patch

# prompt user before executing command via a lynxcgi link even in advanced mode,
# as the actual URL may not be shown but hidden behind an HTTP redirect and set
# TRUSTED_LYNXCGI:none in lynx.cfg to disable all lynxcgi URLs by default
# [CVE-2008-4690]
Patch2: lynx-CVE-2008-4690.patch

# avoid build failure caused by mistakenly excluded <locale.h>
Patch3: lynx-2.8.8-locale.patch

# fix bugs detected by static analysis
Patch4: lynx-2.8.9-static-analysis.patch

Provides: webclient
Provides: text-www-browser
BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
#BuildRequires: slang-devel
#BuildRequires: telnet
BuildRequires: unzip
BuildRequires: zip
BuildRequires: zlib-devel

# provides /usr/share/doc/HTML/en-US/index.html used as STARTFILE on RHEL
%if 0%{?rhel}
Requires: redhat-indexhtml
%endif

%description
Lynx is a text-based Web browser. Lynx does not display any images,
but it does support frames, tables, and most other HTML tags. One
advantage Lynx has over graphical browsers is speed; Lynx starts and
exits quickly and swiftly displays web pages.

%prep
%setup -q -n lynx2.8.9rel.%{devrel}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
sed -e "s,^HELPFILE:.*,HELPFILE:file://localhost%{_pkgdocdir}/lynx_help/lynx_help_main.html,g" -i lynx.cfg
%if 0%{?rhel}
sed -e 's,^STARTFILE:.*,STARTFILE:file:%{_datadir}/doc/HTML/en-US/index.html,' -i lynx.cfg
%endif

%build
#autoreconf -fi
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" configure
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" config.guess
perl -pi -e "s|/bin/sh|%{_bindir}/bash|g" config.sub
export SHELL=%{_bindir}/bash
export SHELL_PATH="$SHELL"
export CONFIG_SHELL="$SHELL"
%configure --libdir=%{_sysconfdir}            \
    --disable-font-switch           \
    --disable-rpath-hack            \
    --enable-addrlist-page          \
    --enable-charset-choice         \
    --enable-cgi-links              \
    --enable-cjk                    \
    --enable-debug                  \
    --enable-default-colors         \
    --enable-externs                \
    --enable-file-upload            \
    --enable-internal-links         \
    --enable-ipv6                   \
    --enable-japanese-utf8          \
    --enable-justify-elts           \
    --enable-locale-charset         \
    --enable-kbd-layout             \
    --enable-libjs                  \
    --enable-nls                    \
    --enable-nsl-fork               \
    --enable-persistent-cookies     \
    --enable-prettysrc              \
    --enable-read-eta               \
    --enable-scrollbar              \
    --enable-source-cache           \
    --enable-warnings               \
    --with-screen=ncurses           \
    --with-ssl=%{_libdir}           \
    --with-zlib                     \
    ac_cv_path_RLOGIN=/usr/bsd/rlogin

make -C po
make %{?_smp_mflags}

# remove zero-length tests files to silence rpmlint
rm -fv test/X test/nobody

%install
chmod -x samples/mailto-form.pl
make install DESTDIR=$RPM_BUILD_ROOT

# remove unneeded files with incompatible encoding
rm -f docs/{OS-390.announce,README.jp}
rm -f samples/*.bat

# convert line endings
dos2unix samples/lynx-demo.cfg
dos2unix samples/midnight.lss

# Install Lang dependent resources
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/ja/LC_MESSAGES/

cat >$RPM_BUILD_ROOT%{_sysconfdir}/lynx-site.cfg <<EOF
# Place any local lynx configuration options (proxies etc.) here.
EOF

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc docs README INSTALLATION samples
%doc test lynx.hlp lynx_help
%{_bindir}/lynx
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/lynx.cfg
%config(noreplace) %{_sysconfdir}/lynx.lss
%config(noreplace,missingok) %{_sysconfdir}/lynx-site.cfg

%changelog
* Mon Jun 01 2020 Daniel Hams <daniel.hams@gmail.com> - 2.8.9-6
- Import into wip

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kamil Dudka <kdudka@redhat.com> - 2.8.9-5
- include license file in the package (#1686886)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Kamil Dudka <kdudka@redhat.com> - 2.8.9-3
- fix bugs detected by static analysis

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

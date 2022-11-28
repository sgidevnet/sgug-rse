Summary: A GUI text editor for systems with X
Name: nedit
Version: 5.7
Release: 8%{?dist}
Source: http://sourceforge.net/projects/nedit/files/nedit-source/nedit-%{version}-src.tar.gz
Source1: nedit.desktop
Source2: nedit-icon.png
Patch0: nedit-5.5-security.patch
# https://sourceforge.net/p/nedit/git/ci/838292fe4034fc4ab4567f1d87193a4e6a57eca0/
Patch1: 0001-Force-C89-on-gcc-linux-to-prevent-accidental-changes.patch
# Append to Fedora's C_OPT_FLAGS and LD_OPT_FLAGS rather than overriding them.
Patch2: nedit-5.7-makefiles.patch
Patch3: nedit-5.6-utf8.patch
Patch5: nedit-5.7-nc-manfix.patch
Patch6: nedit-5.5-visfix.patch
Patch8: nedit-5.5-scroll.patch

Patch100: nedit.sgifixes.patch

URL: http://nedit.org
License: GPLv2
Requires: xorg-x11-fonts-ISO8859-1-75dpi
BuildRequires:  gcc
BuildRequires: motif-devel, libXau-devel, libXpm-devel, libXmu-devel
BuildRequires: desktop-file-utils
# Needed for generating manpages; see doc/Makefile
BuildRequires: perl(Pod::Man)

%description
NEdit is a GUI text editor for the X Window System. NEdit is
very easy to use, especially if you are familiar with the
Macintosh or Microsoft Windows style of interface.

%prep
%setup -q
%patch0 -p1 -b .security
%patch1 -p1 -b .c89
%patch2 -p1 -b .makefiles
%patch3 -p1 -b .utf8
%patch5 -p1 -b .nc-manfix
%patch6 -p1 -b .visfix
%patch8 -p1 -b .scroll

%patch100 -p1 -b .sgifixes

# A place to generate the sgug patch
#exit 1

%build
export PREV_WD=`pwd`
cd doc
# Upstream really doesn't want you generating the manpages, but they forgot to
# include the manpages in 5.7. So generate them.
make VERSION='NEdit 5.7' man
cd $PREV_WD
#make linux C_OPT_FLAGS="$RPM_OPT_FLAGS"
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
make %{_smp_mflags} irix C_OPT_FLAGS="$RPM_OPT_FLAGS" LD_OPT_FLAGS="$LDFLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
mv source/nc source/nedit-client
install -m 755 source/nedit source/nedit-client $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 doc/nedit.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit.1x
mv doc/nc.man doc/nedit-client.man
install -p -m 644 doc/nedit-client.man $RPM_BUILD_ROOT%{_mandir}/man1/nedit-client.1x

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/nedit.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category "Development;" \
        %{SOURCE1}

%files
%doc README ReleaseNotes
%{_mandir}/*/*
%{_bindir}/*
%{_prefix}/share/applications/*
%{_datadir}/icons/hicolor/

%changelog
* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 5.7-8
- Rebuild for jpegturbo

* Sat Jul 04 2020 Daniel Hams <daniel.hams@gmail.com> - 5.7-7
- Pull into wip

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

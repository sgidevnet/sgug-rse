
Name:    pinentry
Version: 1.1.0
Release: 6%{?dist}
Summary: Collection of simple PIN or passphrase entry dialogs

License: GPLv2+
URL:     http://www.gnupg.org/aegypten/
Source0: ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2.sig

# borrowed from opensuse
Source10: pinentry-wrapper

BuildRequires: gcc
BuildRequires: gcr-devel
BuildRequires: gtk2-devel
#BuildRequires: libcap-devel
BuildRequires: ncurses-devel
BuildRequires: libgpg-error-devel
BuildRequires: libassuan-devel
BuildRequires: libsecret-devel
#BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)

Requires(pre): %{_sbindir}/update-alternatives

Provides: %{name}-curses = %{version}-%{release}

%description
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the curses (text) based version of the PIN entry dialog.

#%%package gnome3
#Summary: Passphrase/PIN entry dialog for GNOME 3
#Requires: %%{name} = %%{version}-%%{release}
#Provides: %%{name}-gui = %%{version}-%%{release}
#%%description gnome3
#Pinentry is a collection of simple PIN or passphrase entry dialogs which
#utilize the Assuan protocol as described by the aegypten project; see
#http://www.gnupg.org/aegypten/ for details.
#This package contains the GNOME 3 version of the PIN entry dialog.

%package gtk
Summary: Passphrase/PIN entry dialog based on GTK+
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Provides: pinentry-gtk2 = %{version}-%{release}
%description gtk
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GTK GUI based version of the PIN entry dialog.

#%%package qt
#Summary: Passphrase/PIN entry dialog based on Qt5
#Requires: %%{name} = %%{version}-%%{release}
#Provides: %%{name}-gui = %%{version}-%%{release}
#Obsoletes: pinentry-qt4 < 0.8.0-2
#Provides:  pinentry-qt5 = %%{version}-%%{release}
#%description qt
#Pinentry is a collection of simple PIN or passphrase entry dialogs which
#utilize the Assuan protocol as described by the aegypten project; see
#http://www.gnupg.org/aegypten/ for details.
#This package contains the Qt4 GUI based version of the PIN entry dialog.

%package emacs
Summary: Passphrase/PIN entry dialog based on emacs
Requires: %{name} = %{version}-%{release}
%description emacs
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the emacs based version of the PIN entry dialog.

%prep
%setup -q


%build
%configure \
  --disable-dependency-tracking \
  --without-libcap \
  --disable-pinentry-fltk \
  --disable-pinentry-gnome3 \
  --enable-pinentry-gtk2 \
  --disable-pinentry-qt5 \
  --enable-pinentry-emacs \
  --enable-libsecret

#  --disable-rpath \
#

%make_build


%install
%make_install

# Symlink for Backward compatibility
ln -s pinentry-gtk-2 $RPM_BUILD_ROOT%{_bindir}/pinentry-gtk
#ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt4

install -p -m755 -D %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/pinentry

# unpackaged files
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/pinentry-curses
%{_bindir}/pinentry
%{_infodir}/pinentry.info*

#%%files gnome3
#%%{_bindir}/pinentry-gnome3

%files gtk
%{_bindir}/pinentry-gtk-2
# symlink for backward compatibility
%{_bindir}/pinentry-gtk

#%%files qt
#%%{_bindir}/pinentry-qt
## symlink for backward compatibility
#%%{_bindir}/pinentry-qt4

%files emacs
%{_bindir}/pinentry-emacs

%changelog
* Sun Nov 08 2020 Daniel Hams <daniel.hams@gmail.com> - 1.1.0-6
- Import into sgugrse

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

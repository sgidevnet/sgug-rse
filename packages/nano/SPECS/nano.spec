Summary:         A small text editor
Name:            nano
Version:         4.3
Release:         3%{?dist}
License:         GPLv3+
URL:             https://www.nano-editor.org
Source:          https://www.nano-editor.org/dist/latest/%{name}-%{version}.tar.xz
Source2:         nanorc

BuildRequires:   file-devel
BuildRequires:   gettext-devel
BuildRequires:   gcc
BuildRequires:   git
BuildRequires:   groff
BuildRequires:   ncurses-devel
BuildRequires:   sed
BuildRequires:   texinfo
Conflicts:       filesystem < 3

# refresh the edit window when exiting from the help viewer
Patch1: nano-4.3-display-refersh.patch

%description
GNU nano is a small and friendly text editor.

%prep
%autosetup -S git

%build
mkdir build
cd build
export LIBS="-lgen"
%global _configure ../configure --disable-utf8
%configure
make %{?_smp_mflags}

# generate default /etc/nanorc
# - disable line wrapping by default
# - set hunspell as the default spell-checker
# - enable syntax highlighting by default (#1270712)
sed -e 's/# set nowrap/set nowrap/' \
    -e 's/^#.*set speller.*$/set speller "hunspell"/' \
    -e 's|^# \(include "/usr/share/nano/\*.nanorc"\)|\1|' \
    %{SOURCE2} doc/sample.nanorc > ./nanorc

%install
cd build
%make_install
rm -f %{buildroot}%{_infodir}/dir

# remove installed HTML documentation
rm -f %{buildroot}%{_docdir}/nano/{nano,nano.1,nanorc.5,rnano.1}.html

# install default /etc/nanorc
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 ./nanorc %{buildroot}%{_sysconfdir}/nanorc

%find_lang %{name}

%files -f build/%{name}.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%doc build/doc/sample.nanorc
%doc doc/{faq,nano}.html
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/nanorc
%{_mandir}/man*/*
%{_infodir}/nano.info*
%{_datadir}/nano

%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 4.3-3
- Import into wip

* Wed Nov 27 2019 Kamil Dudka <kdudka@redhat.com> - 4.3-3
- refresh the edit window when exiting from the help viewer

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Kamil Dudka <kdudka@redhat.com> - 4.3-1
- new upstream release

* Tue May 28 2019 Kamil Dudka <kdudka@redhat.com> - 4.2-2
- fix possible crash while opening help

* Wed Apr 24 2019 Kamil Dudka <kdudka@redhat.com> - 4.2-1
- new upstream release

* Mon Apr 15 2019 Kamil Dudka <kdudka@redhat.com> - 4.1-1
- new upstream release

* Tue Apr 02 2019 Kamil Dudka <kdudka@redhat.com> - 4.0-2
- make sure that variables on stack are initialized

* Mon Mar 25 2019 Kamil Dudka <kdudka@redhat.com> - 4.0-1
- new upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Kamil Dudka <kdudka@redhat.com> - 3.2-1
- new upstream release

* Wed Sep 19 2018 Kamil Dudka <kdudka@redhat.com> - 3.1-1
- new upstream release

* Fri Sep 14 2018 Kamil Dudka <kdudka@redhat.com> - 3.0-2
- when Ctrl+Shift+Delete has no key code, do not fall back to KEY_BACKSPACE

* Mon Sep 10 2018 Kamil Dudka <kdudka@redhat.com> - 3.0-1
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Kamil Dudka <kdudka@redhat.com> - 2.9.8-1
- new upstream release

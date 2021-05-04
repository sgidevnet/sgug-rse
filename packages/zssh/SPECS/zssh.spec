Name:           zssh
Version:        1.5c
Release:        5%{?dist}
Summary:        SSH and Telnet client with ZMODEM file transfer capability
License:        GPLv3
URL:            http://zssh.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/zssh/zssh/1.5/%{name}-%{version}.tgz
# patches from https://sources.debian.org/patches/zssh/1.5c.debian.1-7/
Patch0:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0001-Remove-build-instruction-about-lrzsz.patch
Patch1:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0002-Install-files-into-under-DESTDIR.patch
Patch2:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0003-Do-not-symlink-zssh-to-ztelnet.patch
Patch3:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0004-Use-GNU-openpty-library-for-pty.h.patch
Patch4:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0005-Do-not-call-strip-in-build-process.patch
Patch5:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0006-replace-CPPFunction-call-with-rl_completion_func_t.patch
Patch6:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0007-Fix-typo-in-man-page-zssh.1.patch
Patch7:         https://sources.debian.org/data/main/z/zssh/1.5c.debian.1-7/debian/patches/0008-Strip-build-date-from-version-string-to-enable-repro.patch
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  libtermcap-devel
BuildRequires:  autoconf
Requires:       lrzsz

%description
%{summary}.

%prep
%autosetup -p1
# remove bundled lrzsz
rm -fr lrzsz-0.12.20

%build
autoconf
%configure
%make_build

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_mandir}/man1/
%make_install
rm %{buildroot}%{_mandir}/man1/ztelnet.1*

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.5c-4
- Port patches from Debian (BZ#1716106)
- Requires lrzsz

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5c-3
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  7 2017 mosquito <sensor.wen@gmail.com> - 1.5c-1
- Initial package build

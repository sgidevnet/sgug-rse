Name: pidgin-groupchat-typing-notifications
Version: 3
Release: 3%{?dist}
Summary: Adds typing notifications for group chats in Pidgin

License: GPLv3+
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)
BuildRequires: gcc

Requires: pidgin%{?_isa}

%description
Adds typing notifications for multi-user group chats in Pidgin.
Currently only tested as working with the Hangouts plugin, but
support for other protocols will come later.

%prep
%autosetup

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
# Executing base install from makefile...
%make_install

# Setting correct chmod...
chmod 755 %{buildroot}%{_libdir}/pidgin/grouptyping.so

%files
%{_libdir}/pidgin/grouptyping.so
%license LICENSE
%doc README.md

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3-1
- Updated to version 3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2-5
- Fixed build under Fedora Rawhide.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2-1
- Updated to version 2. Use normal releases instead of Git snapshots.

* Mon Nov 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.git33a75f9
- Small SPEC fixes.

* Sun Nov 06 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.git33a75f9
- Initial commit.

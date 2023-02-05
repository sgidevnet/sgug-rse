%if 0%{?fedora} < 17 && 0%{?rhel} < 7
%global _bindir   /bin
%endif

Summary:          Re-implementation for Unix of the Plan 9 shell
Name:             rc
Version:          1.7.4
Release:          12%{?dist}
License:          zlib
URL:              http://tobold.org/article/rc
Source0:          http://static.tobold.org/%{name}/%{name}-%{version}.tar.gz
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
Conflicts:        filesystem < 3
Provides:         /bin/rc
%endif
Requires(post):   grep
Requires(postun): sed
BuildRequires:    gcc
BuildRequires:    readline-devel

%description
Rc is a command interpreter for Plan 9 that provides similar facilities to
UNIX's Bourne shell, with some small additions and less idiosyncratic syntax.
This is a re-implementation for Unix, by Byron Rakitzis, of the Plan 9 shell.

%prep
%setup -q

%build
%configure --with-edit=gnu
%make_build

%install
%make_install

%check
make check

%post
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
grep -q "^/bin/%{name}$" %{_sysconfdir}/shells 2>/dev/null || \
  echo "/bin/%{name}" >> %{_sysconfdir}/shells
%endif
grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells 2>/dev/null || \
  echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells

%postun
if [ ! -x %{_bindir}/%{name} ]; then
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
  sed -e 's@^/bin/%{name}$@POSTUNREMOVE@' -e '/^POSTUNREMOVE$/d' -i %{_sysconfdir}/shells
%endif
  sed -e 's@^%{_bindir}/%{name}$@POSTUNREMOVE@' -e '/^POSTUNREMOVE$/d' -i %{_sysconfdir}/shells
fi

%files
%license COPYING
%doc ChangeLog AUTHORS EXAMPLES NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.4-11
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.7.4-4
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Robert Scheck <robert@fedoraproject.org> 1.7.4-1
- Upgrade to 1.7.4

* Sat May 09 2015 Robert Scheck <robert@fedoraproject.org> 1.7.3-1
- Upgrade to 1.7.3

* Wed Apr 08 2015 Robert Scheck <robert@fedoraproject.org> 1.7.2-1
- Upgrade to 1.7.2
- Initial spec file for Fedora and Red Hat Enterprise Linux

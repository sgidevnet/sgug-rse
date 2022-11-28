Name:           txt2man
Version:        1.6.0
Release:        7%{?dist}
Summary:        Convert flat ASCII text to man page format

License:        GPLv2+
URL:            https://github.com/mvertes/txt2man
Source0:        https://github.com/mvertes/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       gawk

%description
tx2man is a shell script using gnu awk, that should run on any
Unix-like system. The syntax of the ASCII text is very straightforward
and looks very much like the output of the man(1) program.

%prep
# No idea why but github archive is prepending the name twice
%setup -q -n %{name}-%{name}-%{version}

%build
#no build needed

%install
rm -rf $RPM_BUILD_ROOT
#manual install
install -p -m 0755 -D bookman $RPM_BUILD_ROOT%{_bindir}/bookman
install -p -m 0755 -D src2man $RPM_BUILD_ROOT%{_bindir}/src2man
install -p -m 0755 -D txt2man $RPM_BUILD_ROOT%{_bindir}/txt2man

install -p -m 0644 -D bookman.1 $RPM_BUILD_ROOT%{_mandir}/man1/bookman.1
install -p -m 0644 -D src2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/src2man.1
install -p -m 0644 -D txt2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/txt2man.1



%files
%doc COPYING Changelog README
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.0-1
- Update to latest upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon May 09 2011 Adam Miller <maxamillion@fedoraproject.org> - 1.5.6-1
- New upstream release, fixes old bugs.
- Upstream release notes claim POSIX shell code, but bookman still relies on
  bash styled syntax so we continue to patch it out.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 04 2009 Sindre Pedersen Bjordal <sindrepb@fedoraproject.org> - 1.5.5-1
- Initial build
- Include debian patch to fix bashisms

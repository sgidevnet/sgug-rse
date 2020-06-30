Name:		auto-destdir
Version:	1.11
Release:	17%{?dist}
Summary:	Automate DESTDIR support for "make install"

License:	MIT
URL:		http://www.dwheeler.com/auto-destdir
Source0:	http://www.dwheeler.com/auto-destdir/%{name}-%{version}.tgz

BuildArch:	noarch

%description
Auto-DESTDIR is a set of programs for POSIX/Unix/Linux systems that helps
automate program installation from source code.  It can be useful for
creating native packages (e.g., RPM or deb), or for installing programs
from source code to be managed by tools like GNU stow.

The Auto-DESTDIR tools (run-redir and make-redir) redirect file installations
so that the installed files are placed inside the the $DESTDIR directory,
even if the provided makefile doesn't support the DESTDIR convention.
In most cases you can simply replace "make install" with
"make-redir DESTDIR=... install".

%prep
%setup -q


%build
%configure --scriptdir="%{_libexecdir}/%{name}"
make


%install
make DESTDIR="%{buildroot}" install
chmod a-x %{buildroot}/%{_mandir}/man1/*


%files
%{_bindir}/*
%{_libexecdir}/%{name}/
%doc %{_mandir}/man1/*
%doc README
%license COPYING

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 1.11-8
- Use license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.11-3
- Rebuild for Fedora 17 mass rebuild
- Drop unnecessary spec file elements (BuildRoot, clean, etc.)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 09 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.11-1
- Added wrapper for "touch"
- Auto-create DESTDIR directory if it doesn't exist and something is redirected.
- Simplified implementation.
- Documentation: Fixed make-redir(1) so it describes how to use in RPM spec
  files, more override info, note that it's useful with GNU stow, etc.
- make-redir now overrides MKDIR_P and mkdir_p by default

* Wed Sep 02 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.10-1
- Test suite improvements: More tests, runs on Cygwin.
- Simplified .spec file.

* Sun Aug 23 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.7-1
- Shortened description
- Moved scripts to libexecdir.
- Fixed missing '$' in run-redir
- See https://bugzilla.redhat.com/show_bug.cgi?id=518766 for more info.

* Sun Aug 23 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.6-1
- New version 1.6.
- Significantly improved test suite, with a few found and fixed bugs
- Refactored code

* Sun Aug 23 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.5-1
- New version 1.5.
- Fix ./configure so error messages report the problem
  correctly and handle empty values correctly.
- Remove debug-disabler in RPM .spec file.

* Sun Aug 23 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.4-2
- Switch from ./configure to %%configure

* Sat Aug 22 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.4-1
- Change so run-redir isn't modified in place. Simplifies Debian packaging.

* Fri Aug 21 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.3-1
- Added wrapper for "mv"

* Mon Aug 12 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.1-1
- Modified to better comply with GNU coding standards

* Mon Feb 16 2009 David A. Wheeler <dwheeler , at, dwheeler dot com> 1.0-1
- Initial version. Wraps install, mkdir, cp, ln.


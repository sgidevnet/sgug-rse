Name:           fedpkg-minimal
Version:        1.1.0
Release:        13%{?dist}
Summary:        Script to allow fedpkg fetch to work

License:        GPLv2+
URL:            https://pagure.io/%{name}
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-Read-BSD-formatted-sources.patch
Patch1:         0002-remove-the-in-two-steps.patch
Patch2:         0003-Make-curl-follow-redirects.patch
Patch3:         0004-Update-baseurl-to-src.fpo.patch


BuildArch:      noarch

Requires:       curl

Conflicts:      fedpkg


%description
Script for use in Koji to allow sources to be fetched

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
install -d %{buildroot}%{_bindir}
install -pm 755 bin/fedpkg %{buildroot}%{_bindir}/fedpkg


%files
%doc README.md LICENSE AUTHORS.md
%{_bindir}/fedpkg

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-7
- use upstreamed more robust patches for switch to https and src

* Mon Dec 12 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-6
- switch the lookcaside cache url to src.fp.o and use https://

* Sun Dec 11 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-5
- update patch to support new sources format to work on rhel6

* Thu Dec 08 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-4
- add patch to support new sources format

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Pavol Babincak <pbabinca@redhat.com> - 1.1.0-1
- Verify sources
- Add Till and Jesse to Authors and Till to Copyright header
- Remove redundant whitespace at the end of file
- Simplify parsing sources file
- Abort on errors
- Added copyright and authors
- Use curl instead of wget

* Wed Mar 04 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-3
- Use %%setup instead of %%autosetup in %%prep
- Define BuildRoot
- Move license back under %%doc macro

* Fri Feb 06 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-2
- use %%license tag instead of %%doc for the LICENSE file (rhbz#1189611)
- preserve timestamp of original installed files (rhbz#1189611)
- drop installation README.md and LICENSE from %%install section to install it
  only once from %%doc and %%license macro (rhbz#1189611)

* Wed Feb 04 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-1
- Initial release made from
  http://koji.fedoraproject.org/koji/packageinfo?packageID=17475

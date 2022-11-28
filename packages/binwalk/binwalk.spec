Name:           binwalk
Version:        2.1.1
Release:        12%{?dist}
Summary:        Firmware analysis tool
License:        MIT
URL:            https://github.com/devttys0/binwalk
Source0:        https://github.com/devttys0/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
# Optional, for graphs and visualizations
Suggests:       python3-pyqtgraph
# Optional, for --disasm functionality
Suggests:       capstone
# Optional, for automatic extraction/decompression of files and data
Recommends:     mtd-utils gzip bzip2 tar arj p7zip p7zip-plugins cabextract squashfs-tools
Suggests:       sleuthkit

%description
Binwalk is a tool for searching a given binary image for embedded files and
executable code. Specifically, it is designed for identifying files and code
embedded inside of firmware images. Binwalk uses the python-magic library, so 
it is compatible with magic signatures created for the Unix file utility. 

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%files
%doc API.md INSTALL.md README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*.egg-info

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Scott Talbert <swt@techie.net> - 2.1.1-7
- Add p7zip-plugins as a dependency and change from Suggests to Recommends (#1511958)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Scott Talbert <swt@techie.net> - 2.1.1-1
- New upstream release 2.1.1
- Remove patches (all upstream/obsolete), switch to noarch, add suggests

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Aug 24 2015 Scott Talbert <swt@techie.net> - 2.0.0-6
- Needed to specify python3 to configure

* Mon Aug 24 2015 Scott Talbert <swt@techie.net> - 2.0.0-5
- Cherry-pick patch from upstream for python3 fix
- Add weak dependency on python3-pyqtgraph (#1248735)

* Thu Jul 30 2015 Scott Talbert <swt@techie.net> - 2.0.0-4
- Switch to python3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov  1 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-2
- Fix *.so permissions for -debuginfo

* Mon Sep 29 2014 Scott Talbert <swt@techie.net> - 2.0.0-1
- New upstream release 2.0.0 (#1085059, #1111576)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Tom Callaway <spot@fedoraproject.org> 1.2-1
- update to 1.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Adam Jackson <ajax@redhat.com> 0.4.5-1
- Initial packaging.


%bcond_without flxmlrpc

Name:           flcluster
Version:        1.0.4
Release:        5%{?dist}
Summary:        A management tool for accessing dxcluster nodes

License:        GPLv3+
URL:            http://www.w1hkj.com/
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
Source99:       flcluster.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel >= 1.3.0
%if %{with flxmlrpc}
BuildRequires:  flxmlrpc-devel >= 0.1.0
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
flcluster can connect to and display data from DX cluster servers. The three
most common server types are A←-R-Cluster, CC-Cluster, and DX Spider. The
program is designed to work stand alone or as a helper application to fldigi.
It can move call, mode, and frequency data from a spotted QSO to the appropriate
fldigi controls. It can query fldigi for the same items when generating a spot
report.


%prep
%autosetup

%if %{with flxmlrpc}
# Remove bundled xmlrpc library.
rm -rf src/xmlrpcpp
%endif


%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build


%install
%make_install

%if 0%{?fedora}
# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-1
- Update to latest upstream release.

* Mon Oct 30 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0.3-1
- Initial packaging.

Name:           flnet
Version:        7.3.2
Release:        5%{?dist}
Summary:        Amateur Radio Net Control Station

License:        GPLv3+
URL:            http://www.w1hkj.com/Net-help/index.html
Source0:        http://downloads.sourceforge.net/fldigi/%{name}-%{version}.tar.gz
Source99:       flnet.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel >= 1.3.4
BuildRequires:  flxmlrpc-devel >= 0.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
Net provides the Amateur Radio Net Control Station operator with a real time
tool to assist him or her in managing the net activities.  A single screen with
multiple windows is used to allow rapid entry, search, pick and display of all
stations calling in to the net.  All operations on the main screen are
accomplished with keyboard entries only.  No mouse action is required to
perform the net control functions.  Experience has shown that most net control
operators prefer this method of operation to improve the speed of entry and
selection.


%prep
%autosetup

# Remove bundled xmlrpc library
rm -rf src/xmlrpcpp


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
desktop-file-validate %{buildroot}/%{_datadir}/applications/flnet.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/flnet
%{_datadir}/applications/flnet.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/flnet.xpm


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Richard Shaw <hobbes1069@gmail.com> - 7.3.2-1
- Update to latest upstream release.
- Add appdata file.

* Fri Oct 28 2016 Richard Shaw <hobbes1069@gmail.com> - 7.3.1-1
- Update to latest upstream release.

* Tue Oct 25 2016 Richard Shaw <hobbes1069@gmail.com> - 7.2.6-1
- Update to latest upstream release.

* Wed Dec  2 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.5-1
- Update to latest upstream release.

* Tue Nov  3 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.4-1
- Update to latest upstream release.

* Tue May  5 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.3-1
- Update to latest upstream release.
- Build with external xmlrpc library.
- Update package to use %%license where appropriate.

* Wed Mar 11 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.2-1
- Update to latest upstream release.

* Tue Jan 13 2015 Richard Shaw <hobbes1069@gmail.com> - 7.2.1-1
- Update to latest upstream release.

* Mon Feb  3 2014 Richard Shaw <hobbes1069@gmail.com> - 7.0.1-1
- Initial packaging.

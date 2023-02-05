Name: easy-rsa
Version:  3.0.6
Release:  2%{?dist}

Summary: Simple shell based CA utility
License: GPLv2

URL: https://github.com/OpenVPN/easy-rsa
Source0: https://github.com/OpenVPN/easy-rsa/releases/download/v%{version}/EasyRSA-unix-v%{version}.tgz

Requires: openssl
BuildArch: noarch


%description
This is a small RSA key management package, based on the openssl
command line tool, that can be found in the easy-rsa subdirectory
of the OpenVPN distribution. While this tool is primary concerned
with key management for the SSL VPN application space, it can also
be used for building web certificates.


%prep
%setup -qn EasyRSA-v%{version}
%build
#Nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/easy-rsa/%{version}/
(
cd %{buildroot}%{_datadir}/easy-rsa
ln -s %{version} 3.0
ln -s %{version} 3
)
cp -rp easyrsa %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp openssl-easyrsa.cnf %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp x509-types %{buildroot}%{_datadir}/easy-rsa/%{version}/

%files
%doc COPYING.md ChangeLog *.md vars.example
%license gpl-2.0.txt
%{_datadir}/easy-rsa/

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0.6-1
- Update to 3.0.6.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.0.3-1
-3.0.3, fix for new openssl.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Jon Ciesla <limburgher@gmail.com> - 3.0.1-1
- Latest stable upstream, BZ 1304339.
- Updated path structure, François Kooman fkooman@tuxed.net

* Mon Sep 21 2015 Jon Ciesla <limburgher@gmail.com> - 3.0.0-1
- Latest stable upstream.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Jon Ciesla <limburgher@gmail.com> - 2.2.2-1
- Latest stable upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Jon Ciesla <limburgher@gmail.com> - 2.2.0-2
- Update cp to preserve timestamps.

* Wed May 22 2013 Jon Ciesla <limburgher@gmail.com> - 2.2.0-1
- Create.

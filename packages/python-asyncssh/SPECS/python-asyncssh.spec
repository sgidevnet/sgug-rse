%global         srcname  asyncssh
%global         desc     Python 3 library for asynchronous client and\
server-side SSH communication. It uses the Python asyncio module and\
implements many SSH protocol features such as the various channels,\
SFTP, SCP, forwarding, session multiplexing over a connection and more.

Name:           python-%{srcname}
Version:        2.2.1
Release:        3%{?dist}
Summary:        Asynchronous SSH for Python

License:        EPL-2.0 or GPLv2+
URL:            https://github.com/ronf/asyncssh
Source0:        %pypi_source

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel

BuildRequires:  python3-setuptools

# required by setup.py test
BuildRequires:  openssh
BuildRequires:  openssl
BuildRequires:  python3-bcrypt
BuildRequires:  python3-gssapi
BuildRequires:  python3-libnacl
BuildRequires:  python3-pyOpenSSL

BuildRequires:  python3-cryptography
Requires:       python3-cryptography

# for ed25519 etc.
Recommends:     python3-libnacl

# for OpenSSH private key encryption
Suggests:       python3-bcrypt
# for GSSAPI key exchange/authentication
Suggests:       python3-gssapi
# for X.509 certificate authentication
Suggests:       python3-pyOpenSSL
# for U2F etc. support
Suggests:       python3-fido2

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
sed -i '1,1s@^#!.*$@#!%{__python3}@' examples/*.py
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst examples
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 2.2.1-3
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Georg Sauthoff <mail@gms.tf> - 2.2.1-1
- Update to latest upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Georg Sauthoff <mail@gms.tf> - 2.1.0-1
- Update to latest upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Sat Apr 13 2019 Georg Sauthoff <mail@gms.tf> - 1.16.1-1
- Update to latest upstream version
* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 1.15.1-1
- Update to more recent upstream version
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Sat Dec  8 2018 Georg Sauthoff <mail@gms.tf> - 1.15.0-1
- Update to latest upstream version
* Sun Sep  9 2018 Georg Sauthoff <mail@gms.tf> - 1.14.0-1
- Update to latest upstream version
* Sat Jul 28 2018 Georg Sauthoff <mail@gms.tf> - 1.13.3-1
- initial packaging
